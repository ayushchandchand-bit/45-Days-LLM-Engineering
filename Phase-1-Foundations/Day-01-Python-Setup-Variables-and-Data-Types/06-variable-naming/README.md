# 06 — Variable Naming

Good names make code readable. Python also has hard **rules** you can't break.

## The rules (must follow)
A variable name:
- ✅ may contain **letters, digits, and underscores** (`_`)
- ✅ must **start** with a letter or underscore — **not a digit**
- ❌ cannot contain spaces or symbols like `-`, `+`, `@`, `!`
- ❌ cannot be a Python **keyword** (`if`, `for`, `class`, `True`, `import`, …)
- is **case-sensitive**: `age`, `Age`, and `AGE` are three different variables

```python
user_name = "ok"      # ✅
_total = 0            # ✅
age2 = 30             # ✅
2age = 30             # ❌ SyntaxError — starts with a digit
user-name = "x"       # ❌ SyntaxError — '-' not allowed
class = "CS"          # ❌ SyntaxError — 'class' is a keyword
```

## The conventions (should follow)
Python style (PEP 8) prefers **`snake_case`** for variables and functions:

- ✅ `first_name`, `total_price`, `is_active`
- ❌ `firstName` (that's camelCase — used in Java/JS, not Python)

Make names **descriptive**: `n` is fine for a loop counter, but `total_users` beats `tu`.

## See the keyword list
```python
>>> import keyword
>>> keyword.kwlist
```

Run the example:

```bash
python variable_naming.py
```

➡ Next: [07-assignment-operators](../07-assignment-operators/)
