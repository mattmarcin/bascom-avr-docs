#!/usr/bin/env python3
"""Main entry point for the BASCOM-AVR documentation scraper."""

import argparse
import logging
import re
import sys
from pathlib import Path

from .crawler import Crawler
from .fetcher import Fetcher
from .llms_generator import generate_llms_txt, CATEGORY_DESCRIPTIONS

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def extract_title(content: str, filename: str) -> str:
    """Extract title from markdown content."""
    match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return filename.replace('_', ' ').replace('.md', '').title()


def regenerate_llms_from_files(docs_dir: Path) -> str:
    """Regenerate llms.txt from existing markdown files."""
    lines = [
        "# BASCOM-AVR Documentation",
        "",
        "> BASCOM-AVR is a BASIC compiler for Atmel AVR microcontrollers by MCS Electronics. "
        "It provides a high-level BASIC language for programming AVR chips with built-in "
        "support for LCD displays, I2C, SPI, 1-Wire, USB, CAN, and TCP/IP networking.",
        "",
    ]

    # Collect all markdown files by category
    categories = {}
    for md_file in docs_dir.rglob("*.md"):
        rel_path = md_file.relative_to(docs_dir)
        parts = rel_path.parts

        # Determine category
        if len(parts) == 1:
            category = "commands"
        elif len(parts) == 2:
            category = parts[0]
        else:
            category = "/".join(parts[:-1])

        try:
            content = md_file.read_text(encoding='utf-8')
            title = extract_title(content, md_file.stem)
        except Exception:
            title = md_file.stem.replace('_', ' ').title()

        if category not in categories:
            categories[category] = []
        categories[category].append({
            'title': title,
            'path': str(rel_path).replace('\\', '/'),
        })

    # Sort pages within each category
    for cat in categories:
        categories[cat].sort(key=lambda p: p['title'].lower())

    # Define category order
    primary = ["commands", "configuration", "directives"]
    secondary = ["hardware", "hardware/modern-avr", "ide"]
    libraries = [
        "libraries/lcd", "libraries/i2c", "libraries/spi", "libraries/1wire",
        "libraries/tcpip", "libraries/usb", "libraries/can", "libraries/rainbow",
        "libraries/ft800", "libraries/remote-control"
    ]

    def add_section(header, cat_list):
        lines.append(f"## {header}")
        lines.append("")
        for category in cat_list:
            if category not in categories:
                continue
            cat_name = category.split("/")[-1].replace("-", " ").title()
            desc = CATEGORY_DESCRIPTIONS.get(category, "")
            lines.append(f"### {cat_name}")
            if desc:
                lines.append(desc)
            lines.append("")
            for page in categories[category]:
                lines.append(f"- [{page['title']}]({page['path']})")
            lines.append("")

    add_section("Language Reference", primary)
    add_section("Hardware", secondary)
    add_section("Libraries", libraries)

    # Footer
    lines.extend([
        "---", "",
        "Source: <https://avrhelp.mcselec.com/>", "",
        "Copyright MCS Electronics. All rights reserved.", "",
    ])

    content = "\n".join(lines)
    (docs_dir / "llms.txt").write_text(content, encoding="utf-8")
    return content


def generate_context7_files(docs_dir: Path, context7_dir: Path) -> None:
    """Generate combined markdown files per category for context7."""
    context7_dir.mkdir(parents=True, exist_ok=True)

    # Collect all markdown files by category
    categories = {}
    for md_file in docs_dir.rglob("*.md"):
        rel_path = md_file.relative_to(docs_dir)
        parts = rel_path.parts

        # Determine category
        if len(parts) == 1:
            category = "commands"
        elif len(parts) == 2:
            category = parts[0]
        else:
            # Flatten nested like libraries/lcd -> libraries-lcd
            category = "-".join(parts[:-1])

        try:
            content = md_file.read_text(encoding='utf-8')
            title = extract_title(content, md_file.stem)
        except Exception:
            content = ""
            title = md_file.stem.replace('_', ' ').title()

        if category not in categories:
            categories[category] = []
        categories[category].append({
            'title': title,
            'content': content,
            'filename': md_file.stem,
        })

    # Sort pages within each category by title
    for cat in categories:
        categories[cat].sort(key=lambda p: p['title'].lower())

    # Category display names and descriptions
    category_info = {
        "commands": ("BASCOM-AVR Commands", "Language commands, statements, functions, and chip-specific documentation"),
        "configuration": ("Configuration Directives", "CONFIG directives for hardware initialization"),
        "directives": ("Compiler Directives", "Compiler directives ($) for build configuration"),
        "hardware": ("AVR Hardware", "AVR internal hardware documentation"),
        "hardware-modern-avr": ("Modern AVR Hardware", "XMEGA, xTiny, MegaX, and AVR-Dx series documentation"),
        "ide": ("IDE Reference", "IDE menus, options, and tools"),
        "libraries-lcd": ("LCD Libraries", "Text and graphical LCD display libraries"),
        "libraries-i2c": ("I2C Libraries", "I2C/TWI communication protocol"),
        "libraries-spi": ("SPI Libraries", "SPI communication protocol"),
        "libraries-1wire": ("1-Wire Libraries", "Dallas 1-Wire protocol"),
        "libraries-tcpip": ("TCP/IP Libraries", "TCP/IP networking with W5100/W5500"),
        "libraries-usb": ("USB Libraries", "USB communication"),
        "libraries-can": ("CAN Libraries", "CAN bus communication"),
        "libraries-rainbow": ("Rainbow Libraries", "WS2812 RGB LED control"),
        "libraries-ft800": ("FT800 Libraries", "FT800/FT810 GPU display controller"),
        "libraries-remote-control": ("Remote Control Libraries", "RC5/RC6 infrared remote control"),
    }

    # Write combined file for each category
    for category, pages in categories.items():
        info = category_info.get(category, (category.replace("-", " ").title(), ""))
        title, description = info

        lines = [f"# {title}", ""]
        if description:
            lines.append(f"> {description}")
            lines.append("")

        for page in pages:
            # Add each page's content with H2 header
            lines.append(f"## {page['title']}")
            lines.append("")
            # Strip the H1 from individual page content to avoid duplicate headers
            content = page['content']
            content = re.sub(r'^#\s+.+\n*', '', content, count=1)
            lines.append(content.strip())
            lines.append("")
            lines.append("---")
            lines.append("")

        output_file = context7_dir / f"{category}.md"
        output_file.write_text("\n".join(lines), encoding="utf-8")
        logger.info(f"  Created {output_file.name} ({len(pages)} pages)")


