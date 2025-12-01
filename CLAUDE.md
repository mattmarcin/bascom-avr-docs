# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python scraper that downloads BASCOM-AVR documentation from https://avrhelp.mcselec.com/ and converts it to Markdown format. BASCOM-AVR is a BASIC compiler for Atmel AVR microcontrollers by MCS Electronics.

## Commands

```bash
# Setup virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Run the scraper
python -m scraper.main

# Run with options
python -m scraper.main -o docs -w 10 -v  # verbose, 10 workers
python -m scraper.main --skip-crawl  # quick test with entry points only
```

## Architecture

```
bascom-avr-docs/
├── scraper/
│   ├── main.py          # Entry point, CLI argument handling
│   ├── crawler.py       # Discovers pages via threaded crawling from TOC
│   ├── fetcher.py       # Downloads pages with thread pool
│   ├── converter.py     # HTML→Markdown using BeautifulSoup + html2text
│   ├── llms_generator.py # Generates llms.txt index
│   └── utils.py         # URL handling, categorization logic
├── docs/                # Output: categorized markdown files + llms.txt
├── requirements.txt
└── venv/
```

## Key Design Decisions

- **Threading**: Uses `ThreadPoolExecutor` for parallel page fetching (configurable workers)
- **Categorization**: Pages auto-sorted into folders based on filename patterns in `utils.py:categorize_page()`
- **Link conversion**: Internal `.htm` links converted to `.md` in output
- **Content extraction**: Strips navigation divs (`#idheader`), scripts, and nav links before conversion
