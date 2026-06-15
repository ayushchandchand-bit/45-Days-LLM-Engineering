"""
Exercise 3 — Common Skills Finder (solution).

Run:
    python common_skills_solution.py
"""

required = {"python", "sql", "docker", "git", "aws"}
asha     = {"python", "sql", "git", "excel"}
ben      = {"python", "docker", "aws", "linux"}

def report(name, skills):
    """Print how a candidate matches the role, using set algebra."""
    have = skills & required          # intersection: required AND held
    missing = required - have         # difference: required but NOT held
    print(f"{name}:")
    print(f"  covers  {len(have)}/{len(required)} required -> {have}")
    print(f"  missing -> {missing or 'none'}")
    return have

asha_have = report("Asha", asha)
ben_have = report("Ben", ben)
print()

# Skills exactly one of them has (symmetric difference):
print("Only one candidate has:", asha ^ ben)
# Everything the pair knows between them (union):
print("Combined skill pool   :", asha | ben)
print()

# Who's the better fit? (more required skills covered)
if len(asha_have) > len(ben_have):
    print("Best fit: Asha")
elif len(ben_have) > len(asha_have):
    print("Best fit: Ben")
else:
    print("It's a tie on required-skill coverage.")
