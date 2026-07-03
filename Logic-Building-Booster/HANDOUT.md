# Logic-Building Practice — Fake Systems 🧠

Six problems. Each is a **simulated** real-world system (no real security/SMS/payments) stripped down
to its **logic**. You will build each as a small **command-line (CLI) program** that takes input with
`input()`, validates it, and prints results. Uses only Python basics (variables, loops, conditionals,
functions, lists/dicts/sets, classes). Try each *before* asking for help — struggling is the point.

**The method (use it every time):** Understand the inputs & output → solve one case *by hand* →
write the steps in plain English → turn each step into code → test normal, edge, and weird inputs.

**CLI ground rules for every problem:**
- Read input with `input(...)`; strip stray spaces with `.strip()`.
- **Validate before you use it** — never assume the user typed the right thing (empty text, letters
  where a number should be, negative amounts, etc.).
- To read a number safely: check `text.isdigit()` first, or wrap `int(text)` in `try/except ValueError`.
- Loop with a menu until the user chooses **Exit**. Print a clear message for every outcome.

---

## 1. Fake Login System 🔐

**Build:** a login screen that keeps asking for a username and password until the user logs in or the
account gets locked.

**Data:** hard-code a few users, e.g. `users = {"aditi": "pass123", "rahul": "hunter2"}`.

**What the program does (loop):**
1. Ask for **username** (`input`), then **password** (`input`).
2. Decide the outcome and print one of:
   - `Login successful!` — username exists **and** password matches → stop.
   - `Wrong password. Tries left: N` — password wrong, but attempts remain.
   - `No such user.` — username not in `users`.
   - `Account locked!` — after **3 wrong password attempts** for that user → stop.
3. Keep a **per-user** count of wrong tries. 3 wrong tries → lock that account (a wrong 4th attempt
   should say *locked*, even if they now type the right password).

**Validation:** reject empty username/password (re-ask). Username check is case-sensitive (keep it
simple).

**Sample run:**
```
Username: aditi
Password: wrong
Wrong password. Tries left: 2
Username: aditi
Password: nope
Wrong password. Tries left: 1
Username: aditi
Password: bad
Account locked!
```

> **Hint:** Ask the questions in order — *locked? → exists? → correct?*. "3 tries" is just a **counter**
> per user plus a threshold; a **set** of locked usernames remembers who's blocked.

---

## 2. OTP Engine 📱

**Build:** a menu-driven OTP tool that "texts" a code and then verifies what the user types.

**Menu (loop until Exit):**
```
1. Send OTP
2. Enter OTP
3. Exit
```

**Behaviour:**
- **Send OTP** → generate a fresh **6-digit** random number (use the `random` module), store it,
  reset the attempt budget to **3**, and print it like a fake SMS: `[SMS] Your OTP is 483920`.
