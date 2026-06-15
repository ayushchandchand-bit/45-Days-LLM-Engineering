"""
Tuples — ordered but UNCHANGEABLE (immutable). A frozen list / fixed record.

Run:
    python tuples.py
"""

# =====================================================================
# 1) Create and access (indexing works just like lists)
# =====================================================================
point = (3, 4)                       # round brackets
print("point      :", point)
print("point[0]   :", point[0])      # 3
print("length     :", len(point))

# But you CANNOT change a tuple:
try:
    point[0] = 9
except TypeError as e:
    print("can't edit :", e)
print()

# =====================================================================
# 2) Unpacking — the everyday superpower
# =====================================================================
person = ("Asha", 21, "Pune")
name, age, city = person             # one line -> three variables
print(f"{name} is {age}, from {city}")

# Swap two variables with NO temp variable (tuple packing/unpacking):
a, b = 10, 20
a, b = b, a
print("after swap : a =", a, " b =", b)
print()

# =====================================================================
# 3) You've used tuples already: returning multiple values (Day 5)
# =====================================================================
def min_max(nums):
    return min(nums), max(nums)      # this builds a tuple

lo, hi = min_max([4, 9, 1, 7])       # ...and we unpack it
print("min, max   :", lo, hi)
print()

# =====================================================================
# 4) WHY immutable matters: tuples can be dict keys / set members
# =====================================================================
# A list CANNOT be a dict key (TypeError); a tuple can. Perfect for coordinates.
locations = {
    (12.97, 77.59): "Bengaluru",
    (19.07, 72.87): "Mumbai",
}
print("lookup by coordinate:", locations[(19.07, 72.87)])
print()

# =====================================================================
# 5) REAL USE: fixed records you iterate and unpack
# =====================================================================
# A tuple signals "these fields belong together and won't change."
matches = [
    ("India", "Australia", 2),     # (team_a, team_b, winner_index... fixed facts)
    ("England", "India", 1),
]
for team_a, team_b, winner in matches:
    won = (team_a, team_b)[winner - 1]   # tiny index trick
    print(f"{team_a} vs {team_b} -> {won} won")

# Single-element tuple needs a trailing comma, or it's not a tuple:
not_a_tuple = (5)
real_tuple = (5,)
print("\n(5) is a", type(not_a_tuple).__name__,
      "| (5,) is a", type(real_tuple).__name__)
