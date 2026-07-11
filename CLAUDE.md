# CLAUDE.md

Guidance for Claude Code (and any AI assistant) working in this repository.

## What this repo is
Course code for **SSAI-101**, Softpro School of AI's **46-day AI Development Summer Training**
(LLM engineering + agentic AI). It is a *teaching* repo: code here is written to be **read and
learned from**, not just to run. Audience = students (pre-final/final-year B.Tech, BCA/MCA,
early-career) with only Python basics as a prerequisite.

- Full curriculum: [`COURSE-PLAN.md`](COURSE-PLAN.md)
- **Career track** (parallel 30-min/day "get hired" talks over slide decks): [`CAREER-PLAN.md`](CAREER-PLAN.md)
- Original syllabus: `docs/course-1-45day-summer-training.md (4).pdf` (text: `docs/_syllabus.txt`)
- Python-week source outline: `dump/python.txt`

## The Career Launchpad track (parallel to the code)
A separate **30-min daily talk** on getting hired / winning freelance work — thesis: **build content +
specialize**. Source of truth: [`CAREER-PLAN.md`](CAREER-PLAN.md) (45-day arc, 5 themes). Each day's
deck lives **inside that day's code folder** as `career-talk/index.html` (+ `README.md` speaker notes).
Decks are self-contained branded HTML (reuse the Day-1 career deck as the shared template); ~10–14
slides ≈ 30 min. Days 1–2 are committed; Days 3–7 are drafted locally. Keep `CAREER-PLAN.md` and the
per-day decks in sync.

**Structure:** 46 days · 3 hrs/day · 4 phases · 3 mini-projects + 1 capstone, all deployed free.
(Day 16 — CLI chatbot — was inserted into Phase 2, shifting every later day +1; the course is now 46
days. The repo **folder** is still named `45-Days-LLM-Engineering` and the **career track** in
`CAREER-PLAN.md` is still a 45-day arc — both left as-is for now.)

## Repository layout
```
45-Days-LLM-Engineering/
├── README.md                  Master roadmap
├── COURSE-PLAN.md             Full day-by-day plan (source of truth for what each day covers)
├── CLAUDE.md                  This file
├── requirements.txt           Grows as the AI track begins (Day 8+)
├── docs/                      Syllabus & reference
├── Phase-1-Foundations/       Days 1–15
├── Phase-2-RAG-and-Memory/    Days 16–26
├── Phase-3-Agents-and-Tools/  Days 27–38
└── Phase-4-Capstone/          Days 39–46
```

Days 1–7 are a Python power-up; the AI track starts Day 8. Phase day-ranges are fixed in
`COURSE-PLAN.md` — keep all READMEs consistent with it.

## Per-day structure (follow this pattern exactly)
```
Phase-X-Name/Day-NN-Topic-In-Kebab-Case/
├── README.md                  Learning objectives + module index table + how-to-run + today's exercise
├── 01-first-concept/
│   ├── README.md              Teaching notes: explain the idea, tables, gotchas, "➡ Next" link
│   └── concept.py             Runnable, heavily-commented example(s)
├── 02-next-concept/
│   └── ...
└── exercises/
    ├── README.md              Problem statements (link to solutions)
    ├── name.py                Starter/stub for students (with TODOs)
    └── name_solution.py       Worked solution
```

### Conventions
- **Day folders:** `Day-NN-Title-In-Kebab-Case` (zero-padded number, e.g. `Day-01-...`, `Day-12-...`).
- **Module folders:** `NN-concept-name` (zero-padded, kebab-case): `01-variables`, `02-functions`.
- **Python files:** `snake_case.py`. Solutions end in `_solution.py`; student stubs use `# TODO`.
- **Every `.py` is independently runnable** from its own folder: `python file.py`. No hidden setup.
- Each `.py` starts with a docstring saying what it shows and the exact run command.
- READMEs are GitHub-markdown: use tables for comparisons, fenced code blocks, and a
  `➡ Next: [..](../..)` link at the bottom of each module.

