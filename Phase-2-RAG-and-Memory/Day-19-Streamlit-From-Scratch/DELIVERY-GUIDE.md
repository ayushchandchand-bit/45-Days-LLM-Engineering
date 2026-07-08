# Day 19 — Trainer's Delivery Guide (Streamlit From Scratch)

A minute-by-minute script for teaching this day, written for a trainer who is **also new to
Streamlit**. If you can read Python and run one command in a terminal, you can deliver this. Read
this once fully before class, then keep it open on a second screen.

**Session length:** ~3 hours (with two short breaks). **Format:** live-coding + students follow along.

---

## 0. Before the session (do this the night before)

1. **Install Streamlit** into the course Python:
   ```bash
   C:\Users\Pc\AppData\Local\Programs\Python\Python314\python.exe -m pip install streamlit
   ```
   (Also installs pandas, altair, etc. `groq` and `python-dotenv` you already have from Day 9/16.)
2. **Smoke-test it works** — from the Day 19 folder run:
   ```bash
   streamlit run 01-hello-streamlit/hello_app.py
   ```
   A browser tab should open at `http://localhost:8501`. Press **Ctrl + C** to stop.
3. **Put your Groq key in a `.env`** in the Day 19 folder for module 07:
   ```
   GROQ_API_KEY=your_key_here
   ```
4. Open two terminals: one for running the app, one free for typing. Keep the **terminal visible**
   next to the browser all day — module 05 depends on students seeing terminal output.
5. Zoom your editor and browser font up. This is a very visual day.

### The one sentence to repeat all day
> **"Every click reruns the whole script, top to bottom."**
Say it in module 01, prove it in module 05, and lean on it in module 07. If students remember only
one thing today, this is it.

---

## 1. Opening hook (10 min)

Don't start with slides. Start with a **reveal**.

- Say: *"For 18 days our AI lived in a black terminal. Today we give it a face — in about 40 lines
  of Python, no HTML, no JavaScript."*
- Run module 07 live **now**, at the very start (you set up the key last night):
  ```bash
  streamlit run 07-groq-chat-app/chat_app.py
  ```
- Type a question, let the answer **stream in**. Watch the room lean forward.
- Then say: *"By the end of today, you will have built this. Let's start from an empty file."*
- Stop the app (Ctrl + C). Now go to module 01.

This "show the destination first" opening is worth the 5 minutes — it gives every later concept a purpose.

---

## 2. Module 01 — Hello, Streamlit (20 min)

**Goal:** everyone gets *a* page on screen and learns the run command.

