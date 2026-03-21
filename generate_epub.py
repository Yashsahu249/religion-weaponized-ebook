"""
generate_epub.py
Generates a standard EPUB 2 eBook for
"Religion Weaponized: The Dark Side of Faith" by Yash Sahu.

EPUB files are accepted by all major eBook retailers including
Amazon KDP (via Kindle Convert), Apple Books, Google Play Books,
Kobo, Smashwords, and Draft2Digital.

Usage:
    python generate_epub.py                      # writes religion_weaponized.epub
    python generate_epub.py --output my_book.epub
"""

import argparse
import os
import uuid

from ebooklib import epub

from ebook_content import BOOK_METADATA, CHAPTERS

# ──────────────────────────────────────────────
# CSS stylesheet embedded in the EPUB
# ──────────────────────────────────────────────
EPUB_CSS = """
body {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1em;
    line-height: 1.7;
    color: #333333;
    margin: 1.5em 2em;
}

h1.cover-title {
    font-size: 2.4em;
    text-align: center;
    color: #1A2B4A;
    margin-top: 2em;
    margin-bottom: 0.3em;
    font-weight: bold;
    letter-spacing: 0.04em;
}

h2.cover-subtitle {
    font-size: 1.4em;
    text-align: center;
    color: #D4AF37;
    font-style: italic;
    margin-top: 0;
    margin-bottom: 1.5em;
}

p.cover-author {
    font-size: 1.1em;
    text-align: center;
    color: #888888;
    margin-top: 2em;
}

hr.cover-rule {
    border: none;
    border-top: 2px solid #D4AF37;
    width: 50%;
    margin: 1.5em auto;
}

h1.chapter-title {
    font-size: 1.8em;
    text-align: center;
    color: #1A2B4A;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
    font-weight: bold;
}

hr.chapter-rule {
    border: none;
    border-top: 1px solid #D4AF37;
    width: 40%;
    margin: 0.8em auto 1.5em auto;
}

h2.subheading {
    font-size: 1.2em;
    color: #1A2B4A;
    margin-top: 1.4em;
    margin-bottom: 0.4em;
    font-weight: bold;
}

p.body-text {
    text-align: justify;
    margin-top: 0.3em;
    margin-bottom: 0.6em;
}

blockquote.pull-quote {
    border-left: 4px solid #D4AF37;
    background-color: #F0F4FF;
    padding: 0.8em 1.2em;
    margin: 1em 1.5em;
    font-style: italic;
    color: #1A2B4A;
    font-size: 1.05em;
}

li.bullet-item {
    margin-bottom: 0.4em;
}

ul.bullet-list {
    padding-left: 1.5em;
}

p.copyright {
    font-size: 0.85em;
    text-align: center;
    color: #666666;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
}

p.toc-heading {
    font-size: 1.6em;
    text-align: center;
    color: #1A2B4A;
    font-weight: bold;
    margin-bottom: 1em;
}

ul.toc-list {
    list-style: none;
    padding-left: 0;
}

ul.toc-list li {
    font-size: 1em;
    color: #333333;
    margin-bottom: 0.5em;
    border-bottom: 1px dotted #cccccc;
    padding-bottom: 0.4em;
}
"""


# ──────────────────────────────────────────────
# Helper: build one chapter's HTML body
# ──────────────────────────────────────────────
def _chapter_html(chapter: dict) -> str:
    lines = []
    lines.append(f'<h1 class="chapter-title">{_esc(chapter["title"])}</h1>')
    lines.append('<hr class="chapter-rule"/>')

    # Collect consecutive bullets into a <ul>
    pending_bullets = []

    def flush_bullets():
        if pending_bullets:
            lines.append('<ul class="bullet-list">')
            for b in pending_bullets:
                lines.append(f'  <li class="bullet-item">{_esc(b)}</li>')
            lines.append('</ul>')
            pending_bullets.clear()

    for elem_type, text in chapter["content"]:
        if elem_type == "bullet":
            pending_bullets.append(text)
        else:
            flush_bullets()
            if elem_type == "heading":
                lines.append(f'<h1 class="chapter-title">{_esc(text)}</h1>')
            elif elem_type == "subheading":
                lines.append(f'<h2 class="subheading">{_esc(text)}</h2>')
            elif elem_type == "body":
                lines.append(f'<p class="body-text">{_esc(text)}</p>')
            elif elem_type == "quote":
                lines.append(
                    f'<blockquote class="pull-quote">{_esc(text)}</blockquote>'
                )

    flush_bullets()
    return "\n".join(lines)


def _esc(text: str) -> str:
    """Minimal HTML escaping for body text."""
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
    )


def _make_epub_chapter(
    book: epub.EpubBook,
    chapter: dict,
    css_item: epub.EpubItem,
    file_name: str,
) -> epub.EpubHtml:
    """Create and register an EpubHtml item for one chapter."""
    body = _chapter_html(chapter)
    html_content = (
        f"<html><head>"
        f"<title>{_esc(chapter['title'])}</title>"
        f'<link rel="stylesheet" type="text/css" href="style/main.css"/>'
        f"</head><body>{body}</body></html>"
    )
    item = epub.EpubHtml(
        title=chapter["title"],
        file_name=file_name,
        lang="en",
        content=html_content,
    )
    item.add_link(href="style/main.css", rel="stylesheet", type="text/css")
    book.add_item(item)
    return item


