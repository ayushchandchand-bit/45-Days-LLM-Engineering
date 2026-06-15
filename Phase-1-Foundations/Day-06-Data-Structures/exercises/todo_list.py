"""
Exercise 1 — Todo List Manager (STUDENT STUB).

A menu-driven todo app backed by a list. Combines Day-4 loops + Day-6 lists.

Run (asks for input):
    python todo_list.py
"""

tasks = []   # our list of task strings

# TODO: loop a menu with `while True:`
#   - input() a command: add / done / list / quit
#   - "add"  -> input() a task and tasks.append(it)
#   - "list" -> if empty say so; else enumerate(tasks, start=1) and print numbered
#   - "done" -> input() a number, convert to index (n-1), validate, tasks.pop(index)
#   - "quit" -> break
#   - anything else -> show the valid commands
