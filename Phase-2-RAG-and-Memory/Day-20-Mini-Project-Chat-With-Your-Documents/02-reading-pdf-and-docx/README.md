# 02 · Reading PDF & DOCX

Most real documents aren't `.txt`. Resumes, reports and textbooks are **PDF** or **Word
(`.docx`)**. You **cannot** `.decode()` these — they are compressed, structured binary
formats. You need a library that knows the format and hands you back the words.

| File type | Library        | The one call you need                         |
|-----------|----------------|-----------------------------------------------|
| `.txt`    | *(none)*       | `open(...).read()` (module 01)                |
| `.pdf`    | `pypdf`        | `PdfReader(f).pages[i].extract_text()`        |
| `.docx`   | `python-docx`  | `Document(f).paragraphs[i].text`              |

Install them (once):

```bash
pip install pypdf python-docx
```

> Note the import names differ from the pip names: `pip install python-docx` but `import docx`.

## PDF — `pypdf`

A PDF is a list of **pages**. You extract text page by page and join them:

```python
from pypdf import PdfReader

reader = PdfReader("resume.pdf")
text = "\n".join(page.extract_text() or "" for page in reader.pages)
```

⚠️ **The scanned-PDF trap.** If a PDF is a *photo* of a page (a scan), there is no text inside
it — only an image. `extract_text()` returns `""`. That's not a bug; it's why our app checks
for empty text and warns the user instead of silently indexing nothing. (Reading text from an
image needs OCR, which is a separate topic.)

## DOCX — `python-docx`

A Word document is a list of **paragraphs**. Read their `.text`:

```python
from docx import Document

doc = Document("resume.docx")
text = "\n".join(p.text for p in doc.paragraphs)
```

## The takeaway for Day 20

Different file types, but the **same goal**: `file -> one big string of text`. In the project
we hide all three behind a single function, `load_text(file)`, so the rest of the app never has
to care whether the upload was a PDF, a DOCX or a TXT. That "hide the messy details behind one
clean function" idea is exactly what **modules** are for — the next lesson.

## Run it

```bash
python read_docx.py     # creates a sample .docx, then reads it back
python read_pdf.py      # creates a sample .pdf,  then reads it back
```

Both scripts fabricate their own sample file so they run with no setup. (Fabricating the file
uses extra library calls — ignore those; the part you'll reuse is the short *reading* section
at the top of each `main()`.)

➡ Next: [03 · Python Modules & Project Structure](../03-python-modules/README.md)
