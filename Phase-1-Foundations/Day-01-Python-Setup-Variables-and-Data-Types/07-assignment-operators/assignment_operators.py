"""
Compound assignment operators — shortcuts for updating a variable in place.

Run:
    python assignment_operators.py
"""

x = 10
print("start:", x)

x += 3      # same as: x = x + 3
print("after += 3:", x)   # 13

x -= 5      # x = x - 5
print("after -= 5:", x)   # 8

x *= 2      # x = x * 2
print("after *= 2:", x)   # 16

x //= 3     # x = x // 3  (floor divide)
print("after //= 3:", x)  # 5

x **= 2     # x = x ** 2
print("after **= 2:", x)  # 25

x %= 7      # x = x % 7
print("after %= 7:", x)   # 4

# ----- The everyday use: a running total -----
print("\nRunning total of a shopping cart:")
total = 0
total += 199
total += 49
total += 25
print("cart total:", total)   # 273
