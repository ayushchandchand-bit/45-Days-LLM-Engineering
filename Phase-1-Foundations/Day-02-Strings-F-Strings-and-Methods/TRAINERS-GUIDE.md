# 🎤 Trainer's Guide — Day 02: Strings, f-strings & String Methods

A minute-by-minute script you can follow live. Covers the full session: the 30-min **career talk**,
the technical modules (with exactly what to *say*, what to *type*, what to *ask*, and the *gotchas*
to pre-empt), the independent exercises, and the wrap-up.

> **Audience reminder:** complete beginners (Day 2). They learned numbers/variables/`print()`
> yesterday. Strings are the data type they'll use most with LLMs — sell that early.

---

## 0. Before the session (5-min pre-flight)
- [ ] Projector mirrored; font size **large** (terminal + editor at ≥18pt).
- [ ] A terminal open in the Day-02 folder; `python` REPL ready to launch.
- [ ] Editor open on `Phase-1-Foundations/Day-02-Strings-F-Strings-and-Methods/`.
- [ ] Run one script once to confirm Python works: `python 01-strings/strings.py`.
- [ ] Use the **real CPython** for running: `C:\Users\PC\AppData\Local\Programs\Python\Python312\python.exe`.
- [ ] Open the career deck `career-talk/index.html` in a browser, press **F** (fullscreen), clicker paired.
- [ ] ⚠️ **Windows console can't print `₹`** — scripts use `Rs` on purpose. If a student types `₹` in
      a `print()` and hits `UnicodeEncodeError`, that's the teachable moment (see Module 06).

## Session map (3 hrs 30 min)

| Block | Time | What |
|-------|:----:|------|
| Career talk | 30 min | Deck: *The AI Job & Freelance Market (2026)* |
| Concept + live coding | 75 min | Modules 01–06 (strings → f-strings) |
| Guided code-along | 45 min | Modules 07–08 (methods + chaining) |
| Independent work | 45 min | The 3 exercises |
| Standup + wrap-up | 15 min | Recap, blockers, preview Day 3 |

*Running behind? See the **Triage** box at the very end for what to cut safely.*

---

## 1. Career talk — 30 min
Deck: [`career-talk/index.html`](career-talk/) · full notes in [`career-talk/README.md`](career-talk/README.md).

- Present the 11 slides (~28 min) and collect today's **Career Action** ask aloud:
  *"Find 5 real job/freelance posts you'd want, note the skills each asks for."*
- **Bridge into code (1 line):** *"Every one of those posts wants Python. Every LLM prompt and every
  model reply is a **string**. So today we master text — the data type AI runs on."*

---

## 2. Concept + live coding — 75 min (Modules 01–06)
Teach from the REPL where you can. **Type live, make a mistake on purpose, let them predict outputs.**

### 🔥 Cold open (2 min)
In the REPL, type and ask "what will this print?" *before* hitting Enter each time:
```python
>>> "AI" + " " + "Engineer"
>>> "ha" * 3
>>> "Python"[::-1]
```
The reversed-string trick gets a reaction — promise "you'll know how that works in 30 minutes."

### Module 01 — Strings (10 min) · `01-strings/`
- **One message:** text goes in quotes; `+` joins, `*` repeats.
- **Type live:** quotes-inside-quotes (`"it's"` vs `'She said "hi"'`). Ask: *"why pick one over the other?"*
- **⚠️ Gotcha to stage on purpose:** `"Age: " + 25` → `TypeError`. Let them see the error, then fix with
  `str(25)`. Say: *"remember this pain — f-strings (in 40 min) make it vanish."*
