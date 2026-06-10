# 01 — Running Python

> 🐍 **Haven't installed Python yet?** Do the [**Python Installation Guide**](../../Python-Installation-Guide.md)
> first (Windows / macOS / Linux), then come back here.

There are **two ways** to run Python, and you'll use both constantly.

## 1. The REPL (interactive mode)
REPL = **R**ead **E**val **P**rint **L**oop. Type Python, press Enter, see the result instantly.
Great for quick experiments.

```bash
python
```

You'll see a `>>>` prompt:

```python
>>> 2 + 2
4
>>> "hello".upper()
'HELLO'
>>> exit()   # or press Ctrl+Z then Enter (Windows) / Ctrl+D (mac/Linux)
```

> Tip: `ipython` is a nicer REPL with colors, autocomplete, and `?` help. Install later with
> `pip install ipython`.

## 2. Script files (`.py`)
For anything you want to **keep and re-run**, put it in a file. That's how real programs are built.

Run the example in this folder:

```bash
python hello.py
```

## Which do I use?
- **REPL** → "what does this do?" / quick math / testing one line
- **Script** → anything you'll run more than once, or share

## A note on Python versions
This course uses **Python 3.10+** (3.12 recommended). Check yours:

```bash
python --version
```

Python 2 is dead — if you see `Python 2.x`, you need `python3` instead.

➡ Next: [02-numbers](../02-numbers/)
