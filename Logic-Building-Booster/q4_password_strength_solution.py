"""
Problem 4 - Password Strength Checker (SOLUTION).

Run:
    python q4_password_strength_solution.py

Logic-building note:
  Five independent rules, each a True/False. Two patterns do all the work:
    - BOOLEAN FLAGS: start each flag False, flip it to True the moment you see
      proof (one pass over the characters).
    - SCORE = count of rules passed. Then map the score to a verdict word.
  Turning "is it strong?" into "how many of these 5 boxes are ticked?" is the
  whole trick - it makes a fuzzy question countable.
"""

SPECIALS = "!@#$%^&*()-_=+[]{};:,.?/"


def check_password(pw):
    """Return (score 0-5, verdict, checks-dict)."""
    has_upper = has_lower = has_digit = has_special = False

    for ch in pw:                       # ONE pass sets all four flags
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in SPECIALS:
            has_special = True

    checks = {
        "length>=8": len(pw) >= 8,
        "uppercase": has_upper,
        "lowercase": has_lower,
        "digit": has_digit,
        "special": has_special,
    }

    score = sum(checks.values())        # True counts as 1, so this is the tick count

    if score == 5:
        verdict = "Strong"
    elif score >= 3:
        verdict = "Medium"
    else:
        verdict = "Weak"

    return score, verdict, checks


if __name__ == "__main__":
    samples = ["abc", "password", "Password1", "Str0ng!Pass", "GoodPass9"]
    for pw in samples:
        score, verdict, checks = check_password(pw)
        missing = [rule for rule, ok in checks.items() if not ok]
        print(f"{pw!r:16} score={score}/5  {verdict:6}  missing={missing}")
