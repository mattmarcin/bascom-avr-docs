"""Fetcher for downloading and processing documentation pages."""

import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import requests

from .converter import Converter
from .utils import BASE_URL, categorize_page, htm_to_md_filename, extract_title_from_filename

logger = logging.getLogger(__name__)


@dataclass
class PageResult:
    """Result of fetching and converting a page."""
    url: str
    filename: str
    title: str
    markdown: str
    category: str
    metadata: dict
    success: bool
    error: Optional[str] = None


class Fetcher:
    """Fetches and converts documentation pages."""

    def __init__(self, output_dir: str, max_workers: int = 10, timeout: int = 30):
        self.output_dir = Path(output_dir)
        self.max_workers = max_workers
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "BASCOM-AVR-Docs-Scraper/1.0"
        })
        self.converter = Converter()
        self.results: list[PageResult] = []

    def fetch_page(self, url: str) -> PageResult:
        """Fetch a single page and convert it to markdown."""
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)

        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()

            markdown, title, metadata = self.converter.convert(response.text)

            if not title:
                title = extract_title_from_filename(filename)

            category = categorize_page(filename, title)
            md_filename = htm_to_md_filename(filename)

            return PageResult(
                url=url,
                filename=md_filename,
                title=title,
                markdown=markdown,
                category=category,
                metadata=metadata,
                success=True
            )

        except requests.RequestException as e:
            logger.error(f"Failed to fetch {url}: {e}")
            return PageResult(
                url=url,
                filename=htm_to_md_filename(filename),
                title="",
                markdown="",
                category="",
                metadata={},
                success=False,
                error=str(e)
            )
        except Exception as e:
            logger.error(f"Error processing {url}: {e}")
            return PageResult(
                url=url,
                filename=htm_to_md_filename(filename),
                title="",
                markdown="",
                category="",
                metadata={},
                success=False,
                error=str(e)
            )

    def save_page(self, result: PageResult) -> bool:
        """Save a converted page to disk."""
        if not result.success or not result.markdown:
            return False

        # Create category directory
        category_dir = self.output_dir / result.category
        category_dir.mkdir(parents=True, exist_ok=True)

        # Save markdown file
        output_path = category_dir / result.filename
        try:
            output_path.write_text(result.markdown, encoding="utf-8")
            logger.debug(f"Saved: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to save {output_path}: {e}")
            return False

    def fetch_all(self, urls: set[str], progress_callback=None) -> list[PageResult]:
        """Fetch all pages using thread pool."""
        total = len(urls)
        completed = 0

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self.fetch_page, url): url for url in urls}

            for future in as_completed(futures):
                url = futures[future]
                try:
                    result = future.result()
                    self.results.append(result)

                    if result.success:
                        self.save_page(result)

                    completed += 1
                    if progress_callback:
                        progress_callback(completed, total, result)
                    else:
                        logger.info(f"[{completed}/{total}] {result.filename}: {'OK' if result.success else 'FAILED'}")

                except Exception as e:
                    logger.error(f"Error processing {url}: {e}")
                    completed += 1

        return self.results

    def close(self):
        """Close the session."""
        self.session.close()

    def get_statistics(self) -> dict:
        """Get statistics about the fetch operation."""
        successful = [r for r in self.results if r.success]
        failed = [r for r in self.results if not r.success]

        categories = {}
        for r in successful:
            cat = r.category
            if cat not in categories:
                categories[cat] = 0
            categories[cat] += 1

        return {
            "total": len(self.results),
            "successful": len(successful),
            "failed": len(failed),
            "categories": categories,
            "failed_urls": [r.url for r in failed]
        }
