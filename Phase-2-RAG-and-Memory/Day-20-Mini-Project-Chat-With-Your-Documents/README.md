# Day 20 — Mini-Project 1: Chat With Your Documents

**Phase 2 · RAG & Memory.** Today the separate pieces from Days 16–19 become one real,
deployable app — and we learn the two things that turn *scripts* into a *project*: **reading
files** and **splitting code into modules**.

> **What you build:** a Streamlit web app where you upload PDF/DOCX/TXT files and chat with
> them. Questions are answered *from your documents* using RAG (embeddings + Chroma + Groq),
> with full control over the model, temperature, and answer length in the sidebar.

## Learning objectives
By the end of today you can:
- Read text from `.txt`, `.pdf`, and `.docx` files (file handling + `pypdf` / `python-docx`).
- Split a program into **modules** and import your own files — and explain `if __name__ == "__main__"`.
- Structure an AI app as a small **package** where each file has one job.
- Wire the full RAG pipeline end to end: **load → chunk → embed → store → retrieve → generate**.
- Give the user live control of the LLM (model picker, temperature, max tokens) from a UI.

## What this reuses (Phase 2 so far)
| From    | Idea used here                                    |
|---------|---------------------------------------------------|
| Day 16  | Conversation memory — a `messages` list           |
| Day 17  | Embeddings — `sentence-transformers` (`all-MiniLM-L6-v2`) |
| Day 18  | Chroma — store vectors, retrieve nearest chunks   |
| Day 19  | Streamlit — widgets, session state, caching, streaming chat |

## Module index

### Part A — two new concepts (small, runnable, isolated)
| # | Folder | You learn |
|---|--------|-----------|
| 01 | [`01-reading-files/`](01-reading-files/README.md) | `open`/`with`, modes, encodings, bytes → text |
| 02 | [`02-reading-pdf-and-docx/`](02-reading-pdf-and-docx/README.md) | Extract text from PDF (`pypdf`) and DOCX (`python-docx`) |
| 03 | [`03-python-modules/`](03-python-modules/README.md) | Import your own files; `__name__` guard; packages |

### Part B — the project, built as a real package
| Folder | What it is |
|--------|------------|
| [`docchat/`](docchat/README.md) | The full app: `config` · `file_loader` · `chunker` · `vector_store` · `rag` · `llm` · `app` |

### Exercises
| Folder | Practise |
|--------|----------|
| [`exercises/`](exercises/README.md) | Document Stats · Mini RAG in the terminal |

## How to run

**Setup (once).** Install deps with the real CPython (see repo `CLAUDE.md`):
```bash
pip install -r docchat/requirements.txt
```
Create a `.env` (in the folder you run from) with your free Groq key:
```
GROQ_API_KEY=your_key_here
```

**Part A — run the concept scripts directly:**
```bash
python 01-reading-files/read_text_file.py
python 02-reading-pdf-and-docx/read_docx.py
python 02-reading-pdf-and-docx/read_pdf.py
python 03-python-modules/main.py
```

**Part B — run the app:**
```bash
streamlit run docchat/app.py
```
Upload a PDF/DOCX/TXT, then ask questions. Open **📚 Sources used** under any answer to see
which chunks grounded it.

## Today's exercise
Do both exercises in [`exercises/`](exercises/README.md):
1. **Document Stats** — file handling + chunking in a small module.
2. **Mini RAG in the terminal** — the whole pipeline without the UI.

Then a **stretch**: add a `.md` loader to `docchat/file_loader.py`.

## The big idea
> A useful AI app isn't one clever function — it's a handful of small, honest pieces wired
> together: *get the text in, break it up, find the relevant bit, and let the model answer from
> it.* Today you built exactly that, and you can read every line.

➡ Next: **Day 21 — Chunking strategies** (fixed vs recursive vs semantic vs parent-document) —
we replace today's simple word-chunker with smarter ones.
