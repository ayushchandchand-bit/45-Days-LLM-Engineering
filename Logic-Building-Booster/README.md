# Logic-Building Booster — Fake Systems Edition 🧠

Six problems that make you **think**, not just recall syntax. Each one is a *simulated* real-world
system — a login screen, an OTP flow, a shopping cart — stripped down to its **logic**. No real
security, no real SMS, no real payments: the point is to practise turning a real-world rule into
loops, conditionals, and state.

Everything here uses only what you already know from **Days 1–7** (variables, strings, booleans,
loops, functions, lists/dicts/sets, and classes). Nothing from the AI track is needed.

> This is a standalone booster you can run any session — it is **not** tied to a specific day.

## How to use this

1. **Read a problem** and try it *before* looking at anything else. Struggling is the point.
2. Stuck? Read the **Approach hint** — it nudges, it doesn't solve.
3. Write your answer in the **stub file** (`qN_*.py`, has `# TODO`s).
4. Run it, then compare with the worked **solution** (`qN_*_solution.py`).

Every file is runnable on its own:

```bash
python q1_fake_login_solution.py
```

> ⚠️ On Windows use the real CPython:
> `C:\Users\Pc\AppData\Local\Programs\Python\Python314\python.exe q1_fake_login_solution.py`

---

## The 5-step method (use it on every problem)

| Step | Ask yourself | Output |
|--:|---|---|
| 1. **Understand** | What are the **inputs**? The **output**? The rules/edge cases? | A one-line restatement |
| 2. **Example by hand** | Solve one case on paper. *How* did your brain do it? | A traced example |
| 3. **Plan** | Write the steps in plain English (pseudocode). Pick a **pattern**. | Pseudocode |
| 4. **Code** | Translate each pseudocode line to Python. | A function / method |
| 5. **Test** | Try normal, boundary, and weird inputs. | Confidence |

**The pattern toolbox** (you've met all of these): *accumulator* (running total), *counter*,
*boolean flag*, *guard clause* (reject bad input first), *best-so-far* (max/min), *dict lookup*,
and *state on an object* (a class remembers things between calls).

---

## The problems

| # | Problem | Scenario | Core pattern(s) | Files |
|--:|---------|----------|-----------------|-------|
| 1 | **Fake Login** | 3 wrong tries → lockout | dict lookup · counter · set · flags | [stub](q1_fake_login.py) · [solution](q1_fake_login_solution.py) |
| 2 | **OTP Engine** | send / verify / expire | state machine · counter · matching | [stub](q2_otp_engine.py) · [solution](q2_otp_engine_solution.py) |
| 3 | **Fake Cart & Bill** | subtotal → coupon → GST | accumulator · dict iteration | [stub](q3_fake_cart.py) · [solution](q3_fake_cart_solution.py) |
| 4 | **Password Strength** | score a password /5 | boolean flags · scoring | [stub](q4_password_strength.py) · [solution](q4_password_strength_solution.py) |
| 5 | **Wallet / UPI** | deposit / withdraw + statement | guard clauses · history list | [stub](q5_wallet_upi.py) · [solution](q5_wallet_upi_solution.py) |
| 6 | **Coupon Engine** | pick the best coupon | best-so-far · skip rule | [stub](q6_coupon_engine.py) · [solution](q6_coupon_engine_solution.py) |

---

### Problem 1 — Fake Login System 🔐
Store users as `{username: password}`. Return `"OK"` / `"WRONG"` / `"NO_USER"`, and after **3 wrong
tries** lock the account (`"LOCKED"`).

> **Approach hint:** Ask the questions in order of specificity — *locked? → exists? → correct?*. The
> "3 tries" rule is just a **counter** per username plus a threshold; a **set** remembers who is
> locked.

### Problem 2 — OTP Engine 📱
`send()` makes a fresh 6-digit code and resets an attempt budget; `verify()` returns
`OK` / `WRONG` / `EXPIRED` / `NO_OTP`.

> **Approach hint:** The engine is a tiny **state machine** — it only remembers *the current OTP* and
> *attempts left*. Every wrong guess spends one attempt; at zero it's `EXPIRED`. A correct guess
> **consumes** the OTP (set it back to `None`).

### Problem 3 — Fake Cart & Bill 🛒
Add/remove items, then build a bill: **subtotal → minus discount → plus 18% GST → total**.

> **Approach hint:** `subtotal` is the **accumulator** pattern over `price*qty`. Get the *order*
> right — discount comes off *before* GST. A coupon is just an `if`-rule that returns a rupee amount.

### Problem 4 — Password Strength Checker 🛡️
Score `/5`: length ≥ 8, uppercase, lowercase, digit, special. Map score → Weak / Medium / Strong.

> **Approach hint:** Five **boolean flags**, all starting `False`, flipped in **one pass** over the
> characters. `score = sum(checks.values())` because `True == 1`. A fuzzy "is it strong?" becomes a
> countable "how many boxes are ticked?".

### Problem 5 — Wallet / UPI Simulator 💸
`deposit` / `withdraw` with validation, plus a `statement()` mini-log.

> **Approach hint:** Lead every method with **guard clauses** — reject `amount <= 0` and
> over-withdrawal *first*, then do the happy path. Keep a **history list** of
> `(type, amount, balance_after)`; the statement is just that list printed back.

### Problem 6 — Coupon Engine 🎟️
Given a cart total and several coupons, return the **one that saves the most**.

> **Approach hint:** **Best-so-far**: start `best_discount = 0`, loop the coupons, `continue` past any
> whose `min_total` isn't met, compute each rupee discount, and keep the champion. Each coupon is
> **data** (a dict), so new offers are new rows, not new code.

---

### Stretch goals (if you finish early)
- **Login:** add an `unlock(username)` admin method; track a *timestamp* of the last failed try.
- **OTP:** add a real resend cool-down (a counter that must reach 0 before `send()` works again).
- **Cart:** let a coupon be *percent OR flat*, and pick whichever is cheaper for the shop.
- **Password:** reject passwords containing the username; report *which* rules failed (already returned).
- **Wallet:** add `transfer(other_wallet, amount)` built on top of `withdraw` + `deposit`.
- **Coupon:** return the **full ranking** of coupons by savings, not just the winner.
