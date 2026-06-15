"""
Exercise 3 — Common Skills Finder (STUDENT STUB).

Compare two candidates against a role using SET algebra.

Run:
    python common_skills.py
"""

required = {"python", "sql", "docker", "git", "aws"}
asha     = {"python", "sql", "git", "excel"}
ben      = {"python", "docker", "aws", "linux"}

# TODO 1: for each candidate, print:
#   - skills in common with the role:   candidate & required
#   - required skills they are missing: required - candidate
# TODO 2: print skills only ONE candidate has:  asha ^ ben
# TODO 3: print the combined skill pool:         asha | ben
# TODO 4: decide who covers more required skills (compare len of the & sets)
