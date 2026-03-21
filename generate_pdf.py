"""
generate_pdf.py
Generates a professional, print-ready PDF eBook for
"Religion Weaponized: The Dark Side of Faith" by Yash Sahu.

Usage:
    python generate_pdf.py                     # writes religion_weaponized.pdf
    python generate_pdf.py --output my_book.pdf
"""

import argparse
import os
import sys
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
)

from ebook_content import BOOK_METADATA, CHAPTERS

# ──────────────────────────────────────────────
# Colour palette  (Navy / Gold / White / Grey)
# ──────────────────────────────────────────────
NAVY = colors.HexColor("#1A2B4A")
DARK_NAVY = colors.HexColor("#0D1425")
GOLD = colors.HexColor("#D4AF37")
WHITE = colors.white
LIGHT_GRAY = colors.HexColor("#CCCCCC")
DARK_GRAY = colors.HexColor("#444444")
MID_GRAY = colors.HexColor("#888888")

# ──────────────────────────────────────────────
# Page size & margins
# ──────────────────────────────────────────────
PAGE_WIDTH, PAGE_HEIGHT = letter          # 8.5 × 11 in
LEFT_MARGIN = RIGHT_MARGIN = 1.0 * inch
TOP_MARGIN = BOTTOM_MARGIN = 1.0 * inch

BODY_WIDTH = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN
BODY_HEIGHT = PAGE_HEIGHT - TOP_MARGIN - BOTTOM_MARGIN


# ──────────────────────────────────────────────
# Style sheet
# ──────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    styles = {
        # ---------- COVER ----------
        "CoverTitle": ParagraphStyle(
            "CoverTitle",
            fontName="Helvetica-Bold",
            fontSize=40,
            leading=48,
            textColor=WHITE,
            alignment=TA_CENTER,
            spaceAfter=12,
        ),
        "CoverSubtitle": ParagraphStyle(
            "CoverSubtitle",
            fontName="Helvetica-Oblique",
            fontSize=22,
            leading=28,
            textColor=GOLD,
            alignment=TA_CENTER,
            spaceAfter=24,
        ),
        "CoverAuthor": ParagraphStyle(
            "CoverAuthor",
            fontName="Helvetica",
            fontSize=16,
            leading=20,
            textColor=LIGHT_GRAY,
            alignment=TA_CENTER,
            spaceAfter=8,
        ),
        # ---------- TOC ----------
        "TOCHeading": ParagraphStyle(
            "TOCHeading",
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=30,
            textColor=NAVY,
            alignment=TA_CENTER,
            spaceAfter=24,
        ),
        "TOCEntry": ParagraphStyle(
            "TOCEntry",
            fontName="Helvetica",
            fontSize=12,
            leading=18,
            textColor=DARK_GRAY,
            leftIndent=0,
            spaceAfter=6,
        ),
        # ---------- CHAPTER ----------
        "ChapterTitle": ParagraphStyle(
            "ChapterTitle",
            fontName="Helvetica-Bold",
            fontSize=28,
            leading=36,
            textColor=NAVY,
            alignment=TA_CENTER,
            spaceBefore=12,
            spaceAfter=24,
        ),
        "SubHeading": ParagraphStyle(
            "SubHeading",
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=20,
            textColor=NAVY,
            spaceBefore=14,
            spaceAfter=6,
        ),
        "Body": ParagraphStyle(
            "Body",
            fontName="Helvetica",
            fontSize=11,
            leading=17,
            textColor=DARK_GRAY,
            alignment=TA_JUSTIFY,
            spaceBefore=4,
            spaceAfter=8,
        ),
        "Quote": ParagraphStyle(
            "Quote",
            fontName="Helvetica-Oblique",
            fontSize=12,
            leading=18,
            textColor=NAVY,
            alignment=TA_CENTER,
            leftIndent=40,
            rightIndent=40,
            spaceBefore=12,
            spaceAfter=12,
            borderColor=GOLD,
            borderWidth=1,
            borderPadding=(8, 12, 8, 12),
            backColor=colors.HexColor("#F0F4FF"),
        ),
        "Bullet": ParagraphStyle(
            "Bullet",
            fontName="Helvetica",
            fontSize=11,
            leading=17,
            textColor=DARK_GRAY,
            leftIndent=20,
            bulletIndent=6,
            spaceBefore=2,
            spaceAfter=4,
        ),
        # ---------- FOOTER ----------
        "Footer": ParagraphStyle(
            "Footer",
            fontName="Helvetica",
            fontSize=8,
            textColor=MID_GRAY,
            alignment=TA_CENTER,
        ),
        # ---------- COPYRIGHT ----------
        "Copyright": ParagraphStyle(
            "Copyright",
            fontName="Helvetica",
            fontSize=9,
            leading=14,
            textColor=DARK_GRAY,
            alignment=TA_CENTER,
            spaceAfter=6,
        ),
    }
    return styles


# ──────────────────────────────────────────────
# Page callbacks (headers / footers)
# ──────────────────────────────────────────────
def cover_page_callback(canvas, doc):
    """Full-bleed navy cover background."""
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)

    # Gold horizontal rule at top
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(3)
    canvas.line(LEFT_MARGIN, PAGE_HEIGHT - 0.6 * inch,
                PAGE_WIDTH - RIGHT_MARGIN, PAGE_HEIGHT - 0.6 * inch)

    # Gold horizontal rule at bottom
    canvas.line(LEFT_MARGIN, 0.6 * inch,
                PAGE_WIDTH - RIGHT_MARGIN, 0.6 * inch)
    canvas.restoreState()


