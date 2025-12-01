# BASCOM-AVR Documentation

Markdown documentation scraped from the official BASCOM-AVR help at https://avrhelp.mcselec.com/

## Structure

```
docs/
├── llms.txt              # Index following llmstxt.org standard
├── commands/             # Language commands, statements, functions
├── configuration/        # CONFIG directives
├── directives/           # Compiler directives ($)
├── hardware/             # AVR internal hardware
│   └── modern-avr/       # XMEGA, xTiny, MegaX, AVR-Dx
├── ide/                  # IDE menus and tools
└── libraries/
    ├── lcd/              # Text and graphical LCD
    ├── i2c/              # I2C/TWI protocol
    ├── spi/              # SPI protocol
    ├── 1wire/            # Dallas 1-Wire
    ├── tcpip/            # TCP/IP with W5100/W5500
    ├── usb/              # USB communication
    ├── can/              # CAN bus
    ├── rainbow/          # WS2812 RGB LEDs
    ├── ft800/            # FT800/FT810 GPU
    └── remote-control/   # RC5/RC6 infrared
```

## Scraper Usage

### Setup

```bash
python -m venv venv
# Windows
venv\Scripts\pip install -r requirements.txt
# Linux/Mac
venv/bin/pip install -r requirements.txt
```

### Scrape Documentation

```bash
# Full scrape (discovers all pages)
python -m scraper.main -o docs

# Quick test (entry points only)
python -m scraper.main -o docs --skip-crawl

# Adjust workers and timeout
python -m scraper.main -o docs -w 20 -t 60
```

### Regenerate llms.txt

If you modify the markdown files and need to regenerate the index:

```bash
python -m scraper.main -o docs --regenerate-llms
```

### Options

- `-o, --output` - Output directory (default: docs)
- `-w, --workers` - Number of worker threads (default: 10)
- `-t, --timeout` - Request timeout in seconds (default: 30)
- `-v, --verbose` - Enable debug logging
- `--skip-crawl` - Skip page discovery, use entry points only
- `--regenerate-llms` - Only regenerate llms.txt from existing files

## Copyright

Documentation content copyright MCS Electronics. All rights reserved.
