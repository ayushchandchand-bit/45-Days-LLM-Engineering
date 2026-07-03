"""
Problem 1 - Fake Login System with lockout (STUB - fill in the TODOs).

Build a login checker that:
  - stores users as a dict {username: password}
  - returns "OK" on the right password
  - returns "WRONG" on a wrong password (and remembers the miss)
  - after `max_attempts` wrong tries, LOCKS the account -> "LOCKED"
  - returns "NO_USER" for an unknown username

Run:
    python q1_fake_login.py
"""


class LoginSystem:
    def __init__(self, users, max_attempts=3):
        self.users = users
        self.max_attempts = max_attempts
        self.failed = {}        # username -> count of wrong tries
        self.locked = set()     # usernames that are blocked

    def login(self, username, password):
        # TODO 1: if username is already in self.locked -> return "LOCKED"
        # TODO 2: if username not in self.users -> return "NO_USER"
        # TODO 3: if the stored password matches -> reset failed count, return "OK"
        # TODO 4: otherwise it is wrong: add 1 to self.failed[username]
        #         (use self.failed.get(username, 0) + 1)
        # TODO 5: if failures reached self.max_attempts -> add to self.locked, return "LOCKED"
        # TODO 6: else return "WRONG"
        pass


if __name__ == "__main__":
    users = {"aditi": "pass123", "rahul": "hunter2"}
    system = LoginSystem(users, max_attempts=3)

    trials = [
        ("aditi", "wrong"),
        ("aditi", "nope"),
        ("aditi", "still-wrong"),
        ("aditi", "pass123"),
        ("rahul", "hunter2"),
        ("ghost", "any"),
    ]
    for username, pw in trials:
        print(f"login({username!r}, {pw!r}) -> {system.login(username, pw)}")