def inner_page_callback(canvas, doc):
    """Running footer on inner pages."""
    canvas.saveState()
    page_num = doc.page
    title = BOOK_METADATA["title"]
    footer_text = f"{title}  •  Page {page_num}"
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MID_GRAY)
    canvas.drawCentredString(PAGE_WIDTH / 2.0, 0.45 * inch, footer_text)

    # thin gold line above footer
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.5)
    canvas.line(LEFT_MARGIN, 0.6 * inch, PAGE_WIDTH - RIGHT_MARGIN, 0.6 * inch)
    canvas.restoreState()


# ──────────────────────────────────────────────
# Document builder
# ──────────────────────────────────────────────
def build_document(output_path: str) -> str:
    """Build the complete PDF and save to *output_path*.

    Returns the absolute path to the generated file.
    """
    styles = build_styles()

    # ── Frame / Template setup ─────────────────
    cover_frame = Frame(
        LEFT_MARGIN, BOTTOM_MARGIN,
        BODY_WIDTH, BODY_HEIGHT,
        id="cover_frame",
        showBoundary=0,
    )
    inner_frame = Frame(
        LEFT_MARGIN, BOTTOM_MARGIN + 0.3 * inch,   # leave room for footer
        BODY_WIDTH, BODY_HEIGHT - 0.3 * inch,
        id="inner_frame",
        showBoundary=0,
    )

    cover_template = PageTemplate(
        id="Cover",
        frames=[cover_frame],
        onPage=cover_page_callback,
    )
    inner_template = PageTemplate(
        id="Inner",
        frames=[inner_frame],
        onPage=inner_page_callback,
    )

    doc = BaseDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=LEFT_MARGIN,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN,
        title=BOOK_METADATA["title"] + " – " + BOOK_METADATA["subtitle"],
        author=BOOK_METADATA["author"],
        subject=BOOK_METADATA["description"],
        creator="religion-weaponized-ebook generator",
    )
    doc.addPageTemplates([cover_template, inner_template])

    story = []

    # ── Cover page ────────────────────────────
    story.append(NextPageTemplate("Cover"))
    story.append(Spacer(1, 2.2 * inch))
    story.append(Paragraph(BOOK_METADATA["title"].upper(), styles["CoverTitle"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph(BOOK_METADATA["subtitle"], styles["CoverSubtitle"]))
    story.append(Spacer(1, 0.5 * inch))
    # Decorative rule
    story.append(HRFlowable(
        width="60%",
        thickness=2,
        color=GOLD,
        spaceAfter=20,
        hAlign="CENTER",
    ))
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph(
        f"by {BOOK_METADATA['author']}", styles["CoverAuthor"]
    ))
    story.append(PageBreak())

    # ── Switch to inner template for all subsequent pages ─
    story.append(NextPageTemplate("Inner"))

    # ── Copyright page ────────────────────────
    story.append(Spacer(1, 3.0 * inch))
    story.append(Paragraph(
        f"<b>{BOOK_METADATA['title']}: {BOOK_METADATA['subtitle']}</b>",
        styles["Copyright"],
    ))
    story.append(Paragraph(
        f"Copyright © {BOOK_METADATA['year']} {BOOK_METADATA['author']}",
        styles["Copyright"],
    ))
    story.append(Paragraph(
        "All rights reserved. No part of this publication may be reproduced, "
        "distributed, or transmitted in any form or by any means without the "
        "prior written permission of the author.",
        styles["Copyright"],
    ))
    story.append(Paragraph(
        f"Published by {BOOK_METADATA['publisher']}",
        styles["Copyright"],
    ))
    story.append(PageBreak())

    # ── Table of Contents ─────────────────────
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph("Table of Contents", styles["TOCHeading"]))
    story.append(HRFlowable(
        width="80%",
        thickness=1,
        color=GOLD,
        spaceAfter=16,
        hAlign="CENTER",
    ))

    toc_entries = [ch["title"] for ch in CHAPTERS]
    for entry in toc_entries:
        story.append(Paragraph(f"• &nbsp; {entry}", styles["TOCEntry"]))
    story.append(PageBreak())

    # ── Chapters ──────────────────────────────
    for chapter in CHAPTERS:
        story.append(Spacer(1, 0.4 * inch))
        story.append(Paragraph(chapter["title"], styles["ChapterTitle"]))
        story.append(HRFlowable(
            width="50%",
            thickness=1.5,
            color=GOLD,
            spaceAfter=14,
            hAlign="CENTER",
        ))

        for (elem_type, text) in chapter["content"]:
            if elem_type == "heading":
                story.append(Paragraph(text, styles["ChapterTitle"]))
            elif elem_type == "subheading":
                story.append(Paragraph(text, styles["SubHeading"]))
            elif elem_type == "body":
                story.append(Paragraph(text, styles["Body"]))
            elif elem_type == "quote":
                story.append(Spacer(1, 0.1 * inch))
                story.append(Paragraph(text, styles["Quote"]))
                story.append(Spacer(1, 0.1 * inch))
            elif elem_type == "bullet":
                story.append(Paragraph(f"• &nbsp; {text}", styles["Bullet"]))

        story.append(PageBreak())

    # ── Build ─────────────────────────────────
    print(f"Building PDF: {output_path} …")
    doc.build(story)
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    abs_path = os.path.abspath(output_path)
    print(f"✅  PDF generated successfully!")
    print(f"📄  File : {abs_path}")
    print(f"📦  Size : {size_mb:.2f} MB")
    print(f"📑  Pages: see file for total page count")
    return abs_path


# ──────────────────────────────────────────────
# CLI entry point
# ──────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Generate the Religion Weaponized eBook as a PDF."
    )
    parser.add_argument(
        "--output", "-o",
        default="religion_weaponized.pdf",
        help="Output PDF filename (default: religion_weaponized.pdf)",
    )
    args = parser.parse_args()
    build_document(args.output)


if __name__ == "__main__":
    main()
