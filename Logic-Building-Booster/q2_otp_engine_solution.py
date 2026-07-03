"""
Problem 2 - OTP Engine (SOLUTION).

Run:
    python q2_otp_engine_solution.py

Logic-building note:
  An OTP flow is a tiny STATE MACHINE. At any moment the engine remembers:
    - the current OTP (or None if none is active)
    - how many verify attempts are still allowed
  Every action just reads and updates that state:
    send()   -> make a fresh random OTP, reset the attempt budget
    verify() -> compare; on a miss, spend one attempt; at zero, it EXPIRES
  We PRINT the OTP like a fake SMS gateway so you can trace the flow.
"""

import random   # imported like any module (Day 7). random.randint(a, b) is inclusive.


class OTPEngine:
    def __init__(self, length=6, max_attempts=3):
        self.length = length
        self.max_attempts = max_attempts
        self.otp = None            # no OTP active yet
        self.attempts_left = 0

    def send(self):
        """Generate a fresh OTP with exactly `length` digits and 'text' it."""
        low = 10 ** (self.length - 1)      # 6 digits -> 100000
        high = 10 ** self.length - 1       # 6 digits -> 999999
        self.otp = random.randint(low, high)
        self.attempts_left = self.max_attempts
        print(f"[SMS] Your OTP is {self.otp}")
        return self.otp

    def verify(self, entered):
        if self.otp is None:
            return "NO_OTP"                # nothing to check against
        if self.attempts_left <= 0:
            return "EXPIRED"               # budget already used up
        if entered == self.otp:
            self.otp = None                # consume it - one OTP, one use
            return "OK"
        # wrong guess -> spend one attempt
        self.attempts_left -= 1
        if self.attempts_left <= 0:
            return "EXPIRED"
        return "WRONG"


if __name__ == "__main__":
    engine = OTPEngine(length=6, max_attempts=3)

    real = engine.send()               # the fake gateway shows us the code
    print("verify(000000)  ->", engine.verify(0))       # wrong
    print("verify(guess)   ->", engine.verify(real - 1))  # wrong again
    print(f"verify({real}) ->", engine.verify(real))    # correct -> OK
    print("verify(again)   ->", engine.verify(real))    # OTP already consumed

    print("\n-- resend, then burn all attempts --")
    real = engine.send()
    for guess in (1, 2, 3):            # 3 wrong tries exhausts the budget
        print(f"verify({guess}) ->", engine.verify(guess))
    print(f"verify({real}) ->", engine.verify(real))    # too late -> EXPIRED
