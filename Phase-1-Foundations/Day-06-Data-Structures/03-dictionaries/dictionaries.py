"""
Dictionaries — key: value pairs. Look things up BY NAME, not by position.

Run:
    python dictionaries.py
"""

# =====================================================================
# 1) Create and access by key
# =====================================================================
student = {
    "name": "Asha",
    "age": 21,
    "marks": [88, 72, 95],        # values can be ANY type, even a list
}
print("name       :", student["name"])    # look up by key
print("how many pairs:", len(student))
print("'age' in?  :", "age" in student)    # `in` checks the KEYS
print("21 in?     :", 21 in student)       # False! 21 is a value, not a key
print()

# =====================================================================
# 2) Safe access: [] crashes on missing keys, .get() doesn't
# =====================================================================
# print(student["email"])         # would raise KeyError
print("get email (missing) :", student.get("email"))            # None
print("get email w/ default:", student.get("email", "n/a"))     # "n/a"
print()

# =====================================================================
# 3) Add / update / delete
# =====================================================================
student["email"] = "asha@example.com"      # add a new pair
student["age"] = 22                         # update an existing one
print("after add+update:", student)

removed = student.pop("marks")              # delete AND return the value
print("popped marks    :", removed)
del student["email"]                        # delete a pair (no return)
print("after deletes   :", student)
print()

# =====================================================================
# 4) REAL USE: a price lookup table (dict as a mini database)
# =====================================================================
prices = {"coffee": 120, "sandwich": 180, "juice": 90}
order = ["coffee", "juice", "coffee", "muffin"]   # "muffin" isn't on the menu
bill = 0
for item in order:
    price = prices.get(item, 0)             # unknown item -> 0, no crash
    if price == 0:
        print(f"  {item}: not on the menu, skipped")
    else:
        bill += price
        print(f"  {item}: Rs {price}")
print(f"Total bill: Rs {bill}")
print()

# =====================================================================
# 5) REAL USE: this is exactly what a JSON API / LLM response looks like
# =====================================================================
# Nested dicts + lists = JSON. Reading this is a Phase-1 daily task.
api_response = {
    "status": "ok",
    "user": {"id": 7, "name": "Asha", "roles": ["student", "admin"]},
    "credits": 250,
}
print("status     :", api_response["status"])
print("user name  :", api_response["user"]["name"])      # dig into nested dict
print("first role :", api_response["user"]["roles"][0])  # dict -> list -> index
