# 01 — Lists

A **list** is an **ordered, changeable** collection. It's the workhorse container — a cart, a queue,
a row of scores, the lines of a file.

```python
cart = ["milk", "bread", "eggs"]    # square brackets, comma-separated
cart[0]                             # "milk"   (index from 0)
cart[-1]                            # "eggs"   (negative = from the end)
len(cart)                           # 3
"milk" in cart                      # True
```

## Index & slice (same rules as strings, Day 2)
```python
cart[1]        # "bread"
cart[0:2]      # ['milk', 'bread']   (slice: start inclusive, stop exclusive)
cart[-2:]      # ['bread', 'eggs']
```

## Mutating methods (lists change in place)
| Method | Does | Example |
|--------|------|---------|
| `append(x)` | add `x` to the **end** | `cart.append("rice")` |
| `insert(i, x)` | insert `x` at index `i` | `cart.insert(0, "tea")` |
| `extend(other)` | add **all** items of another list | `cart.extend(["jam","oil"])` |
| `pop()` / `pop(i)` | remove & **return** last / index `i` | `last = cart.pop()` |
| `remove(x)` | remove first matching **value** | `cart.remove("bread")` |
| `cart[i] = x` | replace item at index `i` | `cart[0] = "coffee"` |

⚠️ Most of these **return `None`** and change the list in place. `result = cart.append("x")` makes
`result` be `None` — a classic beginner bug.

## 🎤 Talking points (what to say & focus on)
- **"A list is a row of labelled boxes, numbered from 0."** Indexing, negative indexing and slicing
  are *identical* to Day-2 strings — call that back; it's the same mental model, now mutable.
- **Mutable is the headline.** Unlike strings, you can change a list after making it. Demo
  `cart[0] = "coffee"` and watch the original change. This is new and important.
- **append vs insert vs extend.** `append` adds one to the end; `insert` squeezes one in; `extend`
  merges another list (vs `append(other_list)` which nests it — show that gotcha!).
- **`.append()` returns None.** Show `x = cart.append("rice"); print(x)` → `None`. They WILL hit this;
  pre-empt it. "Mutating methods change in place and hand back nothing."
- **pop vs remove:** `pop` works by *index* and gives you the item back (great for queues/stacks);
  `remove` works by *value* and returns nothing. Different jobs.

## ⚠️ Common mistakes to call out
- `result = list.append(x)` → `result` is `None` (append mutates, returns nothing).
- `list.append(other_list)` when you meant `extend` → you get a nested list, not merged items.
- `remove(x)` on a value that isn't there → `ValueError`. Check with `in` first if unsure.
- Index out of range (`cart[10]` on a 3-item list) → `IndexError`.

Run the examples:

```bash
python lists.py
```

➡ Next: **[02-list-patterns-and-nested](../02-list-patterns-and-nested/)**
