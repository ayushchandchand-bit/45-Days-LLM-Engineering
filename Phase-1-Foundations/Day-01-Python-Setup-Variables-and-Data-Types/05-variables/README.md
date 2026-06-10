# 05 — Variables

A **variable** is a name that points to a value. Think of it as a labelled box.

```python
age = 25
name = "Arjit"
price = 199.99
```

The `=` is the **assignment operator**: "take the value on the right, store it under the name on
the left." (It is *not* equality — that's `==`, which you'll meet on Day 3.)

## Using variables
Once stored, use the name anywhere you'd use the value:

```python
age = 25
print(age)         # 25
print(age + 1)     # 26
```

## Reassignment
A variable can be changed at any time — even to a different type. Python is **dynamically typed**.

```python
x = 10        # x is an int
x = "hello"   # now x is a string — totally fine in Python
```

The right side is evaluated **first**, then stored. This makes the classic "increment" work:

```python
score = 0
score = score + 10   # right side (0 + 10 = 10) is computed, then stored back in score
```

## Multiple assignment (handy)
```python
a, b = 1, 2          # a=1, b=2
x = y = z = 0        # all three set to 0
a, b = b, a          # swap! (no temp variable needed)
```

Run the examples:

```bash
python variables.py
```

➡ Next: [06-variable-naming](../06-variable-naming/)
