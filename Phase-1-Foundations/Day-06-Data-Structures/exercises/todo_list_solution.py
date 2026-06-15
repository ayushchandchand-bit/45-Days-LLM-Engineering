"""
Exercise 1 — Todo List Manager (solution).

Run (asks for input):
    python todo_list_solution.py
"""

tasks = []   # list of task strings

def show_tasks():
    """Print the tasks, numbered from 1 (or a friendly empty message)."""
    if not tasks:                              # empty list is falsy (Day 3)
        print("  (no tasks yet)")
        return
    for i, task in enumerate(tasks, start=1):  # 1-based numbering for humans
        print(f"  {i}. {task}")

print("Todo List - commands: add | done | list | quit")
while True:
    command = input("> ").strip().lower()

    if command == "add":
        task = input("  new task: ").strip()
        if task:
            tasks.append(task)                 # add to the end
            print(f"  added: {task}")
        else:
            print("  (empty task ignored)")

    elif command == "list":
        show_tasks()

    elif command == "done":
        show_tasks()
        if not tasks:
            continue
        raw = input("  finish which number? ").strip()
        if not raw.isdigit():
            print("  please enter a number")
            continue
        index = int(raw) - 1                   # 1-based choice -> 0-based index
        if 0 <= index < len(tasks):
            finished = tasks.pop(index)        # remove & return by index
            print(f"  done: {finished}")
        else:
            print("  no task with that number")

    elif command == "quit":
        print(f"  Bye! {len(tasks)} task(s) still pending.")
        break

    else:
        print("  commands: add | done | list | quit")
