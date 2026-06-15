"""
Walking dicts (keys/values/items), merging them, and the list-of-dicts pattern.

Run:
    python dict_iteration.py
"""

prices = {"coffee": 120, "tea": 80, "juice": 90}

# =====================================================================
# 1) The three views: keys, values, items
# =====================================================================
print("keys  :", list(prices.keys()))
print("values:", list(prices.values()))
print("items :", list(prices.items()))
print("sum of all prices:", sum(prices.values()))   # values() feeds sum()
print()

# =====================================================================
# 2) Looping: bare loop = keys; .items() = key + value
# =====================================================================
for item in prices:                      # looping a dict gives KEYS
    print("  key only:", item)
print()
for name, price in prices.items():       # idiomatic: unpack key, value
    print(f"  {name:<8} Rs {price}")
print()

# =====================================================================
# 3) Merging dicts — right side wins on clashes (defaults + overrides)
# =====================================================================
defaults = {"theme": "light", "lang": "en", "notifications": True}
user     = {"lang": "hi", "theme": "dark"}
settings = {**defaults, **user}          # user values override defaults
print("merged settings:", settings)
print()

# =====================================================================
# 4) Build a dict in a loop — the COUNT pattern (most useful dict idiom)
# =====================================================================
# Tally how many of each fruit we have. d.get(key, 0) + 1 is the trick.
basket = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}
for fruit in basket:
    counts[fruit] = counts.get(fruit, 0) + 1   # missing -> start at 0, then +1
print("fruit counts:", counts)
print()

# =====================================================================
# 5) THE BIG ONE: a list of dicts (rows of records = CSV / DB / JSON)
# =====================================================================
students = [
    {"name": "Asha",   "marks": 88, "city": "Pune"},
    {"name": "Ben",    "marks": 72, "city": "Delhi"},
    {"name": "Chetan", "marks": 95, "city": "Pune"},
]

print("All records:")
for s in students:                       # each s is one record (a dict)
    print(f"  {s['name']:<8} {s['marks']:>3}  {s['city']}")

# Rank by a field (sort a list of dicts by 'marks', highest first):
students.sort(key=lambda s: s["marks"], reverse=True)
print("Top scorer:", students[0]["name"], "with", students[0]["marks"])

# Filter with a comprehension: just the Pune students' names
pune = [s["name"] for s in students if s["city"] == "Pune"]
print("From Pune  :", pune)

# Average marks across all records:
avg = sum(s["marks"] for s in students) / len(students)
print(f"Class avg  : {avg:.1f}")
