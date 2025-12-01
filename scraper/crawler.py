"""Crawler to discover all documentation pages."""

import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Set
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from .utils import BASE_URL, is_internal_link, normalize_url

logger = logging.getLogger(__name__)


class Crawler:
    """Discovers all documentation pages by crawling from entry points."""

    def __init__(self, max_workers: int = 10, timeout: int = 30):
        self.max_workers = max_workers
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "BASCOM-AVR-Docs-Scraper/1.0"
        })
        self.discovered_urls: Set[str] = set()
        self.visited_urls: Set[str] = set()

    def extract_links(self, url: str) -> Set[str]:
        """Extract all internal links from a page."""
        links = set()
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "lxml")

            for a_tag in soup.find_all("a", href=True):
                href = a_tag["href"]
                if is_internal_link(href):
                    full_url = normalize_url(href, url)
                    # Only include .htm files from the same domain
                    if "mcselec.com" in full_url or not full_url.startswith("http"):
                        full_url = normalize_url(href, BASE_URL)
                        links.add(full_url)

        except requests.RequestException as e:
            logger.warning(f"Failed to fetch {url}: {e}")

        return links

    def crawl_page(self, url: str) -> Set[str]:
        """Crawl a single page and return new links found."""
        if url in self.visited_urls:
            return set()

        self.visited_urls.add(url)
        logger.debug(f"Crawling: {url}")

        new_links = self.extract_links(url)
        return new_links - self.discovered_urls

    def discover_all_pages(self, entry_points: list[str] = None) -> Set[str]:
        """Discover all pages starting from entry points."""
        if entry_points is None:
            entry_points = [
                f"{BASE_URL}index.htm",
                f"{BASE_URL}tableofcontents.htm",
                f"{BASE_URL}functionalreference.htm",
            ]

        # Start with entry points
        self.discovered_urls = set(entry_points)
        to_crawl = set(entry_points)

        while to_crawl:
            logger.info(f"Crawling {len(to_crawl)} pages, {len(self.discovered_urls)} discovered so far")

            new_links = set()
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = {executor.submit(self.crawl_page, url): url for url in to_crawl}

                for future in as_completed(futures):
                    try:
                        links = future.result()
                        new_links.update(links)
                    except Exception as e:
                        logger.error(f"Error crawling: {e}")

            self.discovered_urls.update(new_links)
            to_crawl = new_links

        logger.info(f"Discovery complete. Found {len(self.discovered_urls)} pages.")
        return self.discovered_urls

    def close(self):
        """Close the session."""
        self.session.close()
