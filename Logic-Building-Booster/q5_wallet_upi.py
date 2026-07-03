"""
Problem 5 - Wallet / UPI Simulator (STUB - fill in the TODOs).

Build a wallet that tracks a balance and a history of transactions:
  - deposit(amount)  -> reject amount <= 0 ("INVALID"), else add + log, "OK"
  - withdraw(amount) -> reject amount <= 0 ("INVALID"),
                        reject amount > balance ("INSUFFICIENT"),
                        else subtract + log, "OK"
  - statement()      -> print every logged transaction + current balance
Log each move in self.history as a tuple: (type, amount, balance_after).

Run:
    python q5_wallet_upi.py
"""


class Wallet:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        # TODO: guard: if amount <= 0 -> return "INVALID"
        # TODO: self.balance += amount
        # TODO: append ("DEPOSIT", amount, self.balance) to history; return "OK"
        pass

    def withdraw(self, amount):
        # TODO: guard 1: amount <= 0 -> "INVALID"
        # TODO: guard 2: amount > self.balance -> "INSUFFICIENT"
        # TODO: subtract, log ("WITHDRAW", amount, self.balance), return "OK"
        pass

    def statement(self):
        # TODO: loop self.history and print each row, then the current balance
        pass


if __name__ == "__main__":
    w = Wallet(balance=100)
    print("deposit(500)   ->", w.deposit(500))
    print("withdraw(9999) ->", w.withdraw(9999))
    w.statement()
