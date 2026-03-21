# Religion Weaponized eBook

> **"Religion Weaponized: The Dark Side of Faith"** — by Yash Sahu  
> A fully generated, distribution-ready eBook available as both PDF and EPUB.

---

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate cover image + PDF + EPUB in one command
python build.py

# 3. Output files are written to the current directory:
#    religion_weaponized_cover.png  — book cover (1600×2560 px, 300 DPI)
#    religion_weaponized.pdf        — print-ready PDF (for KDP, direct sale)
#    religion_weaponized.epub       — eBook (for Apple Books, Google Play, Kobo)
```

You can also generate each format individually:

```bash
python book_cover_generator.py              # cover PNG only
python generate_pdf.py --output book.pdf    # PDF only
python generate_epub.py --output book.epub \
       --cover religion_weaponized_cover.png  # EPUB with embedded cover
```

To write all output to a specific folder:

```bash
python build.py --out-dir ./dist
```

---

## File Structure

| File | Purpose |
|---|---|
| `build.py` | **One-command builder** — runs cover → PDF → EPUB in sequence |
| `ebook_content.py` | All book content (chapters, quotes, bullet lists) |
| `generate_pdf.py` | PDF generator (ReportLab) — cover page, ToC, styled chapters |
| `generate_epub.py` | EPUB generator (ebooklib) — embedded CSS, metadata, cover image |
| `book_cover_generator.py` | Cover PNG generator (Pillow) — 1600×2560 px, 300 DPI |
| `main.py` | Google Cloud Function stub (HTTP endpoint) |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Container build — Python 3.11 with DejaVu fonts |
| `PUBLISHING_GUIDE.md` | Step-by-step guide for Amazon KDP, Apple Books, Google Play, Kobo |
| `GOOGLE_CLOUD_DEPLOYMENT.md` | Deploy the cover-generator Cloud Function |

---

## Book Contents

| # | Chapter |
|---|---|
| 0 | Introduction |
| 1 | The Weaponization of Faith |
| 2 | Historical Patterns of Religious Control |
| 3 | Modern Religious Manipulation Tactics |
| 4 | Recognizing Religious Abuse |
| 5 | The Psychology of Cult Behavior |
| 6 | Healing from Religious Trauma |
| 7 | Reclaiming Spirituality |
| 8 | Conclusion |
| 9 | Resources & Further Reading |

---

## Where to Sell

| Platform | Format | Guide |
|---|---|---|
| Amazon KDP | PDF / EPUB | [kdp.amazon.com](https://kdp.amazon.com) |
| Apple Books | EPUB | [authors.apple.com](https://authors.apple.com) |
| Google Play Books | EPUB / PDF | [play.google.com/books/publish](https://play.google.com/books/publish) |
| Kobo Writing Life | EPUB | [kobowritinglife.com](https://kobowritinglife.com) |
| Smashwords | EPUB | [smashwords.com](https://www.smashwords.com) |
| Draft2Digital | EPUB | [draft2digital.com](https://www.draft2digital.com) |
| Gumroad (direct) | PDF / EPUB | [gumroad.com](https://gumroad.com) |

See [PUBLISHING_GUIDE.md](PUBLISHING_GUIDE.md) for detailed platform-by-platform instructions.

---

## Requirements

- Python 3.9+
- Dependencies: `Pillow`, `reportlab`, `ebooklib`, `MarkupSafe`

```bash
pip install -r requirements.txt
```

---

## Docker

```bash
docker build -t religion-weaponized-ebook .
docker run --rm -v "$(pwd)/dist:/app/dist" religion-weaponized-ebook \
    python build.py --out-dir /app/dist
```

---

## Resources for Survivors

- [Recovery from Religion Foundation](https://recoveringfromreligion.org)
- [Cult Education Institute](https://culteducation.com)
- [SNAP — Survivors Network](https://snapnetwork.org)
- Crisis Text Line: Text **HOME** to **741741**
- National Domestic Violence Hotline (US): **1-800-799-7233**

---

*For additional information, consult [PUBLISHING_GUIDE.md](PUBLISHING_GUIDE.md) or contact the project maintainers.*