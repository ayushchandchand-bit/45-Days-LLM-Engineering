"""
Problem 6 - Coupon Engine: pick the best coupon (SOLUTION).

Run:
    python q6_coupon_engine_solution.py

Logic-building note:
  "Which coupon saves the most?" is the BEST-SO-FAR pattern (like finding a
  maximum), with a skip rule mixed in:
    - start with best_discount = 0, best_code = None
    - for each coupon: if the cart is too small, SKIP it (continue)
    - work out this coupon's rupee discount
    - if it beats the best so far, it becomes the new champion
  Each coupon is just data (a dict), so adding a new offer means adding a row,
  not new code. Rupees shown as 'Rs.' for console safety.
"""

# Each coupon: code, kind ("percent" or "flat"), value, and a minimum spend.
COUPONS = [
    {"code": "SAVE10",  "kind": "percent", "value": 10, "min_total": 0},
    {"code": "SAVE25",  "kind": "percent", "value": 25, "min_total": 2000},
    {"code": "FLAT150", "kind": "flat",    "value": 150, "min_total": 800},
    {"code": "FLAT500", "kind": "flat",    "value": 500, "min_total": 3000},
]


def discount_for(coupon, total):
    """Rupee discount this coupon gives on `total` (0 if not eligible)."""
    if total < coupon["min_total"]:
        return 0                                  # cart too small - skip rule
    if coupon["kind"] == "percent":
        raw = total * coupon["value"] / 100
    else:                                         # "flat"
        raw = coupon["value"]
    return min(raw, total)                        # never discount below zero


def best_coupon(total, coupons=COUPONS):
    """Return (best_code, best_discount) - the biggest saving available."""
    best_code = None
    best_discount = 0                             # best-so-far starts at nothing
    for coupon in coupons:
        d = discount_for(coupon, total)
        if d > best_discount:                     # a new champion?
            best_discount = d
            best_code = coupon["code"]
    return best_code, best_discount


if __name__ == "__main__":
    for total in [500, 1000, 2500, 4000]:
        code, disc = best_coupon(total)
        pay = total - disc
        print(f"Cart Rs.{total:<5} best={code or 'none':7} "
              f"save Rs.{disc:<7.2f} pay Rs.{pay:.2f}")
