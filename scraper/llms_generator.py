"""Generator for llms.txt file following the llmstxt.org standard."""

from pathlib import Path
from typing import List
from .fetcher import PageResult


# Category descriptions for llms.txt
CATEGORY_DESCRIPTIONS = {
    "commands": "Language commands, statements, functions, and chip-specific documentation",
    "configuration": "CONFIG directives for hardware initialization",
    "directives": "Compiler directives ($) for build configuration",
    "hardware": "AVR internal hardware documentation",
    "hardware/modern-avr": "XMEGA, xTiny, MegaX, and AVR-Dx series documentation",
    "ide": "IDE menus, options, and tools",
    "libraries/lcd": "Text and graphical LCD display libraries",
    "libraries/i2c": "I2C/TWI communication protocol",
    "libraries/spi": "SPI communication protocol",
    "libraries/1wire": "Dallas 1-Wire protocol",
    "libraries/tcpip": "TCP/IP networking with W5100/W5500",
    "libraries/usb": "USB communication",
    "libraries/can": "CAN bus communication",
    "libraries/rainbow": "WS2812 RGB LED control",
    "libraries/ft800": "FT800/FT810 GPU display controller",
    "libraries/remote-control": "RC5/RC6 infrared remote control",
}

# Essential pages to include in main sections
ESSENTIAL_PAGES = {
    "commands": ["dim", "print", "input", "if_then_else_end_if", "for_next",
                 "do_loop", "sub", "declare_function", "config", "getadc"],
    "configuration": ["config_lcd", "config_timer0", "config_timer1",
                      "config_adc", "config_spi", "config_com1"],
}


def generate_llms_txt(results: List[PageResult], output_dir: Path) -> str:
    """Generate llms.txt content following llmstxt.org standard."""

    lines = [
        "# BASCOM-AVR Documentation",
        "",
        "> BASCOM-AVR is a BASIC compiler for Atmel AVR microcontrollers by MCS Electronics. "
        "It provides a high-level BASIC language for programming AVR chips with built-in "
        "support for LCD displays, I2C, SPI, 1-Wire, USB, CAN, and TCP/IP networking.",
        "",
    ]

    # Group by category
    successful = [r for r in results if r.success]
    categories = {}
    for r in successful:
        if r.category not in categories:
            categories[r.category] = []
        categories[r.category].append(r)

    # Define category order - essential first
    primary_categories = [
        "commands",
        "configuration",
        "directives",
    ]

    secondary_categories = [
        "hardware",
        "hardware/modern-avr",
        "ide",
    ]

    library_categories = [
        "libraries/lcd",
        "libraries/i2c",
        "libraries/spi",
        "libraries/1wire",
        "libraries/tcpip",
        "libraries/usb",
        "libraries/can",
        "libraries/rainbow",
        "libraries/ft800",
        "libraries/remote-control",
    ]

    # Build ordered list
    sorted_categories = []
    for cat in primary_categories + secondary_categories + library_categories:
        if cat in categories:
            sorted_categories.append(cat)
    for cat in sorted(categories.keys()):
        if cat not in sorted_categories:
            sorted_categories.append(cat)

    # Primary documentation sections
    lines.append("## Language Reference")
    lines.append("")

    for category in primary_categories:
        if category not in categories:
            continue
        pages = categories[category]
        pages.sort(key=lambda p: p.title.lower())

        cat_name = category.replace("/", " - ").replace("-", " ").title()
        desc = CATEGORY_DESCRIPTIONS.get(category, "")

        lines.append(f"### {cat_name}")
        if desc:
            lines.append(f"{desc}")
        lines.append("")

        for page in pages:
            rel_path = f"{category}/{page.filename}"
            lines.append(f"- [{page.title}]({rel_path})")
        lines.append("")

    # Hardware sections
    lines.append("## Hardware")
    lines.append("")

    for category in secondary_categories:
        if category not in categories:
            continue
        pages = categories[category]
        pages.sort(key=lambda p: p.title.lower())

        cat_name = category.split("/")[-1].replace("-", " ").title()
        desc = CATEGORY_DESCRIPTIONS.get(category, "")

        lines.append(f"### {cat_name}")
        if desc:
            lines.append(f"{desc}")
        lines.append("")

        for page in pages:
            rel_path = f"{category}/{page.filename}"
            lines.append(f"- [{page.title}]({rel_path})")
        lines.append("")

    # Libraries section
    lines.append("## Libraries")
    lines.append("")

    for category in library_categories:
        if category not in categories:
            continue
        pages = categories[category]
        pages.sort(key=lambda p: p.title.lower())

        cat_name = category.split("/")[-1].replace("-", " ").title()
        desc = CATEGORY_DESCRIPTIONS.get(category, "")

        lines.append(f"### {cat_name}")
        if desc:
            lines.append(f"{desc}")
        lines.append("")

        for page in pages:
            rel_path = f"{category}/{page.filename}"
            lines.append(f"- [{page.title}]({rel_path})")
        lines.append("")

    # Footer
    lines.extend([
        "---",
        "",
        "Source: <https://avrhelp.mcselec.com/>",
        "",
        "Copyright MCS Electronics. All rights reserved.",
        "",
    ])

    content = "\n".join(lines)

    # Write to file
    llms_path = output_dir / "llms.txt"
    llms_path.write_text(content, encoding="utf-8")

    return content
