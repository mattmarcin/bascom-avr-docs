"""HTML to Markdown converter for BASCOM-AVR documentation."""

import re
import html2text
from bs4 import BeautifulSoup, NavigableString

from .utils import htm_to_md_filename


class Converter:
    """Converts BASCOM-AVR HTML documentation to Markdown."""

    def __init__(self):
        self.h2t = html2text.HTML2Text()
        self.h2t.body_width = 0  # Don't wrap lines
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.ignore_emphasis = False
        self.h2t.skip_internal_links = False
        self.h2t.inline_links = True
        self.h2t.protect_links = True

    def extract_content(self, html: str) -> tuple[str, str, dict]:
        """Extract main content, title, and metadata from HTML.

        Returns:
            tuple: (content_html, title, metadata_dict)
        """
        soup = BeautifulSoup(html, "lxml")
        metadata = {}

        # Extract title
        title = ""
        title_tag = soup.find("title")
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Try to find the main content div
        content_div = soup.find("div", id="idcontent")
        if not content_div:
            content_div = soup.find("div", id="innerdiv")
        if not content_div:
            content_div = soup.body

        if not content_div:
            return "", title, metadata

        # Remove navigation elements
        for nav in content_div.find_all("div", id="idheader"):
            nav.decompose()
        for nav in content_div.find_all("div", class_="nonscroll"):
            nav.decompose()
        for script in content_div.find_all("script"):
            script.decompose()
        for style in content_div.find_all("style"):
            style.decompose()

        # Remove navigation links at top (Top, Previous, Next)
        for a_tag in content_div.find_all("a"):
            text = a_tag.get_text(strip=True)
            if text in ["Top", "Previous", "Next", "[Top]", "[Previous]", "[Next]"]:
                # Remove the parent if it's just navigation
                parent = a_tag.parent
                a_tag.decompose()
                if parent and parent.name in ["p", "div"]:
                    remaining = parent.get_text(strip=True)
                    if not remaining or remaining in ["| |", "|", "||"]:
                        parent.decompose()

        # Extract See Also links for metadata
        see_also = []
        for text in content_div.find_all(string=re.compile(r"See\s+[Aa]lso", re.I)):
            parent = text.parent
            if parent:
                for a_tag in parent.find_all("a"):
                    see_also.append({
                        "text": a_tag.get_text(strip=True),
                        "href": a_tag.get("href", "")
                    })
        if see_also:
            metadata["see_also"] = see_also

        return str(content_div), title, metadata

    def convert_links(self, markdown: str) -> str:
        """Convert .htm links to .md links in markdown."""
        # Convert internal .htm links to .md (handles both regular and angle-bracket syntax)
        # Pattern: [text](<url.htm>) or [text](url.htm)
        markdown = re.sub(
            r'\[([^\]]+)\]\(<?([^)>]+)\.htm>?\)',
            lambda m: f'[{m.group(1)}]({m.group(2)}.md)',
            markdown
        )
        markdown = re.sub(
            r'\[([^\]]+)\]\(<?([^)>]+)\.html>?\)',
            lambda m: f'[{m.group(1)}]({m.group(2)}.md)',
            markdown
        )
        return markdown

    def clean_markdown(self, markdown: str) -> str:
        """Clean up the converted markdown."""
        # Remove excessive blank lines
        markdown = re.sub(r'\n{4,}', '\n\n\n', markdown)

        # Clean up whitespace around headers
        markdown = re.sub(r'\n+(#{1,6})', r'\n\n\1', markdown)

        # Ensure code blocks are properly formatted
        # Look for patterns that suggest code (BASCOM syntax)
        lines = markdown.split('\n')
        in_code_block = False
        result_lines = []

        code_indicators = [
            r'^\s*\$',  # Compiler directives
            r'^\s*(Dim|Config|Print|Input|If|Then|Else|End|For|Next|Do|Loop|While|Wend|Select|Case|Sub|Function|Declare)\b',
            r'^\s*(Goto|Gosub|Return|Exit|Enable|Disable|On|Waitms|Wait|Set|Reset|Toggle)\b',
            r"^\s*'",  # Comments
            r'^\s*#',  # Preprocessor
        ]

        i = 0
        while i < len(lines):
            line = lines[i]

            # Check if this looks like start of code
            is_code_line = any(re.match(pattern, line, re.I) for pattern in code_indicators)

            if is_code_line and not in_code_block:
                # Look ahead to see if there are multiple code lines
                code_lines = [line]
                j = i + 1
                while j < len(lines):
                    next_line = lines[j]
                    if not next_line.strip():
                        code_lines.append(next_line)
                        j += 1
                        continue
                    is_next_code = any(re.match(pattern, next_line, re.I) for pattern in code_indicators)
                    if is_next_code or (next_line.startswith(' ') and len(next_line.strip()) > 0):
                        code_lines.append(next_line)
                        j += 1
                    else:
                        break

                if len([l for l in code_lines if l.strip()]) >= 2:
                    result_lines.append('```vb')
                    result_lines.extend(code_lines)
                    result_lines.append('```')
                    i = j
                    continue

            result_lines.append(line)
            i += 1

        markdown = '\n'.join(result_lines)

        # Remove any remaining pipe-only lines (navigation remnants)
        markdown = re.sub(r'^\s*\|[\s|]*\|\s*$', '', markdown, flags=re.MULTILINE)

        return markdown.strip()

    def convert(self, html: str) -> tuple[str, str, dict]:
        """Convert HTML to Markdown.

        Returns:
            tuple: (markdown_content, title, metadata)
        """
        content_html, title, metadata = self.extract_content(html)

        if not content_html:
            return "", title, metadata

        # Convert to markdown
        markdown = self.h2t.handle(content_html)

        # Post-process
        markdown = self.convert_links(markdown)
        markdown = self.clean_markdown(markdown)

        # Add title as H1 if not present
        if title and not markdown.startswith('#'):
            markdown = f"# {title}\n\n{markdown}"

        return markdown, title, metadata
