# 08 — The `print()` Function

`print()` is how your program talks to you. You've used it already — here's the full picture.

## Printing multiple values
Pass several values separated by commas. `print()` joins them with a **space** by default.

```python
print("Score:", 42, "points")   # Score: 42 points
```

## `sep` — change the separator between values
```python
print("2024", "06", "10", sep="-")   # 2024-06-10
print("a", "b", "c", sep="")          # abc
```

## `end` — change what's printed at the end
By default `print()` adds a newline (`\n`) at the end. Change it to keep printing on one line:

```python
print("Loading", end="")
print("...", end="")
print(" done")          # Loading... done
```

## Printing numbers and text together
You can mix types freely with commas — `print()` converts each to text for you:

```python
age = 25
print("I am", age, "years old")
```

> On Day 2 you'll learn **f-strings** (`f"I am {age} years old"`) — the cleaner way to build
> strings. For now, commas are perfect.

Run the example:

```bash
python print_basics.py
```

➡ Next: [the exercises »](../exercises/)