# ──────────────────────────────────────────────
# Main builder
# ──────────────────────────────────────────────
def build_document(output_path: str) -> str:
    """Build the EPUB and save to *output_path*.

    Returns the absolute path to the generated file.
    """
    book = epub.EpubBook()

    # ── Metadata ──────────────────────────────
    book.set_identifier(
        BOOK_METADATA.get("isbn") or f"urn:uuid:{uuid.uuid4()}"
    )
    book.set_title(
        f"{BOOK_METADATA['title']}: {BOOK_METADATA['subtitle']}"
    )
    book.set_language(BOOK_METADATA["language"])
    book.add_author(BOOK_METADATA["author"])
    book.add_metadata("DC", "publisher", BOOK_METADATA["publisher"])
    book.add_metadata("DC", "rights", BOOK_METADATA["rights"])
    book.add_metadata("DC", "description", BOOK_METADATA["description"])
    for kw in BOOK_METADATA["keywords"]:
        book.add_metadata("DC", "subject", kw)

    # ── CSS ───────────────────────────────────
    css_item = epub.EpubItem(
        uid="style_main",
        file_name="style/main.css",
        media_type="text/css",
        content=EPUB_CSS.encode("utf-8"),
    )
    book.add_item(css_item)

    # ── Cover HTML page ───────────────────────
    cover_html = (
        f"<html><head>"
        f"<title>{_esc(BOOK_METADATA['title'])}</title>"
        f'<link rel="stylesheet" type="text/css" href="style/main.css"/>'
        f"</head><body>"
        f'<h1 class="cover-title">{_esc(BOOK_METADATA["title"].upper())}</h1>'
        f'<hr class="cover-rule"/>'
        f'<h2 class="cover-subtitle">{_esc(BOOK_METADATA["subtitle"])}</h2>'
        f'<hr class="cover-rule"/>'
        f'<p class="cover-author">by {_esc(BOOK_METADATA["author"])}</p>'
        f"</body></html>"
    )
    cover_item = epub.EpubHtml(
        title=BOOK_METADATA["title"],
        file_name="cover.xhtml",
        lang="en",
        content=cover_html,
    )
    cover_item.add_link(href="style/main.css", rel="stylesheet", type="text/css")
    book.add_item(cover_item)

    # ── Copyright page ────────────────────────
    copyright_html = (
        "<html><head><title>Copyright</title>"
        '<link rel="stylesheet" type="text/css" href="style/main.css"/>'
        "</head><body>"
        "<br/><br/><br/>"
        f'<p class="copyright"><strong>{_esc(BOOK_METADATA["title"])}: '
        f'{_esc(BOOK_METADATA["subtitle"])}</strong></p>'
        f'<p class="copyright">Copyright &#169; {_esc(BOOK_METADATA["year"])} '
        f'{_esc(BOOK_METADATA["author"])}</p>'
        '<p class="copyright">All rights reserved. No part of this publication '
        "may be reproduced, distributed, or transmitted in any form or by any "
        "means without the prior written permission of the author.</p>"
        f'<p class="copyright">Published by {_esc(BOOK_METADATA["publisher"])}</p>'
        "</body></html>"
    )
    copyright_item = epub.EpubHtml(
        title="Copyright",
        file_name="copyright.xhtml",
        lang="en",
        content=copyright_html,
    )
    copyright_item.add_link(href="style/main.css", rel="stylesheet", type="text/css")
    book.add_item(copyright_item)

    # ── Chapter items ─────────────────────────
    chapter_items = []
    for ch in CHAPTERS:
        file_name = f"chapter_{ch['number']:02d}.xhtml"
        item = _make_epub_chapter(book, ch, css_item, file_name)
        chapter_items.append(item)

    # ── Spine (reading order) ─────────────────
    book.spine = [cover_item, copyright_item] + chapter_items

    # ── NCX Table of Contents ─────────────────
    book.toc = tuple(
        epub.Link(item.file_name, item.title, f"ch{i}")
        for i, item in enumerate(chapter_items)
    )
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # ── Write file ────────────────────────────
    print(f"Building EPUB: {output_path} …")
    epub.write_epub(output_path, book)
    size_kb = os.path.getsize(output_path) / 1024
    abs_path = os.path.abspath(output_path)
    print(f"✅  EPUB generated successfully!")
    print(f"📄  File : {abs_path}")
    print(f"📦  Size : {size_kb:.1f} KB")
    return abs_path


# ──────────────────────────────────────────────
# CLI entry point
# ──────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Generate the Religion Weaponized eBook as an EPUB."
    )
    parser.add_argument(
        "--output", "-o",
        default="religion_weaponized.epub",
        help="Output EPUB filename (default: religion_weaponized.epub)",
    )
    args = parser.parse_args()
    build_document(args.output)


if __name__ == "__main__":
    main()
