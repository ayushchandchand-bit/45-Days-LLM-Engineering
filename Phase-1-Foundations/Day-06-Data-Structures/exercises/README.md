# Day 06 — Exercises

Put today's tools to work: lists, dicts, tuples, sets — and choosing between them. Try each in the
stub file first, then check the matching `*_solution.py`.

---

## Exercise 1 — Todo List Manager ✅
A menu-driven todo app: add, remove, and list tasks. Combines Day-4 loops with Day-6 lists.

**Your task:** in `todo_list.py`
1. Keep tasks in a `list`. Loop a menu with `while True:` (Day 4).
2. Options: **add** (`append`), **done** (`pop`/`remove` by number), **list** (`enumerate`), **quit** (`break`).
3. Show tasks numbered from 1; handle "no tasks yet" and invalid numbers gracefully.

*Skills:* lists (`append`/`pop`/`remove`/`enumerate`), `while` menu, `int()`, validation.
*Focus:* mutating a list safely behind a menu; converting a 1-based choice to a 0-based index.

➡ Solution: [`todo_list_solution.py`](todo_list_solution.py)

---

## Exercise 2 — Word Frequency Counter 🔤
The classic text-analysis task: count how many times each word appears. This is the foundation of
search, tag clouds, and (later) basic NLP.

**Your task:** in `word_frequency.py`
1. Take a paragraph (use the provided one or `input()`), `.lower()` it, and `.split()` into words.
2. Strip punctuation from each word (e.g. `word.strip(".,!?;:")`).
3. Build a `counts` dict with the **count pattern**: `counts[word] = counts.get(word, 0) + 1`.
4. Print the **top 5** words by count (`sorted(..., key=..., reverse=True)`).

*Skills:* dicts + `.get()` (count pattern), string methods (Day 2), sorting by a key.
*Focus:* `counts.get(word, 0) + 1` — the single most useful dict idiom there is.

➡ Solution: [`word_frequency_solution.py`](word_frequency_solution.py)

---

## Exercise 3 — Common Skills Finder 🧩
Compare two job candidates against a role using **set algebra**.

**Your task:** in `common_skills.py`
1. Define `required` (set), `asha` (set), `ben` (set) of skills.
2. For each candidate print: skills **in common** with the role (`&`), and skills **missing** (`-`).
3. Print skills **only one** of them has (`^`) and the **combined** skill pool (`|`).
4. Decide who's the better fit (more required skills covered).

*Skills:* sets, `&` / `|` / `-` / `^`, comparing sizes, choosing a structure (why a set, not a list).
*Focus:* mapping a real question ("who fits the role?") onto set operations.

➡ Solution: [`common_skills_solution.py`](common_skills_solution.py)

---

### Stretch goals (if you finish early)
- **Todo:** add a "priority" by storing dicts `{"task": ..., "done": False}` and a "mark done" option.
- **Word count:** ignore common stop-words (`{"the","a","is",...}` — a set!) before counting.
- **Skills:** rank any number of candidates (a list of dicts) by required-coverage and print a leaderboard.
