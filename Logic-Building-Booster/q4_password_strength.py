"""
Problem 4 - Password Strength Checker (STUB - fill in the TODOs).

Score a password out of 5, one point for each rule it passes:
  1. length >= 8
  2. has an UPPERCASE letter
  3. has a lowercase letter
  4. has a digit
  5. has a special character (from SPECIALS below)
Verdict:  5 -> "Strong",  3 or 4 -> "Medium",  otherwise "Weak".

Run:
    python q4_password_strength.py
"""

SPECIALS = "!@#$%^&*()-_=+[]{};:,.?/"


def check_password(pw):
    has_upper = has_lower = has_digit = has_special = False

    # TODO: loop over each character `ch` in pw and flip the right flag:
    #   ch.isupper() -> has_upper = True
    #   ch.islower() -> has_lower = True
    #   ch.isdigit() -> has_digit = True
    #   ch in SPECIALS -> has_special = True

    checks = {
        "length>=8": len(pw) >= 8,
        "uppercase": has_upper,
        "lowercase": has_lower,
        "digit": has_digit,
        "special": has_special,
    }

    # TODO: score = sum(checks.values())
    # TODO: map score -> verdict ("Strong" / "Medium" / "Weak")
    score = 0
    verdict = "Weak"
    return score, verdict, checks


if __name__ == "__main__":
    for pw in ["abc", "Password1", "Str0ng!Pass"]:
        print(pw, "->", check_password(pw))
