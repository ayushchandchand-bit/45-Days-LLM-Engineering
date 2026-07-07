# `docchat/` — the mini-project, built as a real package

This folder **is** the app. It's split into small modules so each file has one job
and stays readable — the lesson-03 idea, applied for real.

## The files (one responsibility each)

| File              | Job                                                        | Reuses      |
|-------------------|------------------------------------------------------------|-------------|
| `config.py`       | All settings in one place: models, temperature, chunk size, prompt | — |
| `file_loader.py`  | Uploaded file (PDF/DOCX/TXT) → plain text                  | lessons 01–02 |
| `chunker.py`      | Long text → small overlapping chunks                       | —           |
| `vector_store.py` | Embed chunks, store in Chroma, retrieve best matches       | Days 17–18  |
| `rag.py`          | Retrieved chunks + question → the grounded `messages` prompt| Day 16 memory |
| `llm.py`          | Talk to Groq: build client, stream the answer              | Day 19      |
| `app.py`          | Streamlit UI + wiring (thin!)                              | Day 19      |

## The data flow (one clean arrow)

```
        upload                 file_loader        chunker           vector_store
  ┌──────────────┐   bytes   ┌───────────┐  text  ┌────────┐ chunks ┌─────────────┐
  │ PDF/DOCX/TXT │ ───────▶  │ load_text │ ─────▶ │ chunk  │ ─────▶ │ embed +     │
  └──────────────┘           └───────────┘        └────────┘        │ store       │
                                                                    └─────┬───────┘
                                                                          │ retrieve top-k
   screen ◀─ st.write_stream ─ llm.stream_answer ◀─ rag.build_messages ◀──┘
                                                     (question + chunks)
```

Read it as a sentence: **the upload is turned into text, split into chunks, embedded and
stored; each question retrieves the most relevant chunks, which are packed into a grounded
prompt and streamed back from Groq.**

## Why this is a *project*, not a script

- **`app.py` is short** because the hard parts live elsewhere. You can read the whole UI in one
  screen.
- **Each module is testable alone.** Every file has an `if __name__ == "__main__"` self-test —
  run `python vector_store.py` to test retrieval without touching the UI.
- **Change one thing in one place.** New model? Edit `config.py`. Different chunking? `chunker.py`.
  Nothing else needs to know.

## Imports: why plain names, not dots

Files here import each other by name (`from chunker import chunk_text`), not with a dot
(`from .chunker import ...`). That's because `streamlit run docchat/app.py` executes `app.py`
as a script and adds this folder to Python's import path, so siblings are found by name. (See
lesson 03 for the three import styles.)

## Run it

```bash
# from the Day-20 folder, with a .env holding GROQ_API_KEY:
streamlit run docchat/app.py
```

## Try it yourself

- Drop the temperature to 0 and ask the same question twice — near-identical answers.
- Ask something **not** in your docs — the bot should say it can't find it (that's the
  grounding prompt in `config.py` doing its job).
- Open **📚 Sources used** under an answer to see exactly which chunks were retrieved.

➡ Back to the [Day 20 overview](../README.md) · Next up: the [exercises](../exercises/README.md)
