"""Utility functions for the scraper."""

import re
from urllib.parse import urljoin, urlparse

BASE_URL = "https://avrhelp.mcselec.com/"


def normalize_url(url: str, base: str = BASE_URL) -> str:
    """Normalize a URL to absolute form."""
    if not url:
        return ""
    return urljoin(base, url)


def is_internal_link(url: str) -> bool:
    """Check if URL is internal to the documentation site."""
    if not url:
        return False
    parsed = urlparse(url)
    if parsed.scheme and parsed.scheme not in ("http", "https"):
        return False
    if parsed.netloc and "mcselec.com" not in parsed.netloc:
        return False
    return url.endswith(".htm") or url.endswith(".html")


def htm_to_md_filename(htm_name: str) -> str:
    """Convert .htm filename to .md filename."""
    name = htm_name.replace(".html", "").replace(".htm", "")
    return f"{name}.md"


def sanitize_filename(name: str) -> str:
    """Sanitize a string for use as a filename."""
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r'_+', '_', name)
    return name.strip('_').lower()


def categorize_page(filename: str, title: str = "") -> str:
    """Determine which category/folder a page belongs to."""
    fname = filename.lower()
    title_lower = title.lower() if title else ""

    # Configuration directives
    if fname.startswith("config_") or fname.startswith("config"):
        return "configuration"

    # Compiler directives (start with _ or $)
    if fname.startswith("_") or "directive" in title_lower:
        return "directives"

    # File operations
    if fname in ["bsave", "bload", "get", "put", "open", "close", "seek",
                 "kill", "dir", "mkdir", "rmdir", "chdir", "eof", "lof",
                 "loc", "freefile", "fileattr", "filelen", "flush", "write",
                 "initfilesystem", "driveinit", "drivereset"]:
        return "libraries/avr-dos"

    # I2C related
    if "i2c" in fname or "twi" in fname:
        return "libraries/i2c"

    # SPI related
    if "spi" in fname:
        return "libraries/spi"

    # 1-Wire related
    if "1w" in fname or "1wire" in fname:
        return "libraries/1wire"

    # LCD related
    if "lcd" in fname or "glcd" in fname:
        return "libraries/lcd"

    # TCP/IP related
    if "tcp" in fname or "udp" in fname or "socket" in fname or "ip" in fname:
        return "libraries/tcpip"

    # USB related
    if "usb" in fname:
        return "libraries/usb"

    # CAN related
    if "can" in fname:
        return "libraries/can"

    # Rainbow/WS2812
    if "rb_" in fname or "rainbow" in fname:
        return "libraries/rainbow"

    # FT800 display
    if "ft8" in fname or fname in ["cmd8", "cmd16", "cmd32", "rd8", "rd16",
                                    "rd32", "wr8", "wr16", "wr32"]:
        return "libraries/ft800"

    # RC5/RC6 remote control
    if "rc5" in fname or "rc6" in fname or "sony" in fname:
        return "libraries/remote-control"

    # Hardware topics
    if "avr_internal" in fname or "hardware" in fname:
        return "hardware"

    # XMEGA/XTINY/MEGAX specific
    if "xmega" in fname or "xtiny" in fname or "megax" in fname or "avrx" in fname:
        return "hardware/modern-avr"

    # IDE related
    if any(x in fname for x in ["file_", "edit_", "view", "window_", "help_",
                                 "program_", "tools_", "options_"]):
        return "ide"

    # String functions
    if fname in ["asc", "chr", "hex", "hexval", "instr", "lcase", "ucase",
                 "left", "right", "mid", "len", "ltrim", "rtrim", "trim",
                 "space", "string", "str", "val", "split", "join", "format"]:
        return "commands/strings"

    # Math functions
    if fname in ["abs", "acos", "asin", "atn", "atn2", "cos", "sin", "tan",
                 "exp", "log", "log10", "sqr", "power", "int", "fix", "round",
                 "sgn", "rnd", "mod", "max", "min", "frac"]:
        return "commands/math"

    # Control flow
    if fname in ["if_then_else_end_if", "while_wend", "do_loop", "for_next",
                 "select_case_end_select", "goto", "gosub", "return", "exit",
                 "continue", "else", "redo"]:
        return "commands/control-flow"

    # Variable/memory
    if fname in ["dim", "const", "local", "alias", "type", "defxxx"]:
        return "commands/variables"

    # Default to commands
    return "commands"


def extract_title_from_filename(filename: str) -> str:
    """Generate a readable title from filename."""
    name = filename.replace(".htm", "").replace(".html", "")
    name = name.replace("_", " ")
    return name.title()
