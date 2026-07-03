"""
Problem 1 - Fake Login System with lockout (SOLUTION).

Run:
    python q1_fake_login_solution.py

Logic-building note:
  A login screen is really THREE questions asked in order:
    1. Is this account locked?         -> a SET of locked usernames
    2. Does the username exist?        -> a DICT lookup (username -> password)
    3. Is the password correct?        -> compare, and COUNT wrong tries
  The whole "3 wrong tries then lock" rule is just a COUNTER + a threshold.
  Nothing here is real security (passwords are plain text on purpose) - it is a
  simulation to practise state + conditionals.
"""


class LoginSystem:
    def __init__(self, users, max_attempts=3):
        self.users = users                 # dict: username -> password
        self.max_attempts = max_attempts   # wrong tries allowed before lockout
        self.failed = {}                   # username -> how many wrong tries so far
        self.locked = set()                # usernames that are now blocked

    def login(self, username, password):
        # Question 1: already locked? (check this FIRST - most specific)
        if username in self.locked:
            return "LOCKED"

        # Question 2: does the account even exist?
        if username not in self.users:
            return "NO_USER"

        # Question 3: correct password?
        if self.users[username] == password:
            self.failed[username] = 0      # success resets the counter
            return "OK"

        # Wrong password -> bump this user's failure counter
        self.failed[username] = self.failed.get(username, 0) + 1
        if self.failed[username] >= self.max_attempts:
            self.locked.add(username)
            return "LOCKED"
        return "WRONG"                     # still has tries left


def attempts_left(system, username):
    """Small helper so the demo can print a friendly count."""
    used = system.failed.get(username, 0)
    return system.max_attempts - used


if __name__ == "__main__":
    users = {"aditi": "pass123", "rahul": "hunter2"}
    system = LoginSystem(users, max_attempts=3)

    # A student would normally type these; we script them to show every branch.
    trials = [
        ("aditi", "wrong"),
        ("aditi", "nope"),
        ("aditi", "still-wrong"),   # 3rd fail -> LOCKED
        ("aditi", "pass123"),       # correct, but account is locked now
        ("rahul", "hunter2"),       # different user logs in fine
        ("ghost", "any"),           # no such user
    ]

    for username, pw in trials:
        result = system.login(username, pw)
        left = attempts_left(system, username)
        print(f"login({username!r}, {pw!r}) -> {result}  (tries left: {left})")
