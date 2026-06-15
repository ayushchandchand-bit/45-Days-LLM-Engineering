"""
Choosing the right structure — same data, four containers, different jobs.

Run:
    python choosing.py
"""

# =====================================================================
# 1) The 4-question decision flow, applied to one scenario each
# =====================================================================

# Q: "look up by name/label?" -> DICT  (a user profile)
profile = {"name": "Asha", "age": 21, "email": "asha@x.com"}
print("DICT  profile['email'] ->", profile["email"])

# Q: "need uniqueness / compare groups?" -> SET  (unique tags)
post_tags = {"python", "ai", "python"}           # dup dropped
print("SET   unique tags      ->", post_tags)

# Q: "must never change / be a key?" -> TUPLE  (a coordinate)
location = (19.07, 72.87)
print("TUPLE location         ->", location, "(can't be edited)")

# Otherwise -> LIST  (an editable, ordered sequence)
cart = ["milk", "bread"]
cart.append("eggs")
print("LIST  cart             ->", cart)
print()

# =====================================================================
# 2) The SAME data done WRONG vs RIGHT
# =====================================================================
# WRONG: parallel lists you must keep in sync by index (fragile!)
names = ["Asha", "Ben"]
marks = [88, 72]
print("Parallel lists (fragile):", names[1], marks[1])   # must match indexes

# RIGHT: a list of dicts — each record keeps its own fields together
students = [
    {"name": "Asha", "marks": 88},
    {"name": "Ben",  "marks": 72},
]
print("List of dicts (clean)  :", students[1]["name"], students[1]["marks"])
print()

# =====================================================================
# 3) They NEST — and that nesting IS json / API data
# =====================================================================
classroom = {                                   # dict
    "subject": "AI",
    "students": [                               # list of...
        {"name": "Asha", "tags": {"python", "ml"}},   # dicts containing sets
        {"name": "Ben",  "tags": {"sql"}},
    ],
}
# Dig through the layers — exactly how you'll read a JSON response in Phase 1:
print("Subject        :", classroom["subject"])
print("First student  :", classroom["students"][0]["name"])
print("Their tags     :", classroom["students"][0]["tags"])

# Collect ALL distinct tags across the class using a set + loop:
all_tags = set()
for student in classroom["students"]:
    all_tags |= student["tags"]                 # union-update with each set
print("All class tags :", all_tags)
print()

# =====================================================================
# 4) A quick "which structure?" self-check (answers in comments)
# =====================================================================
print("Self-check - name the best structure:")
print("  coupon codes already redeemed   -> set  (uniqueness + fast 'seen it?')")
print("  product id -> stock count        -> dict (look up by key)")
print("  the 7 days of the week           -> tuple (fixed, never changes)")
print("  a to-do list you reorder         -> list (ordered, editable)")
