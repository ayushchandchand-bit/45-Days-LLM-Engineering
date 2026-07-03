"""
Problem 3 - Fake Cart & Bill (STUB - fill in the TODOs).

Build a shopping cart that can:
  - add(name, price, qty)  -> new item, or bump qty if it already exists
  - remove(name)
  - subtotal()             -> sum of price*qty over every item
  - bill(coupon)           -> dict with subtotal, discount, gst, total
Order of a bill:  subtotal -> minus discount -> plus 18% GST -> total.
Coupons:  "SAVE10" = 10% off;  "FLAT100" = Rs.100 off if subtotal >= 500.

Run:
    python q3_fake_cart.py
"""


class Cart:
    def __init__(self, gst_rate=0.18):
        self.items = {}            # name -> [price, qty]
        self.gst_rate = gst_rate

    def add(self, name, price, qty=1):
        # TODO: if name already in self.items -> add qty to its quantity
        #       else -> self.items[name] = [price, qty]
        pass

    def remove(self, name):
        # TODO: remove name if present (hint: self.items.pop(name, None))
        pass

    def subtotal(self):
        # TODO: accumulator - loop self.items.values() and add price*qty
        return 0

    def discount(self, coupon, sub):
        # TODO: "SAVE10" -> return sub*0.10
        # TODO: "FLAT100" and sub >= 500 -> return 100
        # TODO: otherwise -> return 0
        return 0

    def bill(self, coupon=None):
        # TODO: sub = self.subtotal(); disc = self.discount(coupon, sub)
        # TODO: taxable = sub - disc; gst = taxable * self.gst_rate
        # TODO: return dict {subtotal, discount, gst, total} (round to 2 dp)
        return {}


if __name__ == "__main__":
    cart = Cart()
    cart.add("Notebook", 60, 3)
    cart.add("Bag", 499)
    print(cart.bill("SAVE10"))
