"""
Day 20 - Step 2b: Read text out of a PDF with pypdf.

Install once:
    pip install pypdf

Run it:
    python read_pdf.py

The reusable part is read_pdf() - three lines. The make_sample_pdf() helper below
hand-builds a tiny valid PDF only so the demo needs no setup; you will never write
a PDF by hand in real code, so skip past it.
"""

from pathlib import Path

# pypdf reads existing PDFs. PdfReader is the only thing we need from it.
from pypdf import PdfReader

SAMPLE = Path(__file__).resolve().parent / "sample_doc.pdf"


# ---------------------------------------------------------------------------
# THE PART YOU REUSE: get text out of a PDF.
# ---------------------------------------------------------------------------
def read_pdf(path) -> str:
    """A PDF is a list of pages. Extract each page's text and join them."""
    reader = PdfReader(path)
    # extract_text() can return None for a page with no text (e.g. a scan), so we
    # fall back to "" to keep join() happy. Empty result => probably a scanned PDF.
    return "\n".join((page.extract_text() or "") for page in reader.pages)


# ---------------------------------------------------------------------------
# Setup-only helper: fabricate a minimal PDF so the demo is self-contained.
# You do NOT need to understand this to use pypdf - it just writes a valid file.
# ---------------------------------------------------------------------------
def make_sample_pdf(path, lines) -> None:
    # Build the page's text-drawing commands (PDF's tiny drawing language).
    ops = b"BT /F1 16 Tf 72 720 Td 20 TL "
    for line in lines:
        safe = line.replace("(", r"\(").replace(")", r"\)")
        ops += ("(" + safe + ") Tj T* ").encode("latin-1")
    ops += b"ET"
    # A PDF is a set of numbered objects: catalog, pages, one page, a font, content.
    objects = [
        b"<</Type/Catalog/Pages 2 0 R>>",
        b"<</Type/Pages/Kids[3 0 R]/Count 1>>",
        b"<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]"
        b"/Resources<</Font<</F1 4 0 R>>>>/Contents 5 0 R>>",
        b"<</Type/Font/Subtype/Type1/BaseFont/Helvetica>>",
        b"<</Length " + str(len(ops)).encode() + b">>stream\n" + ops + b"\nendstream",
    ]
    out = b"%PDF-1.4\n"
    offsets = []
    for number, body in enumerate(objects, start=1):
        offsets.append(len(out))
        out += str(number).encode() + b" 0 obj" + body + b"endobj\n"
    xref_pos = len(out)
    # The cross-reference table tells a reader the byte offset of every object.
    out += b"xref\n0 " + str(len(objects) + 1).encode() + b"\n0000000000 65535 f \n"
    for off in offsets:
        out += ("%010d 00000 n \n" % off).encode()
    out += (
        b"trailer<</Size " + str(len(objects) + 1).encode() + b"/Root 1 0 R>>\n"
        b"startxref\n" + str(xref_pos).encode() + b"\n%%EOF"
    )
    Path(path).write_bytes(out)


def main() -> None:
    make_sample_pdf(
        SAMPLE,
        ["Priya Sharma - B.Tech CSE 2026", "Skills: Python, Chroma, Streamlit.",
         "Built a RAG document chatbot."],
    )

    print("=" * 72)
    print("Reading a .pdf file with pypdf")
    print("=" * 72)
    print(f"File: {SAMPLE.name}\n")

    text = read_pdf(SAMPLE)
    print("Extracted text:")
    print(text)
    print(f"\n({len(text)} characters extracted)")

    # Show the scanned-PDF check the real app relies on.
    if not text.strip():
        print("\n[!] No text found - this looks like a scanned/image PDF.")


if __name__ == "__main__":
    main()
