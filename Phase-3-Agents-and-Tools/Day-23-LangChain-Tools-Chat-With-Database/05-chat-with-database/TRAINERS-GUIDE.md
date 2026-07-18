# 🎤 Trainer's Guide — Building "Chat With Your Database" (Day 23, Module 05)

A minute-by-minute script for **building the text-to-SQL agent live** with the class, file by
file, using the [`starter-kit/`](starter-kit/). Covers exactly what to *say*, what to *type*,
what to *ask*, the *gotchas* to stage on purpose, and what to cut if you run behind.

> **Where this sits in the day:** modules 01–04 (why-tools → `@tool` → `bind_tools` →
> the tool-calling loop) come first. This project is the payoff — students have seen every
> piece; today they assemble them into something that feels like magic. Budget **~110 min**.
>
> **The one sentence of the session:** *"You type English; the model inspects the schema,
> writes SQL, runs it through OUR tools, reads the rows, and answers in words — and we're
> going to build that loop by hand."*

---

## 0. Before the session (10-min pre-flight)

- [ ] Use the **real CPython**: `C:\Users\Pc\AppData\Local\Programs\Python\Python314\python.exe`
      (the bare `python` on PATH is a venv without pip — see repo `CLAUDE.md`).
- [ ] `pip install langchain langchain-groq streamlit python-dotenv` — confirm imports work.
- [ ] In **your** copy of the finished folder: `python build_sample_db.py`, then run
      `python agent.py` once **with** your Groq key in `.env` — confirm real answers come back.
      (Groq free tier can hiccup; know before class, not during.)
- [ ] Also run `python agent.py` once **without** a key (rename `.env` briefly) — confirm the
      offline stand-in prints *"There are 15 customers from Pune."* That's your no-internet backup.
- [ ] `streamlit run app.py` once; leave the browser tab ready for the opening demo.
- [ ] Students: everyone has the `starter-kit/` folder open, deps installed, and has run
      `python build_sample_db.py`. A Groq key is **optional until step 4** — say that up front
      so nobody stalls on signup.
- [ ] Projector: terminal + editor at ≥18pt. Two visible windows: editor left, terminal right.
- [ ] ⚠️ Never project your `.env`. Keep it out of the editor's open tabs.

## Session map (~110 min)

| Block | Time | What |
|-------|:----:|------|
| 1. Demo the finished thing | 10 min | Run the answer key app, one question, open "How I got this" |
| 2. The data + the safe layer | 15 min | `build_sample_db.py` + read-walk `db.py` (given, not written) |
| 3. Write `tools.py` | 20 min | The three `@tool` wrappers; docstrings are the API |
| 4. Write `agent.py` ⭐ | 30 min | The tool-calling loop — the heart of the day |
| 5. Write `cli.py` | 10 min | Terminal chat; mostly a victory lap |
| 6. Write `app.py` | 15 min | Streamlit handler + the "How I got this" expander |
| 7. Break it on purpose + wrap | 10 min | Safety demos, where this goes (Day 24/25) |

*Running behind? See the **Triage** box at the end.*

---

## 1. Demo first — sell the destination (10 min)

Don't explain anything yet. From your **finished** copy: `streamlit run app.py`.

- Type: **"Which city has the most customers?"** Let the answer land.
- Then the money move: **open the "How I got this (tool calls)" expander.** Walk it slowly:
  *"It called `list_tables`. Then `describe_table`. Then it WROTE this SQL itself and ran it.
  Nobody typed that query — the model did."*
- Point at the sidebar schema: *"and it can only read. Watch me try to make it delete
  something later — it can't."* (Plant that; you pay it off in block 7.)
- **Say:** *"Everything you just saw is six small files, and four of them you're writing in
  the next 90 minutes. The loop inside is the module-04 loop — nothing new, just pointed at
  a real database."*
- Close the app. Everyone switches to `starter-kit/`.

**Ask (frame the whole build):** *"What are the three things the model needs to answer that
question?"* → what tables exist, what columns they have, a way to run SQL. *"That's exactly
our three tools."*

---

## 2. The data + the safe layer (15 min) — `build_sample_db.py` + `db.py` (both given)

These two are **plumbing** — read them together, don't type them.

### `build_sample_db.py` (5 min)
- Everyone runs `python build_sample_db.py`. It creates `store.db`.
- **Two things to point at:** `random.seed(42)` — *"fixed seed = everyone in this room has
  byte-identical data, so when the agent says 15 customers from Pune, it's 15 for all of us."*
  And the four linked tables (customers → orders → order_items → products): ~3,700 rows.
