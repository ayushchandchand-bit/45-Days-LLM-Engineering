# 04 — Comments

Comments are notes for **humans**. Python ignores them completely when running your code.

## Single-line comments
Everything after a `#` on a line is a comment.

```python
# This whole line is a comment
print("Hi")  # This part (after the code) is an inline comment
```

## "Block" comments
Python has no special multi-line comment syntax — you just use `#` on each line:

```python
# This is a longer note
# spread across
# several lines.
```

> You'll often see triple-quoted strings (`""" ... """`) used as multi-line notes too
> (especially as **docstrings** at the top of files/functions). Technically those are strings,
> not comments — more on that on Day 2 and Day 5.

## Why comment?
- Explain *why*, not *what*. Good code already shows *what* it does.
- ❌ `x = x + 1  # add 1 to x`  (obvious — useless)
- ✅ `retries += 1  # the API occasionally drops the first request`

## Keyboard shortcut
In VS Code, select lines and press **Ctrl + /** (Cmd + / on Mac) to toggle comments.

Run the example:

```bash
python comments.py
```

➡ Next: [05-variables](../05-variables/)
