"""
Problem 2 - OTP Engine (STUB - fill in the TODOs).

Build a one-time-password engine that:
  - send()  -> generates a fresh 6-digit OTP, resets the attempt budget, "texts" it
  - verify(entered):
        "OK"      if it matches (then the OTP is used up)
        "WRONG"   if it does not match and tries remain
        "EXPIRED" once the attempt budget hits zero
        "NO_OTP"  if no OTP was ever sent

Run:
    python q2_otp_engine.py
"""

import random


class OTPEngine:
    def __init__(self, length=6, max_attempts=3):
        self.length = length
        self.max_attempts = max_attempts
        self.otp = None
        self.attempts_left = 0

    def send(self):
        # TODO 1: low  = 10 ** (self.length - 1)   # smallest 6-digit number
        # TODO 2: high = 10 ** self.length - 1      # largest 6-digit number
        # TODO 3: self.otp = random.randint(low, high)
        # TODO 4: self.attempts_left = self.max_attempts
        # TODO 5: print the OTP like an SMS and return it
        pass

    def verify(self, entered):
        # TODO 1: if self.otp is None -> return "NO_OTP"
        # TODO 2: if self.attempts_left <= 0 -> return "EXPIRED"
        # TODO 3: if entered == self.otp -> set self.otp = None, return "OK"
        # TODO 4: wrong guess: self.attempts_left -= 1
        # TODO 5: if self.attempts_left <= 0 -> return "EXPIRED", else return "WRONG"
        pass


if __name__ == "__main__":
    engine = OTPEngine()
    real = engine.send()
    print("verify(wrong)   ->", engine.verify(0))
    print(f"verify({real}) ->", engine.verify(real))