- **Say:** *"Enough data that you can't eyeball the answers. The agent has to actually query."*

### `db.py` — read-walk, don't skim (10 min)
- **Frame:** *"This file knows the database and NOTHING about the LLM. That split is the
  architecture of the whole project: data layer, brain, UI — each testable alone."*
- Walk the three functions: `list_tables` / `get_schema` / `run_query`. One job each.
- **🔑 The safety slide of the day — two locks, in order:**
  1. `mode=ro` in `_connect` — *"the connection itself is read-only; a write fails at the
     driver, below our code."*
  2. `_is_safe_select` — single statement, must start with `SELECT`/`WITH`, no `;`-stacking,
     banned write keywords. *"Belt AND braces — never trust one layer when a model writes SQL."*
- **Everyone runs `python db.py`.** Success = tables print, top-3 products print, and the
  `DELETE FROM customers` at the bottom prints `rejected ->`. *"Note the rejection is a normal
  printed message, not a crash. Hold that thought — it becomes important in tools.py."*
- Mention `MAX_ROWS = 50`: *"a careless `SELECT *` on 2,700 rows would flood the model's
  context. Caps like this are how you keep agents cheap and sane."*
- **Check:** *"If the model sends `SELECT 1; DROP TABLE customers`, which lock catches it?"*
  → `_is_safe_select` (the `;` check) — and even if it didn't, `mode=ro` would.

---

## 3. Write `tools.py` (20 min) — TODOs 1–4

Open `starter-kit/tools.py`. **Everyone types with you.** This is a code-along, not a lecture.

- **Frame:** *"db.py speaks Python. The model speaks tool-calls. tools.py is the adapter —
  three thin wrappers, and the real content is the DOCSTRINGS."*

### TODO 1 — `list_tables` (5 min)
```python
@tool
def list_tables() -> str:
    """List all tables in the database. Call this FIRST to see what data exists."""
    return ", ".join(db.list_tables())
```
- **🔑 Recap from module 02, say it again anyway:** name from the function name, description
  from the **docstring**, args from the type hints. *"The docstring is not a comment. It is
  the instruction the model reads to decide when to call this. 'Call this FIRST' is us
  programming the model's behaviour — in English, in a docstring."*
- Why `", ".join(...)`? Tools return **text** to the model, not Python lists.

### TODO 2 — `describe_table` (5 min)
```python
@tool
def describe_table(table_name: str) -> str:
    """
    Show the columns and their types for one table. Call this BEFORE writing SQL
    so you use real column names. Pass a single table name from list_tables.
    """
    try:
        return db.get_schema(table_name)
    except db.DatabaseError as e:
        return str(e)
```
- **⭐ The idea of this file — errors become feedback:** *"We catch the error and RETURN it
  as text. If the model asks for a table that doesn't exist, it gets back 'No such table:
  … Tables are: customers, orders…' — reads it, corrects itself, next loop. If we let it
  raise, the program dies and the model learns nothing."*

### TODO 3 — `run_sql_query` (4 min)
- Same pattern as TODO 2, wrapping `db.run_query`. Docstring must say: single read-only
  SELECT only, and *check the schema with describe_table first*. Let them write this one
  mostly alone — it's the same shape.

### TODO 4 — `TOOLS` + `TOOL_MAP` (2 min)
```python
TOOLS = [list_tables, describe_table, run_sql_query]
TOOL_MAP = {t.name: t for t in TOOLS}
```
- *"The list is what we bind to the model; the map is how the loop finds a tool by the NAME
  the model asked for."* Both consumed in the next file.

### Test (4 min) — `python tools.py`
- Success = three real results **and** the broken query (`SELECT * FROM nope`) comes back as
  readable text, not a traceback.
- **⚠️ Common student errors here:**
  - `list_tables.invoke()` → TypeError. Tools take a **dict**: `.invoke({})`,
    `.invoke({"table_name": "products"})`. *"That dict is the model's calling convention."*
  - Forgot `@tool` on one function → `AttributeError: 'function' object has no attribute
    'invoke'` (or `.name` fails in `TOOL_MAP`).
  - Docstring missing → `@tool` raises at import time. Good — the description is mandatory
    *because the model can't use a tool it can't read about*.
- **Check:** *"Who decides which of these three runs, and when?"* → **The model.** We only
  decide what's on the menu. (Callback to module 03.)

---

## 4. Write `agent.py` ⭐ (30 min) — the tool-calling loop

The headline. Slow down; this is the 30 minutes the day exists for.

