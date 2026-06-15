"""
List patterns: iterate, sort, comprehensions, nested lists, copy-vs-reference.

Run:
    python list_patterns.py
"""

# =====================================================================
# 1) sort() vs sorted()  (mutate-in-place vs return-new)
# =====================================================================
scores = [72, 95, 60, 88, 79]
print("sorted(scores) :", sorted(scores), " (new list)")
print("original kept  :", scores)
scores.sort(reverse=True)                  # mutates IN PLACE, returns None
print("after .sort()   :", scores)
print("count of 88     :", [72, 88, 88].count(88))
print()

# =====================================================================
# 2) List comprehension — the Day-4 "build" pattern in one line
# =====================================================================
# long form:
squares_long = []
for n in range(6):
    squares_long.append(n * n)
# comprehension (identical result):
squares = [n * n for n in range(6)]
print("squares        :", squares)

# with a filter (only keep some items):
evens = [n for n in range(10) if n % 2 == 0]
print("evens          :", evens)

# transform real data: rupee strings -> numbers, 18% GST applied
prices = [199, 499, 1299]
with_gst = [round(p * 1.18, 2) for p in prices]
print("prices + GST   :", with_gst)
print()

# =====================================================================
# 3) Nested lists — a table (list of rows)
# =====================================================================
# Each inner list is a row: [name, marks]
report = [
    ["Asha", 88],
    ["Ben", 72],
    ["Chetan", 95],
]
print("Report card:")
for name, marks in report:                 # unpack each row
    print(f"  {name:<8} {marks}")
print("Chetan's marks (report[2][1]):", report[2][1])

# Sort the table by marks (descending) using a key function:
report.sort(key=lambda row: row[1], reverse=True)
print("Ranked        :", report)
print()

# =====================================================================
# 4) THE REFERENCE TRAP — b = a does NOT copy
# =====================================================================
a = [1, 2, 3]
b = a                                      # same list, two names (alias)
b.append(4)
print("a after b.append(4):", a)           # [1, 2, 3, 4]  <- a changed too!

# Independent copy: .copy()  (or a[:]  or  list(a))
a = [1, 2, 3]
c = a.copy()
c.append(4)
print("a stays put        :", a)           # [1, 2, 3]
print("c is separate      :", c)           # [1, 2, 3, 4]
