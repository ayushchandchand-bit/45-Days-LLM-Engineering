# Day 20 — Trainer's Delivery Guide (3-hour session)

Minute-by-minute script for teaching **Mini-Project 1: Chat With Your Documents**. This is a
*build day*: the win is that students leave with a running app they understand line by line.

**One-line story for the day:** "You've learned the pieces — Streamlit, embeddings, Chroma,
Groq. Today we bolt them together into one app, and pick up the two skills real projects need:
reading files and splitting code into modules."

## Before class (5-min setup check)
- [ ] `pip install -r docchat/requirements.txt` works with the real CPython.
- [ ] A `.env` with a valid `GROQ_API_KEY` sits in the Day-20 folder.
- [ ] `streamlit run docchat/app.py` opens and shows the uploader.
- [ ] Have 1–2 sample files ready to upload (a short PDF resume + a `.txt` of notes).
- [ ] First run downloads the embedding model (~90 MB) — do it **before** class on the room's wifi.

## Timing at a glance
| Block | Time | Topic |
|------:|------|-------|
| 0 | 0:00–0:10 | Demo the finished app first (the "wow") |
| 1 | 0:10–0:35 | Part A · file handling (lessons 01–02) |
| 2 | 0:35–1:00 | Part A · modules & structure (lesson 03) |
| — | 1:00–1:10 | Break |
| 3 | 1:10–1:35 | Tour the `docchat/` package — the map |
| 4 | 1:35–2:10 | Read the pipeline modules together (file_loader → llm) |
| 5 | 2:10–2:35 | Read & run `app.py`; demo model/temperature controls |
| 6 | 2:35–3:00 | Independent work: exercises + stretch, doubt-solving |

---

## Block 0 — Demo first (0:00–0:10)
Run the app. Upload a resume PDF. Ask: *"What are this person's top skills?"* Then ask something
**not** in the file — show it says *"I couldn't find that in your documents."* Open **📚 Sources
used**. Say: *"By the end of today this is yours, and you'll understand every line. Let's build up
to it."* Don't explain the code yet — just create the want.

## Block 1 — File handling (0:10–0:35)
**Why:** every app so far invented its data. Real apps read files.
- Live-code `read_text_file.py` ideas: `with open(...)`, why `with`, `encoding="utf-8"`.
- Hammer the **`"w"` truncates** warning — this bites everyone once.
- Run `read_docx.py` and `read_pdf.py`. Land the key line only: `PdfReader(f).pages[i].extract_text()`.
- **The scanned-PDF trap:** show that a scan returns `""`. This is *why* the app warns instead of
  indexing nothing. (Great real-world "gotcha" moment.)
- Bytes vs text: an upload is **bytes**; `.decode("utf-8")` makes it text. Foreshadow the uploader.

## Block 2 — Modules & structure (0:35–1:00)
**Why:** we're about to write 7 files, not 1. This is the day's conceptual leap.
- Open `03-python-modules/`. Run `python text_utils.py` (self-test prints) then `python main.py`
  (self-test does **not** print). Ask the class *why*. Reveal `if __name__ == "__main__"`.
- Give the one-sentence definition: **"A module is just a `.py` file you can import."**
- Show the one-big-file vs modules table. Anchor the rule: **one file = one job, named for the job.**
- Mention the three import styles but tell them we'll use plain names — and exactly why
  (`streamlit run` puts the script's folder on the path).

### Break (1:00–1:10)

## Block 3 — The package map (1:10–1:35)
Open `docchat/README.md`. Walk the **file table** and the **data-flow diagram** out loud, as one
sentence: *upload → text → chunks → embed+store → retrieve → grounded prompt → answer.* Do **not**
read code yet — give them the map before the streets. Ask them to predict which file does each job.

## Block 4 — Read the pipeline (1:35–2:10)
Open the files in pipeline order; read the comments, run each self-test:
1. `config.py` — "every knob in one place." Point out the models list + the grounding prompt.
2. `file_loader.py` — dispatch by extension; `python file_loader.py`.
3. `chunker.py` — run it; **show the overlap** in the printed chunks (w8 w9 w10 repeat).
4. `vector_store.py` — this is Day 18. Run it: "getting money back" finds "Refunds…" with **no
   shared words**. That's semantic retrieval — the heart of RAG.
5. `rag.py` — run it; show the assembled prompt. "This fused context+question message *is* RAG."
6. `llm.py` — streaming generator; note it has **no Streamlit** so it stays testable.

## Block 5 — The UI & controls (2:10–2:35)
Open `app.py`. Emphasise **how short it is** — payoff of modules. Trace the 5 numbered steps in the
chat handler (store question → retrieve → build messages → stream → save). Then live-demo the
**sidebar**: change the model, push temperature to 0 vs 1 and re-ask, drop `k` to 1. Let them feel
the control. Show **Clear documents**.

## Block 6 — Independent work (2:35–3:00)
Point them at `exercises/`:
- **Document Stats** (file handling + chunking) — everyone should finish this.
- **Mini RAG in the terminal** — the whole pipeline, no UI; great confidence-builder.
- Stretch: add a `.md` loader to `file_loader.py`.
Circulate. Common help below.

---

## Error cheat-sheet (what will actually go wrong)
| Symptom | Cause | Fix |
|---------|-------|-----|
| `No GROQ_API_KEY found` in the app | no `.env` / wrong folder | put `.env` in the folder you run `streamlit` from |
| `ModuleNotFoundError: docx` | installed `docx`, not `python-docx` | `pip install python-docx` (import is `docx`) |
| `ModuleNotFoundError: config` when running app | ran from wrong place | run `streamlit run docchat/app.py` from the Day-20 folder |
| PDF indexes 0 chunks / "No readable text" | scanned/image PDF | expected — use a text PDF; OCR is out of scope |
| `import torch` → `WinError 1114` | missing VC++ redist | install MS VC++ 2015–2022 x64 (see repo `CLAUDE.md`) |
| App feels slow on first question | embedding model loading | it's cached after the first load; warm it before class |
| Answers ignore the document | temperature high / bad chunking | drop temperature; raise `k`; check the Sources expander |
| Two people, one machine, weird state | `session_state` is per-session | it's fine — each browser tab is independent |

## Talking points to land
- **"Retrieval finds meaning, not keywords."** The refund demo (no shared words) is the money moment.
- **"Grounding is a prompt, not magic."** Show the line in `config.py` that forbids outside answers.
- **"Short `app.py` = good structure."** The whole UI fits on one screen because the work is elsewhere.
- **"This is Project 1 — you'll deploy it soon."** Set up the deploy day / homework.

## If you're ahead / behind
- **Behind:** skip reading `llm.py` and `rag.py` line-by-line; just run their self-tests and move to
  the app demo. The *experience* of the working app matters most.
- **Ahead:** have them add the `.md` loader live, or wire a "download chat as .txt" button
  (file handling, full circle).