- **Frame with the given parts first (5 min), don't jump to the TODO:**
  - `SYSTEM_PROMPT` — read it aloud. *"Steps 1–4 in the prompt are the same workflow we wrote
    into the tool docstrings. Prompt and docstrings pulling in the same direction — that's
    deliberate."* Also: *"never invent column names; if a query errors, read it and retry" —
    that line is why error-as-text works.*
  - `build_model()` — one line: `ChatGroq(...).bind_tools(TOOLS)`. Module 03, verbatim.
  - `MAX_STEPS = 8` — *"a confused model must never loop forever. Every agent you ever build
    gets a cap. Every one."*
  - `OfflineDBModel` — *"NOT an AI. A stand-in that replays a fixed 3-tool script, so your
    loop can be tested with no key and no internet. The loop doesn't know the difference —
    which proves the loop is the thing that matters."*

### The loop itself (15 min) — live-code `answer_question`, narrating each line
```python
for _ in range(MAX_STEPS):
    ai = model.invoke(messages)
    messages.append(ai)

    if not ai.tool_calls:              # no tool requested -> final answer
        return ai.content

    for call in ai.tool_calls:         # run every tool the model asked for
        result = TOOL_MAP[call["name"]].invoke(call["args"])
        if verbose:
            print(f"   -> {call['name']}({call['args']})")
        if on_tool:
            on_tool(call["name"], call["args"], str(result))
        messages.append(ToolMessage(content=str(result),
                                    tool_call_id=call["id"]))
```
(Delete the `raise NotImplementedError` line; keep the "(Stopped after too many steps…)"
return under the loop.)

- **Narrate the shape, not just the syntax:** *"Ask the model. If it answered in words —
  done. If it asked for tools — run them, append the results, go around again. That `for`
  with an `if…return` in the middle IS the agent. Everything else today is packaging."*
- **🔑 Three lines to dwell on:**
  - `messages.append(ai)` — *"the model's own request goes into the history too. Forget this
    and the model has amnesia about what it just asked for"* (and the API rejects the orphan
    ToolMessage).
  - `tool_call_id=call["id"]` — *"the receipt. The model may ask for several tools at once;
    the id ties each result to the request it answers. Wrong or missing id = a 400 error
    from the API."*
  - `str(result)` — message content must be text.
- **Ask before running:** *"Why is `return ai.content` INSIDE the loop and the 'stopped'
  message after it?"* → normal exit is the model choosing to answer; falling out the bottom
  means we hit the cap.

### Test (10 min)
- **First with NO key** (everyone can do this): `python agent.py` →
  ```
  Q: How many customers are from Pune?
     -> list_tables({})
     -> describe_table({'table_name': 'customers'})
     -> run_sql_query({'query': "SELECT COUNT(*) FROM customers WHERE city='Pune'"})
  A: There are 15 customers from Pune. (Offline stand-in: ...)
  ```
  *"YOUR loop just drove a 3-tool sequence. The stand-in scripted the choices, but the
  plumbing — invoke, dispatch, ToolMessage, repeat — is all yours."*
- **Then with your key on the projector:** the three demo questions. Point at the printed
  tool calls: the real model often takes a *different* route than the stand-in (it may skip
  `list_tables`, or query twice). *"That's the difference between a script and an agent —
  it chooses."*
- **⚠️ Debug table for the room** (TA floats):

  | Symptom | Cause |
  |---|---|
  | `NotImplementedError` | Forgot to delete the placeholder `raise` |
  | Answer is `None` / blank | Returned `ai` instead of `ai.content` |
  | 400 error mentioning tool messages | Missing `messages.append(ai)` or wrong/missing `tool_call_id` |
  | Loop always hits "(Stopped after too many steps)" | `if not ai.tool_calls` check missing/inverted, so it never returns |
  | `KeyError` in `TOOL_MAP` | TODO 4 in tools.py incomplete, or tool renamed |

---

## 5. Write `cli.py` (10 min) — the victory lap

- **Frame:** *"The brain is done and tested. Notice how small the UIs are now — THAT is why
  we kept Streamlit and the LLM out of agent.py."*
- The stub is a standard input loop (Day 16 shape): banner → no-key branch runs one offline
  demo → else `build_model()` once **outside** the loop, then
  `input` → `answer_question(model, question, verbose=True)` → print, with `quit` to exit.
- **⚠️ Gotcha:** building the model *inside* the `while` works but re-creates it every turn —
  ask *"what's wrong with putting `build_model()` in the loop?"* and let them spot it.
- Keyed students chat with their own DB for a few minutes. Collect one fun question and run
  it on the projector. `verbose=True` means the whole room sees the tool trail every time.

---

## 6. Write `app.py` (15 min) — Streamlit + "How I got this"

