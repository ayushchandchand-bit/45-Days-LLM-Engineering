"""
Problem 6 - Coupon Engine: pick the best coupon (STUB - fill in the TODOs).

Given a cart total and a list of coupons, find the ONE coupon that saves the
most money (and is eligible for that cart). Each coupon is a dict:
    {"code", "kind": "percent"|"flat", "value", "min_total"}
Rules:
  - if total < min_total -> coupon does not apply (discount 0)
  - percent -> discount = total * value / 100
  - flat    -> discount = value
  - a discount can never exceed the total

Run:
    python q6_coupon_engine.py
"""

COUPONS = [
    {"code": "SAVE10",  "kind": "percent", "value": 10, "min_total": 0},
    {"code": "SAVE25",  "kind": "percent", "value": 25, "min_total": 2000},
    {"code": "FLAT150", "kind": "flat",    "value": 150, "min_total": 800},
    {"code": "FLAT500", "kind": "flat",    "value": 500, "min_total": 3000},
]


def discount_for(coupon, total):
    # TODO: if total < coupon["min_total"] -> return 0
    # TODO: percent -> raw = total * value / 100 ; flat -> raw = value
    # TODO: return min(raw, total)
    return 0


def best_coupon(total, coupons=COUPONS):
    best_code = None
    best_discount = 0
    # TODO: loop coupons; compute discount_for each; keep the biggest
    #       (best-so-far: if d > best_discount, update best_discount + best_code)
    return best_code, best_discount


if __name__ == "__main__":
    for total in [500, 2500, 4000]:
        print(total, "->", best_coupon(total))