- **Check:** "Give me a string that contains both a single and double quote." (Answer: use `\` escapes — teases Module 04.)

### Module 02 — Indexing (10 min) · `02-string-indexing/`
- Draw the index ruler on the board for `Hello`: `0 1 2 3 4` on top, `-5…-1` underneath.
- **Type live:** `word[0]`, `word[-1]`, then `word[10]` → `IndexError` (expected, not scary).
- **Two anchors:** negative indexing counts from the end; **strings are immutable** — show `word[0]="J"`
  fails, then rebuild with `"J" + word[1:]`.
- Mention `None` briefly ("a deliberate nothing") — don't dwell; it returns on Day 5.
- **Check:** "How do I always get the last character, even if I don't know the length?" → `[-1]`.

### Module 03 — Slices (12 min) · `03-string-slices/`
- **The #1 confusion:** `start` included, `stop` **excluded**. Say it twice. `"Python"[0:3]` → `'Pyt'`.
- **Type live progressively:** `[2:5]` → `[:3]` → `[3:]` → `[-3:]` → `[::2]` → `[::-1]`.
- Pay off the cold open: `[::-1]` reverses. Explain step = -1 walks backwards.
- **⚠️ Gotcha:** slices **don't** raise on over-range (`[0:100]` is fine) — unlike indexing. Contrast the two.
- **Check (do as a room):** "Slice `"Python"` to get `'tho'`." → `[2:5]`.

### Module 04 — Escape & triple quotes (10 min) · `04-escape-and-triple-quotes/`
- **Type live:** `print("Line1\nLine2")`, `\t`, `\"`. Then `\\`.
- **🪟 Windows hook:** `"C:\name"` secretly has `\n`! Show it, then fix with `\\` or `r"C:\Users"`.
- **Triple quotes = the LLM payoff.** Show the multi-line `prompt = """…"""`. Say: *"this is exactly how
  you'll write prompts to Groq in a few weeks."* Ties today's boring topic to the exciting goal.
- **Check:** "How do you write a 3-line string without typing `\n`?" → triple quotes.

### Module 05 — len / input / type casting (13 min) · `05-len-input-typecasting/`
- `len()` first (trivial). Then `input()` — **run the script live so it pauses**; type an answer to show it blocks.
- **The big idea:** `input()` **always returns a string.** Prove it: `type(input(...))` → `str`.
- **Stage the classic bug:** read an age with `input()`, then `age + 1` → `TypeError` (string + int).
  Fix with `int()`. *This is the single most common beginner bug — make it memorable.*
- **⚠️ Gotcha:** `int("3.5")` → `ValueError` (the dot). Use `float()` for decimals.
- **Check:** "Why does `input()` give a string even when I type 25?" (so you must cast before maths.)

### Module 06 — f-strings (20 min) · `06-f-strings/`  ⭐ *the headline skill of the day*
- Callback to Module 01's `+`/`str()` pain. Then reveal: `f"You are {age} years old."` Audible relief.
- **Type live:** put an *expression* inside braces `f"{age + 1}"`, then a method `f"{name.upper()}"`.
- **Number formatting (the money skill):** build a tiny receipt live —
  `f"{price:.2f}"`, `f"{1000000:,}"`, `f"Rs {price:,.2f}"`, `f"{0.18:.0%}"`.
- **🪟 Teach the `₹` gotcha deliberately:** type `print(f"₹{price:.2f}")` and let it crash with
  `UnicodeEncodeError` on the Windows console. Explain: the *code* is fine, the *terminal* (cp1252)
  can't display `₹`. We print `Rs` to stay portable; the real fix is
  `import sys; sys.stdout.reconfigure(encoding="utf-8")`. (This exact gotcha shows up in their Shopping Cart exercise.)
- **Check:** "Format `2499.5` as `2,499.50`." → `f"{2499.5:,.2f}"`.

---

## 3. Guided code-along — 45 min (Modules 07–08)
Slow down. **Everyone types with you.** TA floats to unstick people. Pause after each method so they run it.

### Module 07 — String methods (25 min) · `07-string-methods/`
- **Frame methods:** "a function that belongs to a value — call it with a dot: `value.method()`."
- **🔑 The non-negotiable point:** strings are immutable, so methods **return a new string** — they
  don't change the original. Prove it: `text.upper()` then show `text` unchanged. *Students forget this constantly.*
- Code-along through `.upper/.lower/.title/.strip/.replace/.find/.count/.startswith`.
- **Teach them to fish:** run `help(str.replace)` in the REPL. Point to the docs link in the module README.
  Say: *"you will never memorise all of these — you look them up. That skill matters more than the list."*
- **Check:** "Will `name.upper()` change `name`? How do I keep the result?" → assign it: `loud = name.upper()`.

### Module 08 — Method chaining (20 min) · `08-method-chaining/`
- Show the verbose 3-step version, then the chained one: `messy.strip().upper().replace(" ", "_")`.
- Read it **left to right**: each method hands its result to the next.
- Real-world clean-up: `"  ALICE@Example.COM  ".strip().lower()`.
- **Taster only:** `.split(",")` → list, `.join()` → string. Say "lists arrive Day 6 — just meet them today."
- **Mini code-along challenge (if time):** clean `"  hELLo WORLD  "` into `"Hello World"`. → `.strip().title()`.

---

## 4. Independent work — 45 min (Exercises)
Point them to [`exercises/`](exercises/). Stubs have `# TODO`s; solutions are `*_solution.py`.
Tell them to **try the stub first**, peek at the solution only when stuck. Suggested order = easiest first.

| Order | Exercise | Skills | Watch for |
|------:|----------|--------|-----------|
| 1 | `age_calculator.py` | `input`, `int()`, f-string | forgetting `int()` → string+int error |
| 2 | `shopping_cart.py` | f-string `:,.2f`, `:.0%` | typing `₹` in `print` → crash; use `Rs` |
| 3 | `press_release.py` | strip/replace/title + chaining | not capturing the chained result |

**Live-verify a solution** to model good habits (note `age`/cart use input — pipe answers if demoing):
```bash
python exercises/shopping_cart_solution.py
python exercises/press_release_solution.py
printf "Riya\n2001\n" | python exercises/age_calculator_solution.py
```
**Stretch for fast finishers:** "make the Press Release also print how many characters were removed"
(`len(raw) - len(clean)`), or "reverse a user's name with `[::-1]`."

---

## 5. Standup + wrap-up — 15 min
- **Go around (1 line each):** "one thing that clicked, one thing still fuzzy." Note repeat fuzzies.
- **Recap the 3 keepers of the day:**
  1. **f-strings** are how you build text — `f"...{value}..."` with `:,.2f` for money.
  2. **Slicing** — `start` in, `stop` out; `[::-1]` reverses.
  3. **String methods return new strings** (immutability) — and you *look them up*, not memorise.
- **Career nudge:** remind them to actually do today's Career Action (5 target job posts).
- **Preview Day 3:** "Booleans & conditionals — making your programs *decide* (if/elif/else). Strings
  plug right in: `if name.lower() == "admin": …`."

---

## ❓ Anticipated student questions (quick answers)
- *"Single vs double quotes — which is right?"* Both identical; pick the one that avoids quotes inside your text.
- *"Why `4 / 2` floaty but strings are different?"* Different types — today's about `str`; numbers were Day 1.
- *"What's the difference between a function and a method?"* A method is a function attached to a value (`x.method()`); `len(x)` is a plain function.
- *"Can I change one letter in a string?"* No — immutable. Build a new string with slicing/replace.
- *"`find()` returned -1?"* That means "not found." It doesn't raise an error.
- *"Why did `₹` crash but `Rs` works?"* Terminal encoding (Windows cp1252), not your code. See Module 06.

## 🧯 Triage — if you're running behind
Cut in this order (lowest learning-loss first):
1. Skip the Module 08 mini-challenge and the stretch goals.
2. Make `press_release.py` a take-home instead of in-class.
3. Compress Module 02's `None` mention to one sentence.
4. **Never cut:** f-strings (06) and the `input()`+casting bug (05) — they're load-bearing for the whole course.

## 🎯 Success check (leave the room able to…)
- [ ] Build a sentence with an f-string including a 2-decimal number.
- [ ] Slice and reverse a string.
- [ ] Read `input()`, cast it, and use it in a calculation without a type error.
- [ ] Clean a messy string with chained methods — and explain why the original is unchanged.
