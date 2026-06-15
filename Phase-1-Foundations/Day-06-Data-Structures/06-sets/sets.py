"""
Sets — unordered collections of UNIQUE items. Two jobs: dedupe + compare.

Run:
    python sets.py
"""

# =====================================================================
# 1) Create — duplicates vanish automatically
# =====================================================================
tags = {"python", "ai", "python", "ml"}   # the duplicate "python" is dropped
print("tags        :", tags)
print("'ai' in tags:", "ai" in tags)       # fast membership test
tags.add("rag")
tags.discard("ml")                          # discard = remove, no error if absent
print("after edits :", tags)

# GOTCHA: {} is an empty DICT. For an empty set, use set().
empty = set()
print("type of {} :", type({}).__name__, "| type of set():", type(empty).__name__)
print()

# =====================================================================
# 2) REAL USE: deduplicate a list (the #1 reason people reach for sets)
# =====================================================================
signups = ["a@x.com", "b@x.com", "a@x.com", "c@x.com", "b@x.com"]
unique_emails = set(signups)
print("raw signups   :", len(signups))
print("unique signups:", len(unique_emails), "->", unique_emails)
print()

# =====================================================================
# 3) Set algebra — the reason sets exist
# =====================================================================
asha_skills = {"python", "sql", "git", "excel"}
ben_skills  = {"python", "git", "docker", "aws"}

print("Both know (intersection &):", asha_skills & ben_skills)
print("Either knows (union |)    :", asha_skills | ben_skills)
print("Only Asha (difference -)  :", asha_skills - ben_skills)
print("Exactly one (sym diff ^)  :", asha_skills ^ ben_skills)
print()

# =====================================================================
# 4) REAL USE: which required skills is a candidate missing?
# =====================================================================
required = {"python", "sql", "docker", "git"}
candidate = {"python", "git", "excel"}
missing = required - candidate              # required but not held
have = required & candidate                 # required and held
print(f"Candidate has {len(have)}/{len(required)} required skills.")
print("Missing:", missing or "none - great fit!")
print()

# =====================================================================
# 5) REAL USE: track "already seen" IDs in a stream (fast + unique)
# =====================================================================
# A crawler / dedup pipeline: skip anything we've processed before.
seen = set()
incoming = [101, 102, 101, 103, 102, 104]
for item_id in incoming:
    if item_id in seen:                     # membership check is fast
        print(f"  {item_id}: duplicate, skip")
        continue
    seen.add(item_id)
    print(f"  {item_id}: new, processing")
print("distinct processed:", len(seen))
