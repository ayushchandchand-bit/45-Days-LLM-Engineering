"""
Problem 5 - Wallet / UPI Simulator (SOLUTION).

Run:
    python q5_wallet_upi_solution.py

Logic-building note:
  Every money method starts with GUARD CLAUSES - reject the bad case FIRST,
  then do the happy path. This keeps the real work un-nested and readable:
      if amount <= 0:            return "reject"
      if amount > self.balance:  return "reject"   (withdraw only)
      ... now it is safe to move the money ...
  We also keep a HISTORY list (a running log) - the "mini statement" is just
  that list printed back. Rupees shown as 'Rs.' for console safety.
"""


class Wallet:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []          # list of (type, amount, balance_after)

    def deposit(self, amount):
        if amount <= 0:                          # guard clause
            return "INVALID"
        self.balance += amount
        self.history.append(("DEPOSIT", amount, self.balance))
        return "OK"

    def withdraw(self, amount):
        if amount <= 0:                          # guard 1: sane amount
            return "INVALID"
        if amount > self.balance:                # guard 2: enough money?
            return "INSUFFICIENT"
        self.balance -= amount
        self.history.append(("WITHDRAW", amount, self.balance))
        return "OK"

    def statement(self):
        print("  -- Mini statement --")
        if not self.history:
            print("  (no transactions yet)")
        for kind, amount, after in self.history:
            print(f"  {kind:9} Rs.{amount:<8.2f} balance Rs.{after:.2f}")
        print(f"  Current balance: Rs.{self.balance:.2f}")


if __name__ == "__main__":
    w = Wallet(balance=100)

    print("deposit(500)   ->", w.deposit(500))
    print("withdraw(200)  ->", w.withdraw(200))
    print("withdraw(9999) ->", w.withdraw(9999))   # more than balance
    print("deposit(-50)   ->", w.deposit(-50))     # nonsense amount
    print("withdraw(400)  ->", w.withdraw(400))
    print()
    w.statement()
