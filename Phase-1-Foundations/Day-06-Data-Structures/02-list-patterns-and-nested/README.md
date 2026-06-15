# 02 — List Patterns & Nested Lists

Now we put lists to work: iterate them, sort them, build new ones compactly, nest them for tables —
and dodge the reference trap that bites everyone.

## Iterating & ordering
```python
for item in cart: ...          # value only (Day 4)
for i, item in enumerate(cart): ...   # index + value
cart.sort()                    # sorts IN PLACE, returns None
cart.sort(reverse=True)        # descending
sorted(cart)                   # returns a NEW sorted list (original untouched)
cart.count("milk")             # how many times "milk" appears
```
⚠️ `sort()` mutates and returns `None`; `sorted()` returns a new list. Pick deliberately.

## List comprehension — the Pythonic "build a new list"
The Day-4 "build" pattern, compressed to one readable line:
```python
# long form
squares = []
for n in range(5):
    squares.append(n * n)
# comprehension (same result)
squares = [n * n for n in range(5)]            # [0, 1, 4, 9, 16]
# with a filter
evens = [n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]
```

## Nested lists — lists inside lists (grids, tables, matrices)
```python
grid = [[1, 2, 3],
        [4, 5, 6]]
grid[1][2]        # 6  -> row 1, column 2
for row in grid:        # outer = rows
    for cell in row:    # inner = columns (Day 4 nested loops!)
        ...
```

## ⚠️ Copy vs reference — the trap
`b = a` does **not** copy the list; both names point at the **same** list:
```python
a = [1, 2, 3]
b = a            # same list, two names
b.append(4)
print(a)         # [1, 2, 3, 4]  <- a changed too!
```
For an independent copy: `b = a.copy()` (or `a[:]`, or `list(a)`).

## 🎤 Talking points (what to say & focus on)
- **`sort()` vs `sorted()` is the classic pair.** One mutates + returns None; one returns a new list.
  Show `x = mylist.sort()` → `None`. Same "mutator returns None" lesson as Module 01 — reinforce it.
- **Comprehensions: introduce as a *shortcut for a loop they already know*.** Write the long `append`
  loop, then collapse it. Don't lead with the syntax; lead with the equivalence. Add the `if` filter
  second. Warn against cramming complex logic into one — readability first.
- **Nested lists = the grids from Day-4 nested loops, now stored.** `grid[row][col]`. This is the
  shape of a spreadsheet, a game board, a matrix — and of JSON arrays-of-arrays in Phase 1.
- **The reference trap is the must-teach.** Run `b = a; b.append(4); print(a)` live. The shared
  mutation shocks people. Then show `.copy()`. This explains a whole category of "why did my other
  list change?" bugs.
- **`enumerate` + `sort(key=...)` hook:** mention you can sort by a key (`sort(key=len)`) — a teaser
  they'll use with list-of-dicts in Module 04.

## ⚠️ Common mistakes to call out
- `x = mylist.sort()` then using `x` (it's `None`).
- Believing `b = a` copies — it aliases. Mutating `b` mutates `a`.
- Over-stuffing a comprehension until it's unreadable — a plain loop is fine.
- `grid[col][row]` instead of `grid[row][col]` — order is [row][column].

Run the examples:

```bash
python list_patterns.py
```

➡ Next: **[03-dictionaries](../03-dictionaries/)**
