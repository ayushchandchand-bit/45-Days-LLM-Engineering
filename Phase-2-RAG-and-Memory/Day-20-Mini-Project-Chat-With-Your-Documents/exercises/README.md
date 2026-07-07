# Day 20 · Exercises

Two terminal exercises that drill today's new skills — **file handling**, **modules**, and the
**RAG pipeline** — without needing the web UI. Each has a stub (with `# TODO`s) and a worked
`_solution.py`.

Run everything with the real CPython (see the repo `CLAUDE.md`):

```
C:\Users\Pc\AppData\Local\Programs\Python\Python314\python.exe file.py
```

## 1 · Document Stats (`doc_stats.py`)
**Practises:** file handling (lessons 01–02) + chunking + writing a small module.

Write a program that takes a file (`.txt`, `.pdf`, or `.docx`), extracts its text, splits it
into chunks, and prints a small report:

```
File      : sample_notes.txt
Characters: 512
Words     : 88
Chunks    : 3   (size=60 words, overlap=10)
Longest word: embeddings
```

- Fill in `load_text()` to dispatch on the file extension (like `docchat/file_loader.py`).
- Fill in `chunk_words()` to make overlapping word-chunks (like `docchat/chunker.py`).
- The script creates its own `sample_notes.txt` so it runs with no setup.

➡ Solution: [`doc_stats_solution.py`](doc_stats_solution.py)

## 2 · Mini RAG in the terminal (`mini_rag_cli.py`)
**Practises:** the whole pipeline end-to-end — embed → store in Chroma → retrieve → (optionally)
answer with Groq — the app minus Streamlit.

Build a command-line "chat with a document":

1. Chunk a built-in document and embed the chunks into an in-memory Chroma collection.
2. For each question, retrieve the top-k chunks and print them with their similarity.
3. If a `GROQ_API_KEY` is set, also print a grounded answer; if not, just show the chunks
   (so the retrieval half works with **no key at all**).

- Fill in `build_index()` and `answer()`.
- The solution runs two demo questions, then drops into a `You:` loop (type `quit` to exit).

➡ Solution: [`mini_rag_cli_solution.py`](mini_rag_cli_solution.py)

## Stretch goals (modify the real app in `docchat/`)
The app already demonstrates these — try rebuilding them yourself:
- A **"Clear documents"** button (see the sidebar in `app.py`).
- A **"Sources used"** expander under each answer (already there — turn it off, then re-add it).
- Add a **`.md` loader** to `file_loader.py` (hint: treat it like `.txt`).
- Add a **word/character counter** to the sidebar using `store.count()`.

➡ Back to the [Day 20 overview](../README.md)