Live-code `hello_app.py` from scratch (don't just open the finished file — type it):
1. `import streamlit as st` — *"one import, always aliased `st`."*
2. `st.title("Hello, Streamlit")` — save.
3. In the terminal: `streamlit run hello_app.py`. Browser opens. **Big moment — let it land.**

**Teach the run command hard.** Write on the board:
```
streamlit run file.py     ✅  (starts the web server)
python file.py            ❌  ("missing ScriptRunContext" warning, nothing happens)
```
Deliberately run `python hello_app.py` once so they **see** the warning. Then never again.

**Demo live reload:** with the app running, add `st.write("edited live!")`, save, and show the
*"Source file changed → Rerun"* button top-right. Click "Always rerun". Students love this.

**First taste of reruns:** add the `st.button("Click me")` block. Click it, message appears. Say:
*"Notice — clicking re-ran the file. Park that thought, it's the big idea in an hour."*

> **Common errors:**
> - *"command not found: streamlit"* → they ran plain `python`/`pip` without Streamlit installed, or
>   used the wrong Python. Use the full Python314 path (see step 0).
> - *Port 8501 in use* → an old app is still running. Ctrl + C the old terminal, or
>   `streamlit run app.py --server.port 8502`.
> - Nothing opens → copy the `http://localhost:8501` URL from the terminal into the browser manually.

---

## 3. Module 02 — Text and Data (20 min)

**Goal:** they can put anything on a page.

- Live-code the top of `display_app.py`: `st.write`, `st.markdown`, `st.code`.
- Emphasise **`st.write` is the "when in doubt" function** — it renders strings, numbers, dicts, and
  tables automatically.
- Build the pandas DataFrame and `st.dataframe(df)`. Reassure them: *"You don't need pandas today — a
  DataFrame is just a table. It's installed with Streamlit."* Show the sortable columns.
- Show `st.metric` and the four status boxes (`success/info/warning/error`). Tell them: *"These
  colour boxes are how your app talks back to the user — we'll use them constantly."*

**Mini-task (3 min):** *"Add a row to the DataFrame with your own name and score, save, watch it
appear."* Gets everyone's hands on the keyboard.

---

## 4. Module 03 — Widgets (25 min)  ·  *then BREAK*

**Goal:** the mental model *"a widget returns the user's value."*

Write this on the board before touching code:
```python
name = st.text_input("Your name")   # `name` IS whatever they typed
age  = st.slider("Age", 0, 100, 25) # `age` IS the slider's number
```
Say it out loud: *"No onclick, no callbacks. The widget hands you a value; you use it below."*

- Build the "Tell me about yourself" section: `text_input`, `slider`, `selectbox`, `checkbox`, then
  the `st.write(f"Hi {name}...")` that uses them. Move the slider — the greeting updates. *"See? No
  button. Widgets already remember their value across reruns."*
- Build the **live tip calculator** — pure widgets, instant update. This surprises people who expect
  to need a "Calculate" button.
- Now the **button** section. This is where you seed module 05:
  ```python
  if st.button("Give me a cheer"):
      st.success("...")
  ```
  Click it — message shows. Click something else — message **vanishes**. Say: *"The button was only
  True for one rerun. Remember that phrase. Next module explains why, and how to make things stick."*

**Take the first break here (~10 min).** You're at roughly the 90-minute mark.

---

## 5. Module 04 — Layout & Sidebar (20 min)

**Goal:** apps that don't look like one long list.

- `st.sidebar.selectbox` / `st.sidebar.slider` — *"settings go on the left, content in the middle.
  Every AI app you build puts the model picker and temperature here."*
- `st.columns(3)` with three `st.metric`s in `with` blocks. Explain the `with column:` pattern once,
  carefully — they'll reuse it for tabs, expanders, and chat bubbles.
- `st.tabs([...])` and `st.expander(...)`. Frame the expander as *"where you hide the long system
  prompt or debug JSON so the screen stays clean."*
- Tie the sidebar checkbox to the debug JSON at the bottom — a real, useful pattern.

Keep this module brisk; it's intuitive once they have the `with` pattern.

---

## 6. Module 05 — Session State & Reruns (30 min)  ← **THE CORE. Do not rush.**

**Goal:** they deeply understand the rerun model and can use `session_state`.

**Step 1 — make reruns visible.** Open `state_app.py`. Point at the `print("SCRIPT RAN...")` line.
Run the app with the **terminal visible**. Click anything a few times. The terminal fills with
"SCRIPT RAN" lines. Say: *"That is the whole file executing again on every single click. Normal
variables are born and die on each run."*

**Step 2 — the broken counter.** Walk the left column line by line, out loud:
- `count = 0` runs **every** rerun → resets to 0.
- click → rerun → `count = 0` again → `+1` → `1`. Forever `1`.
Click it live: stuck on 1. Let them feel the "wait, that's dumb" moment. That confusion is the lesson.

**Step 3 — the fix.** Walk the right column:
```python
if "count" not in st.session_state:   # runs ONLY the first time
    st.session_state.count = 0
if st.button("Add one (working)"):
    st.session_state.count += 1
```
Click it: 1, 2, 3, 4. Say: *"`st.session_state` is a dictionary Streamlit does NOT wipe between
reruns. It's your app's memory."*

**Step 4 — name the golden pattern.** Write it big; tell them they'll type it in almost every app:
```python
if "thing" not in st.session_state:   # 1. init once
    st.session_state.thing = default
# 2. use / update st.session_state.thing freely; it persists
```
Show the `st.json(dict(st.session_state))` at the bottom so they *see* what's stored.

> **Why this matters (say it):** *"The chat app remembers your conversation using exactly this. No
> session_state = no memory = a goldfish bot. This one concept unlocks module 07."*

If you're short on time anywhere today, **steal it from other modules, not this one.**

**Second break (~5 min)** after this if the room needs it.

---

## 7. Module 06 — Caching (15 min)

**Goal:** *"the whole script reruns — so how do we not reload the model every click?"*

- Pose the fear: *"If the entire file reruns on every click, does my 90 MB model reload every click?
  By default — yes. That's unusable."*
- Run `caching_app.py`. Click **uncached** → 2-second wait every time. Click **cached** with the same
  number → slow once, then instant. Change the number → slow once more (new cache entry).
- The rule they must remember:
  - `@st.cache_data` → data (DataFrames, JSON, numbers).
  - `@st.cache_resource` → one shared live object (a **model**, a DB connection, an **API client**).
- Point at the code snippet in the app showing `@st.cache_resource` on the model loader. Say:
  *"You'll see this exact decorator on the Groq client in the next module."*

Don't over-explain caching internals. The 80/20 is: *models/clients → cache_resource; data →
cache_data.*

---

## 8. Module 07 — The Groq Chat App (30 min)  ← the payoff

**Goal:** build the thing from the opening hook, live.

Frame it: *"This is the Day 16 terminal chatbot with a face. Same `messages` list, same Groq call.
Three new ideas, all of which you already met."* Map them explicitly:
1. **Memory** → `st.session_state.messages` (module 05's golden pattern).
2. **Chat bubbles** → `st.chat_message("user"/"assistant")` with the `with` pattern (module 04).
3. **Input box** → `st.chat_input(...)`.

Build `chat_app.py` in this order, testing after each stage:
1. `@st.cache_resource def get_client()` + the no-key `st.error` / `st.stop()` guard. Run it with a
   *wrong* key removed to show the friendly error, then fix the `.env`.
2. The `if "messages" not in st.session_state` init.
3. The **redraw loop** over history in chat bubbles. Explain: *"We repaint the whole conversation
   every rerun — cheap, and it's why past messages stay on screen."*
4. `st.chat_input` → append user msg → call Groq → `st.write_stream` for the typewriter effect →
   append the reply. Send one message; watch it stream.

Then demo the **sidebar**: change the model, rewrite the system prompt (*"You are a pirate"*), hit
**Clear chat**. Now they see every module from today working together.

> **Streaming trouble?** If `st.write_stream` misbehaves in your environment, fall back to
> non-streaming — replace the streaming block with:
> ```python
> resp = client.chat.completions.create(model=model, messages=messages_to_send, temperature=0.4)
> reply = resp.choices[0].message.content
> st.write(reply)
> ```
> Everything else stays the same. Don't lose the room debugging streaming live.

---

## 9. Exercises & wrap (15 min)

- Point them at `exercises/`: **BMI web app** (pure widgets — everyone should finish this) and the
  **AI summarizer** (mini Project 1 — for the faster students).
- Recap the arc on the board: *page → content → widgets → layout → **reruns/state** → caching → chat.*
- The closing line: *"Your AI is no longer a terminal toy. It's a link you can send a friend. That's
  what makes Project 1 real — and Streamlit is how we'll deploy it for free."*

---

## Quick error cheat-sheet (keep visible)

| Symptom | Cause | Fix |
|---------|-------|-----|
| `missing ScriptRunContext` warning | ran `python app.py` | use `streamlit run app.py` |
| `command not found: streamlit` | not installed / wrong Python | `python -m pip install streamlit` (full Python314 path) |
| Port 8501 already in use | old app still running | Ctrl + C it, or `--server.port 8502` |
| Counter stuck at 1 | plain variable, not session_state | use the golden `session_state` pattern |
| Model reloads every click / slow | no caching | `@st.cache_resource` on the loader |
| Chat forgets previous turns | history not in session_state | store messages in `st.session_state.messages` |
| `No GROQ_API_KEY` error | missing `.env` | create `.env` with the key, restart the app |
| Edit didn't show | didn't rerun | click "Rerun" (top-right) or set "Always rerun" |

## Timing summary
| Segment | Mins |
|---------|-----:|
| Opening hook (run the finished chat app) | 10 |
| 01 Hello | 20 |
| 02 Text & data | 20 |
| 03 Widgets → break | 25 |
| 04 Layout | 20 |
| 05 **Session state & reruns** | 30 |
| 06 Caching | 15 |
| 07 Chat app | 30 |
| Exercises & wrap | 15 |
| **Total (excl. breaks)** | **~185** |