## Teaching style
- **Comment the "why," show the "what" by example.** Prefer many small, focused scripts over one
  large file.
- Introduce one concept per module. If a concept needs a forward reference (e.g. f-strings before
  Day 2), note it briefly and move on.
- Use realistic, India-context examples where natural (₹ amounts, local scenarios) — matches the
  cohort.
- Reuse the course's own exercises where they exist (Magic Trick, BMI Calculator, Rock-Paper-
  Scissors, Todo List, etc. — see `dump/python.txt`).
- **Free-tier first, multi-provider.** In the AI track: default to **Groq** (genuinely free tier;
  Day 9 onward uses `groq` + `llama-3.1-8b-instant`), also show Ollama / Hugging Face / Gemini. For
  **embeddings** (Day 16+), default to local `sentence-transformers`; Gemini embeddings are optional.
  Never write localhost-only or paid-API-only code.

## Running code (Windows environment)
- **Use the real CPython for running scripts and pip:**
  `C:\Users\Pc\AppData\Local\Programs\Python\Python314\python.exe`
  ⚠️ The bare `python` on PATH is a hermes venv **without pip** — don't use it for installs.
- **`sentence-transformers` + CPU `torch` are installed globally** into this Python314 (Day 17+).
  PyTorch needs the **Microsoft VC++ 2015–2022 x64 Redistributable** — without it `import torch`
  fails with `WinError 1114` (`c10.dll` can't load `vcruntime140_1.dll`). It's now installed.
- Verify new example scripts actually run before considering a day "done".
- Shell is PowerShell; the Bash tool is also available.

## When adding a new day
1. Read that day's row in `COURSE-PLAN.md` for scope.
2. Create `Day-NN-Topic/` with a day `README.md` (objectives + module table).
3. Break the topic into numbered modules, each with a teaching `README.md` + runnable `.py`.
4. Add an `exercises/` folder with at least one stub + solution.
5. Run every script to confirm it works.
6. Add any new dependencies to the root `requirements.txt`.
7. Keep cross-links and phase READMEs consistent.

## Status
- ✅ Repo scaffold, `README.md`, `COURSE-PLAN.md`, phase folders.
- ✅ **Day 1** complete and verified (8 modules + 3 exercises).
- ✅ **Day 2** complete and verified (8 modules + 3 exercises: Strings, f-strings & methods).
- ✅ **Career Launchpad** plan (`CAREER-PLAN.md`) + **Days 1–2 career decks** committed; Days 3–7 decks drafted locally (not yet committed).
- ✅ **Day 2 trainer's guide** (`TRAINERS-GUIDE.md`) — full minute-by-minute session script.
- ✅ **Day 3** complete and verified (7 modules + 3 exercises: Booleans, conditionals & logical operators) + trainer's guide.
- ✅ **Day 4** complete and verified (6 modules + 3 exercises: Loops — while/for/range/break-continue/nested/loop-patterns).
- ✅ **Day 5** complete and verified (7 modules + 3 exercises: Functions & scope — def/params/return/defaults+keyword/LEGB/global/args-kwargs).
- ✅ **Day 5 Logic Building Challenge** (`Day-05.../logic-building/`) — 5 think-first problems recapping Days 1–5 (FizzBuzz · reverse-number/palindrome via maths · primes · word stats · number pyramid), each with stub + verified `_solution.py`, plus `SOLUTIONS.md` (5-step walk-throughs) and a deck `index.html` (*How to Build Logic When You Code* — Understand→Example→Plan→Code→Test, on the method, not the answers) + `DECK-NOTES.md`.
- ✅ **Day 6** complete and verified (7 modules + 3 exercises: Data structures — lists/list-patterns/dicts/dict-iteration/tuples/sets/choosing).
- ✅ **Day 7** complete and verified (8 modules + 3 exercises: Errors, modules & OOP — error-types/try-except/imports/pip/classes/methods/inheritance/lambda-functions).
- ✅ **Day 7 Coding Challenge Day** (`Day-07.../coding-challenges/`) — 15 problems grouped by topic recapping Days 1–6 (Day1 hms/BMI · Day2 initials/palindrome/title-case · Day3 grade/leap-year · Day4 digit-sum/triangle/fibonacci · Day5 temp-convert/`*args`-stats · Day6 word-freq/set-compare/gradebook), each a `qNN_*.py` stub + verified `_solution.py`, plus a grouped `README.md` with approach hints (no SOLUTIONS.md).
- ✅ **Python power-up week (Days 1–7) is fully built and verified.** All example scripts print ASCII-only (₹/emoji in comments only) so they run under the Windows console codepage.
- ✅ **Day 8** complete (Python for AI — requests / async / dotenv / type hints / Pydantic; 5 modules + 2 exercises).
- ✅ **Day 9** complete (LLM fundamentals & first **Groq** call; 5 modules + 2 exercises). Provider switched Gemini→**Groq** course-wide (`groq` + `llama-3.1-8b-instant`); embeddings stay local/Gemini for Day 17. Folder: `Day-09-LLM-Fundamentals-First-Groq-Call`.
- ✅ **Day 10** complete (Prompt engineering I — system prompts / zero-shot / few-shot / chain-of-thought / anatomy-checklist; 5 modules + 2 exercises). All Groq, temperature 0; module 05 + checklist run offline. Folder: `Day-10-Prompt-Engineering-I`.
- ✅ **GitHub Basics mini-track** — a beginner 3-part visual deck woven into Days 4–6, each in a `github-basics/` folder (`index.html` + speaker-notes `README.md`): Day 4 *Why GitHub* (commit-timeline + local/remote SVGs) · Day 5 *Everyday Workflow* (add/commit/push staging SVG, `.gitignore`) · Day 6 *Branching & Collaboration* (branch-and-merge SVG, PRs). Same Softpro deck template as the career talks, with added `.cmd`/`.diagram` styles; explanations use inline SVG.
- ✅ **Day 16 — CLI Chatbot (conversation memory)** in `Phase-2-RAG-and-Memory/Day-16-CLI-Chatbot/` — **Groq**, free. 6 step modules (single-turn → chat-loop → no-memory demo → **appending-messages** (the core: keep a `messages` list, append every turn) → system-prompt → commands/save with `/reset` `/save` `/load` JSON) + `exercises/` (turn-counter, persona-picker; each stub + `_solution.py`). All 11 `.py` compile. Inserting it as Day 16 cascaded the plan **+1 → 46 days** (Phase 2 → 16–26, Phase 3 → 27–38, Phase 4 → 39–46) across `README.md`, `COURSE-PLAN.md`, and this file.
- ✅ **Day 17 — Embeddings Fundamentals** in `Phase-2-RAG-and-Memory/Day-17-Embeddings-Fundamentals/` — **local `sentence-transformers` (`all-MiniLM-L6-v2`, 384-dim)**, free/no-key default; **Gemini** shown as optional cloud. 5 modules (01 what-is-an-embedding: pure-Python 2-D toy + Euclidean distance, no libs → 02 first real embedding, shape/norm → 03 similar-vs-different: rank by meaning, "automobile"≈"car" with zero shared words → 04 cosine similarity by hand with numpy, cross-checked vs `util.cos_sim`, unit-vector→dot-product shortcut → 05 optional Gemini, fails gracefully with no key) + `exercises/` (semantic-search, odd-one-out; each stub + `_solution.py`). All runnable scripts verified (module 05 prints skip message without `GEMINI_API_KEY`). Sets up Day 18 (from-scratch semantic search).
- ✅ **Day 18 — Semantic Search From Scratch** in `Phase-2-RAG-and-Memory/Day-18-Semantic-Search-From-Scratch/` — **local `sentence-transformers` (`all-MiniLM-L6-v2`)** + numpy, free/no-key, no framework. Reuses Day 17's cosine. 5 modules (01 corpus-and-embed: embed a list once → `(N, 384)` matrix → 02 query-and-score: normalize rows, one matrix-vector multiply scores the whole corpus, no Python loop → 03 top-k-results: `argsort`/`argpartition` → ranked `(score, doc)` → 04 mini-search-engine: a `SemanticSearch` class with `.add()`/`.search()` (mirrors Chroma's add/query) + live input loop → 05 why-this-matters: offline recap — this is RAG's "R", where the hand-rolled version breaks (persistence / linear scan / metadata), why a vector DB) + `exercises/` (FAQ answer bot; search-your-notes with a confidence **threshold** → "no relevant note found"; each stub + `_solution.py`). All 9 `.py` verified with real CPython (refund match at 0.55 with no shared words; "bake bread" correctly rejected by cutoff). No new deps. Sets up Day 19 (Chroma).
- ✅ **Day 19 — Streamlit From Scratch** in `Phase-2-RAG-and-Memory/Day-19-Streamlit-From-Scratch/` — **`streamlit`** (installed into Python314; pulls in pandas/altair), `groq` + `python-dotenv` reused. Built for a trainer new to Streamlit: heavy teaching READMEs + a full minute-by-minute **`DELIVERY-GUIDE.md`** (3-hr session script, error cheat-sheet, timing table). 7 modules (01 hello-streamlit: `streamlit run` vs `python`, title/write, live reload → 02 text-and-data: write/markdown/code/`st.dataframe`(pandas)/metric/status boxes → 03 widgets: "a widget returns the user's value"; button is True only on its click's rerun → 04 layout: sidebar/columns/tabs/expander via `with` → 05 **session-state-and-rerun** (the core): whole-script rerun model, broken-vs-working counter, golden `if "k" not in st.session_state` pattern → 06 caching: `cache_data` (data) vs `cache_resource` (models/clients) → 07 groq-chat-app: `st.chat_input`/`st.chat_message`/`st.write_stream`, history in `st.session_state.messages`, cached client, `.env`+`st.stop()` guard) + `exercises/` (BMI web app — pure widgets; AI summarizer — mini Project 1, spinner+cached client; each stub + `_solution.py`). All 9 runnable `.py` verified with Streamlit's `AppTest` harness (no exceptions); used `width="stretch"` (not deprecated `use_container_width`). Root + local `requirements.txt` updated with `streamlit`. **Note:** the user chose Streamlit for Day 19 (Day 18's old "Next" pointed to pgvector); Day 18 README forward-links updated to match.
- ✅ **Day 20 — Mini-Project 1: Chat With Your Documents** in `Phase-2-RAG-and-Memory/Day-20-Mini-Project-Chat-With-Your-Documents/` — first shippable Streamlit app; RAG over uploaded files. Also the day that finally teaches **file handling** + **Python modules/project structure** (both new). **Part A** (small runnable concept scripts): 01 reading-files (`with open`, modes, encodings, bytes→text) → 02 reading-pdf-and-docx (`pypdf` + `python-docx`; scanned-PDF `""` trap; each script fabricates its own sample file — a hand-built minimal PDF with a correct xref table) → 03 python-modules (import your own file, `if __name__=="__main__"` finally explained, packages, why plain-name sibling imports under `streamlit run`). **Part B** the `docchat/` package, one job per file: `config.py` (models list/temp/chunk knobs/grounding prompt), `file_loader.py` (upload bytes→text via extension dispatch, uses `BytesIO`), `chunker.py` (word chunks w/ overlap), `vector_store.py` (Day-18 Chroma wrapped in a `VectorStore` class — **in-memory `EphemeralClient`** so "Clear documents" is trivial), `rag.py` (build grounded `messages` + numbered source citations), `llm.py` (Groq client + streaming, **no Streamlit** so it stays testable), `app.py` (thin Streamlit UI — sidebar model/temperature/max-tokens/k controls, multi-file uploader, `st.write_stream`, "Sources used" expander). New deps **`pypdf` + `python-docx`** added to root + local `requirements.txt`. `exercises/` (doc_stats: file-handling+chunking; mini_rag_cli: full pipeline minus UI, retrieval works with no key; each stub + `_solution.py`). All Part-A + module self-tests + both solutions verified with real CPython (semantic retrieval confirmed: "getting money back"→"Refunds…" 0.73 with no shared words); `app.py` verified via `AppTest` (clean in both no-key and keyed states). `.gitignore` added for generated samples. **Labeled Mini-Project 1, build-only** (deploy = separate/homework) per user. Updated `COURSE-PLAN.md` Day 19 (→Streamlit) + Day 20 (→this project) rows, which were stale "pgvector via Supabase" duplicates.
- ✅ **Day 21 — LangChain Fundamentals** in `Phase-3-Agents-and-Tools/Day-21-LangChain-Fundamentals/` — **first day of Phase 3** and the course's LangChain on-ramp. **Plan pivot (user):** skip the remaining Phase-2 RAG deep-dives (chunking/retrieval/re-ranking/LlamaIndex/Mini-project 2) and jump into the agent-frameworks track; Phase 2 now ends at Day 20, **Phase 3 starts at Day 21** (LangChain → LangGraph → agents). Uses **latest LangChain 1.x** (`langchain` 1.3.x, `langchain-groq` 1.1.x) on **Groq** (`llama-3.1-8b-instant`), free. 6 modules (01 why-langchain: raw Groq vs `ChatGroq`, message objects, one interface/any provider → 02 prompt-templates: `ChatPromptTemplate`, `{vars}`, `format_messages` offline → 03 lcel-chains **(the core)**: the `|` operator, `prompt \| model \| parser`, `StrOutputParser`, invoke/batch/stream; `LLMChain` called out as legacy → 04 output-parsers: `StrOutputParser` vs `with_structured_output(PydanticModel)` for typed output → 05 runnables: `RunnableLambda`/`Parallel`/`Passthrough`, incl. the classic RAG wiring built offline → 06 memory: `MessagesPlaceholder` + a manual history list; **`RunnableWithMessageHistory` avoided as deprecated**, forward-ref LangGraph) + `exercises/` (translator_chain — LCEL + `batch`; structured_extractor — `with_structured_output`; each stub + `_solution.py`). **Every script runs offline** (templates/`|` flow/schemas/memory-growth demoed with no key; live Groq call skipped gracefully) — all 8 runnable `.py` + 2 stubs verified with real CPython on Python 3.14. New deps `langchain` + `langchain-groq` added to root + local `requirements.txt`. Updated `COURSE-PLAN.md` (Phase 2 → 16–20, Phase 3 → 21–31 LangChain-first) + main `README.md` roadmap. Also built a **branded slide deck** `presentation/index.html` (16 slides, Softpro deck template reused from Day 17) — *LangChain: Intro, Chains & Agents*: problem→what-is→why→LCEL→prompts/parsers→memory→**agents (Think/Act/Observe ReAct loop)**→tools (`@tool`/`bind_tools`)→LangGraph→Phase-3 roadmap — with `presentation/README.md` speaker notes.
- ⏳ **Day 11** built but **held back** (still Gemini-based — needs Groq conversion to match the course switch); preserved with Days 12–15 in branch `backup/pre-rebase-day16`, not yet on remote.
- ⏳ Day 11 conversion + Days 12–15 to reconcile/push next.
- ⏳ Career decks Days 8–45 to follow; Days 4–7 trainer's guides optional (not yet written).
- Repo initialized (git).