def main():
    parser = argparse.ArgumentParser(
        description="Scrape BASCOM-AVR documentation and convert to Markdown"
    )
    parser.add_argument(
        "-o", "--output",
        default="docs",
        help="Output directory for markdown files (default: docs)"
    )
    parser.add_argument(
        "-w", "--workers",
        type=int,
        default=10,
        help="Number of worker threads (default: 10)"
    )
    parser.add_argument(
        "-t", "--timeout",
        type=int,
        default=30,
        help="Request timeout in seconds (default: 30)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    parser.add_argument(
        "--skip-crawl",
        action="store_true",
        help="Skip crawling, use known entry points only"
    )
    parser.add_argument(
        "--regenerate-llms",
        action="store_true",
        help="Only regenerate llms.txt from existing markdown files"
    )
    parser.add_argument(
        "--generate-context7",
        action="store_true",
        help="Generate combined markdown files for context7 in context7/ folder"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Handle --regenerate-llms mode
    if args.regenerate_llms:
        logger.info("Regenerating llms.txt from existing markdown files...")
        regenerate_llms_from_files(output_dir)
        logger.info(f"llms.txt regenerated at: {output_dir / 'llms.txt'}")
        return 0

    # Handle --generate-context7 mode
    if args.generate_context7:
        context7_dir = output_dir.parent / "context7"
        logger.info(f"Generating context7 files from {output_dir}...")
        generate_context7_files(output_dir, context7_dir)
        logger.info(f"Context7 files created in: {context7_dir}")
        return 0

    logger.info("=" * 60)
    logger.info("BASCOM-AVR Documentation Scraper")
    logger.info("=" * 60)

    # Phase 1: Discover all pages
    logger.info("\nPhase 1: Discovering documentation pages...")
    crawler = Crawler(max_workers=args.workers, timeout=args.timeout)

    try:
        if args.skip_crawl:
            # Use only entry points for quick testing
            from .utils import BASE_URL
            urls = {
                f"{BASE_URL}index.htm",
                f"{BASE_URL}tableofcontents.htm",
                f"{BASE_URL}functionalreference.htm",
            }
        else:
            urls = crawler.discover_all_pages()

        logger.info(f"Found {len(urls)} pages to process")

    finally:
        crawler.close()

    # Phase 2: Fetch and convert all pages
    logger.info("\nPhase 2: Fetching and converting pages...")
    fetcher = Fetcher(
        output_dir=str(output_dir),
        max_workers=args.workers,
        timeout=args.timeout
    )

    def progress(completed, total, result):
        status = "OK" if result.success else "FAILED"
        logger.info(f"[{completed}/{total}] {result.filename}: {status}")

    try:
        results = fetcher.fetch_all(urls, progress_callback=progress)

        # Phase 3: Generate llms.txt
        logger.info("\nPhase 3: Generating llms.txt...")
        generate_llms_txt(results, output_dir)

        # Print statistics
        stats = fetcher.get_statistics()
        logger.info("\n" + "=" * 60)
        logger.info("Scraping Complete!")
        logger.info("=" * 60)
        logger.info(f"Total pages: {stats['total']}")
        logger.info(f"Successful: {stats['successful']}")
        logger.info(f"Failed: {stats['failed']}")

        if stats['categories']:
            logger.info("\nPages by category:")
            for cat, count in sorted(stats['categories'].items()):
                logger.info(f"  {cat}: {count}")

        if stats['failed_urls']:
            logger.warning("\nFailed URLs:")
            for url in stats['failed_urls']:
                logger.warning(f"  {url}")

        logger.info(f"\nOutput directory: {output_dir.absolute()}")
        logger.info(f"llms.txt created at: {output_dir / 'llms.txt'}")

    finally:
        fetcher.close()

    return 0 if stats['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
