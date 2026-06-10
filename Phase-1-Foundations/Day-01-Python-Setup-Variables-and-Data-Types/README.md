# Day 01 — Python Setup, Data Types, Operators & Variables

Welcome to Day 1. Today is about getting Python running and getting comfortable with the
absolute building blocks: **numbers, operators, comments, and variables**. Everything else in
this course sits on top of these.

## Learning objectives
By the end of today you can:
- Run Python two ways — interactive (REPL) and script files
- Use the core numeric types (`int`, `float`) and all the operators
- Write comments and readable code
- Create, name, and reassign **variables**
- Use compound **assignment operators** (`+=`, `-=`, …)
- Print output with `print()` and its options (`sep`, `end`)

## Modules (work through them in order)

> 🎤 **Day 1 opens with a presentation** — *Basics of Software Engineering* — giving students the
> big-picture map (frontend, backend, API, DB, Git, cloud, DevOps, CI/CD, and where AI fits)
> before we touch code.

| # | Module | What it covers |
|--:|--------|----------------|
| 00 | [presentation-software-engineering-basics](00-presentation-software-engineering-basics/) | 🖥️ Opening talk (HTML slide deck): how real software is built |
| 01 | [running-python](01-running-python/) | The REPL vs script files; your first program |
| 02 | [numbers](02-numbers/) | Integers, floats, numeric notations |
| 03 | [operators](03-operators/) | Arithmetic + lesser-known operators (`//`, `%`, `**`) |
| 04 | [comments](04-comments/) | Single-line, inline, and block comments |
| 05 | [variables](05-variables/) | Storing values, reassignment, dynamic typing |
| 06 | [variable-naming](06-variable-naming/) | Rules, conventions, keywords to avoid |
| 07 | [assignment-operators](07-assignment-operators/) | `+=`, `-=`, `*=`, `//=`, `**=` … |
| 08 | [print-function](08-print-function/) | `print()` deep dive: `sep`, `end`, multiple values |

Then test yourself in **[exercises/](exercises/)**.

## How to run
From this folder, run any file directly:

```bash
python 02-numbers/numbers.py
```

Or open the interactive REPL and paste snippets:

```bash
python
>>> 2 + 2
4
```

## Today's exercise
**Magic Trick** — see [`exercises/`](exercises/). Pick any number, run it through a sequence of
operations, and the result is always the same. You'll build it using only what you learned today.
