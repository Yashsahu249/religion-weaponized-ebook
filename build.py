"""
build.py
One-command eBook builder.

Runs the three generation steps in order:
  1. Book cover image  → religion_weaponized_cover.png  (via book_cover_generator)
  2. PDF               → religion_weaponized.pdf         (via generate_pdf)
  3. EPUB              → religion_weaponized.epub        (via generate_epub, with cover embedded)

Usage:
    python build.py                        # writes all three files in current directory
    python build.py --out-dir ./dist       # writes to a specific output folder
"""

import argparse
import os
import sys
import time


def run_step(label: str, fn, *args, **kwargs):
    """Run *fn* with timing and a clear console banner."""
    print()
    print("=" * 60)
    print(f"  {label}")
    print("=" * 60)
    start = time.monotonic()
    result = fn(*args, **kwargs)
    elapsed = time.monotonic() - start
    print(f"  ⏱  Completed in {elapsed:.1f}s")
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Build the Religion Weaponized eBook (cover + PDF + EPUB)."
    )
    parser.add_argument(
        "--out-dir", "-d",
        default=".",
        help="Directory to write output files (default: current directory)",
    )
    args = parser.parse_args()

    out_dir = os.path.abspath(args.out_dir)
    os.makedirs(out_dir, exist_ok=True)

    cover_path = os.path.join(out_dir, "religion_weaponized_cover.png")
    pdf_path = os.path.join(out_dir, "religion_weaponized.pdf")
    epub_path = os.path.join(out_dir, "religion_weaponized.epub")

    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║   Religion Weaponized — eBook Build Pipeline         ║")
    print("╚══════════════════════════════════════════════════════╝")
    print(f"  Output directory: {out_dir}")

    # ── Step 1: Cover image ───────────────────
    from book_cover_generator import create_book_cover
    run_step("Step 1/3 — Generating book cover image", create_book_cover, cover_path)

    # ── Step 2: PDF ───────────────────────────
    from generate_pdf import build_document as build_pdf
    run_step("Step 2/3 — Generating PDF", build_pdf, pdf_path)

    # ── Step 3: EPUB (with embedded cover) ────
    from generate_epub import build_document as build_epub
    run_step(
        "Step 3/3 — Generating EPUB",
        build_epub,
        epub_path,
        cover_image_path=cover_path,
    )

    # ── Summary ───────────────────────────────
    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║   ✅  Build complete — all files ready to sell!      ║")
    print("╚══════════════════════════════════════════════════════╝")
    files = [
        ("Cover (PNG)", cover_path),
        ("PDF",         pdf_path),
        ("EPUB",        epub_path),
    ]
    for label, path in files:
        size = os.path.getsize(path)
        size_str = f"{size / (1024*1024):.2f} MB" if size > 1024*1024 else f"{size / 1024:.1f} KB"
        print(f"  📄  {label:<14} {size_str:<10}  {path}")
    print()
    print("Next steps:")
    print("  • Upload the PDF to Amazon KDP (print / Kindle Direct Publishing)")
    print("  • Upload the EPUB to Apple Books, Google Play Books, or Kobo")
    print("  • Use the PNG cover when listing on any platform")
    print()


if __name__ == "__main__":
    main()
