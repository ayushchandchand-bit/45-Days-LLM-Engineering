"""
Exercise 1 — Magic Trick (solution).

Run with different starting numbers — the result is always 4.0.
    python magic_trick_solution.py
"""

number = 7              # try changing this to any number
original = number       # remember where we started

number += 6             # 1. add 6
number *= 2             # 2. multiply by 2
number -= 4             # 3. subtract 4
number /= 2             # 4. divide by 2
number -= original      # 5. subtract the original number

print("Starting number:", original)
print("Result:", number)   # always 4.0

# Why does it work? Algebra:
#   ((n + 6) * 2 - 4) / 2 - n
# = (2n + 12 - 4) / 2 - n
# = (2n + 8) / 2 - n
# = (n + 4) - n
# = 4