- **Enter OTP** → ask the user to type the code, then print one of:
  - `Verified!` — matches → the OTP is now **used up** (can't be reused).
  - `Wrong OTP. Attempts left: N` — no match, tries remain.
  - `OTP expired.` — the 3 attempts are used up.
  - `No OTP sent yet.` — user tried to verify before sending.

**Validation:** if the user types something that isn't a 6-digit number when entering the OTP, say
`Enter a valid 6-digit code.` and don't spend an attempt.

**Sample run:**
```
Choice: 1
[SMS] Your OTP is 483920
Choice: 2
Enter OTP: 000000
Wrong OTP. Attempts left: 2
Choice: 2
Enter OTP: 483920
Verified!
```

> **Hint:** The engine only remembers **two things**: the current OTP and attempts left. Every wrong
> guess spends one attempt; a correct guess consumes the OTP (set it back to "none").

---

## 3. Fake Cart & Bill 🛒

**Build:** a shopping cart with a menu; at checkout, print an itemised bill.

**Menu (loop until Checkout/Exit):**
```
1. Add item
2. Remove item
3. View cart
4. Checkout
```

**Behaviour:**
- **Add item** → ask for **name**, **price**, and **quantity**. If the item already exists, add to its
  quantity instead of duplicating it.
- **Remove item** → ask for a name; remove it (say `Not in cart.` if it isn't there).
- **View cart** → list each item as `name  x qty  = ₹amount`.
- **Checkout** → ask for an optional coupon code, then print the bill in this **exact order**:
  **subtotal → minus discount → plus 18% GST → total.**

**Coupons:** `SAVE10` = 10% off the subtotal; `FLAT100` = ₹100 off if subtotal ≥ ₹500; anything else =
no discount.

**Validation:** price and quantity must be **positive numbers** — reject letters/negatives and re-ask.

**Sample checkout:**
```
Coupon (blank for none): SAVE10
Subtotal : ₹779.00
Discount : ₹77.90  (SAVE10)
GST 18%  : ₹126.20
TOTAL    : ₹827.30
```

> **Hint:** Subtotal is a **running total** over `price × qty`. Order matters — discount comes off
> *before* GST is added. A coupon is just an `if`-rule that returns a rupee amount.

---

## 4. Password Strength Checker 🛡️

**Build:** a CLI that reads a password and reports its strength — plus which rules it failed.

**Behaviour (loop):**
1. Ask the user to type a password.
2. Score it out of **5**, one point per rule: length ≥ 8, has uppercase, has lowercase, has a digit,
   has a special character (`!@#$%^&*` …).
3. Print the score, a verdict — **5 → Strong, 3–4 → Medium, else Weak** — and the **list of failed
   rules** so the user knows how to improve.
4. Ask "check another? (y/n)".

**Sample run:**
```
Enter a password: Password1
Score: 4/5  ->  Medium
Missing: special character
Check another? (y/n): n
```

> **Hint:** Five true/false **flags**, all starting `False`, flipped in **one loop** over the
> characters. The score is just how many flags are `True`.

---

## 5. Wallet / UPI Simulator 💸

**Build:** a wallet app with a menu; every action validates the amount and updates a running balance.

**Menu (loop until Exit):**
```
1. Deposit
2. Withdraw
3. Mini statement
4. Exit
```

**Behaviour:**
- **Deposit** → ask for an amount; reject `amount ≤ 0`; else add it and print the new balance.
- **Withdraw** → ask for an amount; reject `amount ≤ 0`; reject if it's more than the balance
  (`Insufficient balance.`); else subtract it and print the new balance.
- **Mini statement** → print every transaction so far (type, amount, balance after) and the current
  balance.

**Validation:** amount must be a valid positive number — reject text/negatives and re-ask.

**Sample statement:**
```
DEPOSIT   ₹500.00   balance ₹600.00
WITHDRAW  ₹200.00   balance ₹400.00
Current balance: ₹400.00
```

> **Hint:** Start each action with **guard clauses** — reject the bad cases *first*, then do the real
> work. Keep a **history list** of every move; the statement is that list printed back.

---

## 6. Coupon Engine 🎟️

**Build:** a CLI that takes a cart total and tells the user the **best coupon** to use.

**Data:** a fixed list of coupons, each with a code, a kind (`percent` or `flat`), a value, and a
minimum spend. For example:
```
SAVE10   10% off,  min ₹0
SAVE25   25% off,  min ₹2000
FLAT150  ₹150 off, min ₹800
FLAT500  ₹500 off, min ₹3000
```

**Behaviour (loop):**
1. Ask for the **cart total**.
2. Check every coupon: skip any whose minimum spend isn't met; work out its rupee discount
   (percent → `total × value / 100`, flat → `value`); a discount can never exceed the total.
3. Print the **single coupon that saves the most**, the saving, and the amount to pay.
4. Ask "check another total? (y/n)".

**Sample run:**
```
Cart total: 2500
Best coupon: SAVE25  ->  save ₹625.00  ->  pay ₹1875.00
```

**Validation:** total must be a valid non-negative number.

> **Hint:** **Best-so-far** — start with "best saving = 0", check each coupon, skip any whose minimum
> isn't met, work out its discount, and keep the biggest one seen.

---

### Finished early? Stretch goals
- **Login:** add an admin `unlock` option; show a masked password (`****`) as the user types.
- **OTP:** add a resend cool-down (must wait N "ticks" before Send works again).
- **Cart:** let a coupon be percent *or* flat and pick the better one; support quantity edits.
- **Password:** reject passwords that contain the username; suggest a stronger version.
- **Wallet:** add **Transfer** between two wallets (built on withdraw + deposit).
- **Coupon:** print the full ranking of all eligible coupons, not just the winner.

> Reminder: these are **simulations for practice** — real logins, OTPs, and payments need proper
> security. Here we're only training your problem-solving logic.