- **Frame:** *"Same brain, third interface. Everything here is Day 19/22 muscle memory except
  ONE new trick: the `on_tool` callback."*
- Walk the given scaffolding fast (guards for missing `store.db` and missing key, sidebar
  schema from `db.py`, `@st.cache_resource` model, history in `st.session_state`, replay on
  rerun). Ask *"why cache_resource and not cache_data?"* → it's a client/model object (Day 19).
- **The new part — live-code the handler:**
  ```python
  steps = []   # on_tool fills this so we can show the agent's work
  answer = answer_question(model, question, verbose=False,
                           on_tool=lambda n, a, r: steps.append((n, a, r)))
  ```
  *"In the CLI we printed tool calls; a web app can't print. So agent.py fires a callback per
  tool call and stays UI-free — the UI decides what a 'step' looks like. Same trick every
  real framework uses for streaming agent traces."* Then the expander that renders `steps`,
  and append `{"role": "assistant", "content": answer, "steps": steps}` to history.
- `streamlit run app.py` → re-ask the block-1 opening question. Full circle: **the demo from
  minute one is now their code.**
- **⚠️ Common snags:** ran with `python app.py` instead of `streamlit run` (Day 19 flashback);
  `.env` not in *this* folder; port 8501 busy → `streamlit run app.py --server.port 8502`.

---

## 7. Break it on purpose + wrap (10 min)

Pay off the safety promise from block 1 — on the projector, in the finished app:

1. **Ask the agent to destroy data:** *"Please delete all customers from Mumbai."* Open
   "How I got this": if it even attempts SQL, the tool returns *"Only a single read-only
   SELECT statement is allowed."* — and the model apologises and explains. *"The guard didn't
   crash. It answered the model, and the model coped. Layered defence: prompt says don't,
   validator refuses, driver can't."*
2. **Watch self-correction:** ask something that tempts a wrong column (e.g. *"total revenue
   from delivered orders"* — revenue lives in `order_items`, not `orders`). Odds are good
   you'll see a SQL error → corrected retry in the trace. If it works first try, say so —
   *"temperature 0 and good docstrings; you got lucky AND you engineered your luck."*
3. **Recap the architecture in one breath:** data layer (no LLM) → tools (adapter, errors as
   text) → agent (the loop, no UI) → two thin UIs. *"Each file testable alone; three of the
   six ran before anyone had a key."*
4. **The forward hook — say this verbatim:** *"You hand-wrote a `while` loop with a step cap.
   Tomorrow, LangGraph gives that loop a proper engine — state, branching, memory. And on
   Day 25, `create_agent` builds EVERYTHING you wrote today in one line. You'll know exactly
   what that one line is doing — because you built it."*
5. Point at [`exercises/`](../exercises/README.md) (weather_tool + count_rows — both offline)
   as homework; bootcamp rules apply (plan first, 20-min struggle, hints one rung at a time).

---

## Error cheat-sheet (whole session)

| Error / symptom | Fix |
|---|---|
| `store.db not found` | Run `python build_sample_db.py` in the **starter-kit** folder |
| `ModuleNotFoundError: langchain_groq` | Wrong Python — use the full Python314 path (repo `CLAUDE.md`) |
| `groq.AuthenticationError` / 401 | Key typo in `.env`, or `.env` in the wrong folder (must sit next to the script) |
| 429 / rate limit from Groq | Free tier burst — wait ~30 s; fall back to the offline stand-in to keep teaching |
| Tool call trace shows the same failing query repeatedly until "(Stopped…)" | Fine! That's `MAX_STEPS` doing its job — use it as a teaching moment |
| `st.session_state` has no attribute `messages` | The `if "messages" not in st.session_state` guard was skipped (Day 19 module 05) |

## Triage — running behind?

- **Cut first:** block 5 (`cli.py`). Show yours for 2 minutes; the concept adds nothing new.
- **Cut second:** the `app.py` code-along → walk the finished `../app.py` instead, focusing
  only on the `on_tool` lambda + expander (5 min).
- **Never cut:** writing the `agent.py` loop by hand (block 4), the no-key offline test, and
  wrap point 4 (the Day 24/25 hook). If students leave with only one artefact, it's that loop.
- **No internet / Groq down:** the entire build still works to the end of block 4 offline.
  Do blocks 1–4, demo 5–6 from your machine with cached screenshots if needed, and lean
  harder on the offline stand-in — *"the loop is the lesson; the model is a plug-in."*

➡ Back to the [project overview](README.md) · [Starter kit](starter-kit/README.md) · [Day overview](../README.md)
