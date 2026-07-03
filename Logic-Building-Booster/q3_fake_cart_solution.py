"""
Problem 3 - Fake Cart & Bill (SOLUTION).

Run:
    python q3_fake_cart_solution.py

Logic-building note:
  A bill is built in a fixed ORDER - get that order right and the code is easy:
      subtotal  ->  minus discount  ->  plus GST  ->  grand total
  The subtotal is the ACCUMULATOR pattern: walk the cart, add price*qty each time.
  A coupon is just an if-rule that returns a discount amount.
  (Rupees printed as 'Rs.' so it runs on any Windows console.)
"""


class Cart:
    def __init__(self, gst_rate=0.18):
        self.items = {}            # name -> [price, qty]
        self.gst_rate = gst_rate

    def add(self, name, price, qty=1):
        if name in self.items:
            self.items[name][1] += qty        # already there -> bump the quantity
        else:
            self.items[name] = [price, qty]

    def remove(self, name):
        self.items.pop(name, None)            # drop it if present, ignore if not

    def subtotal(self):
        total = 0                             # accumulator
        for price, qty in self.items.values():
            total += price * qty
        return total

    def discount(self, coupon, sub):
        """Return the rupee discount a coupon gives on this subtotal."""
        if coupon == "SAVE10":
            return sub * 0.10                 # 10% off, no minimum
        if coupon == "FLAT100" and sub >= 500:
            return 100                        # flat Rs.100, only if you spend Rs.500+
        return 0                              # unknown / not eligible

    def bill(self, coupon=None):
        sub = self.subtotal()
        disc = self.discount(coupon, sub)
        taxable = sub - disc
        gst = taxable * self.gst_rate
        total = taxable + gst
        return {
            "subtotal": round(sub, 2),
            "discount": round(disc, 2),
            "gst": round(gst, 2),
            "total": round(total, 2),
        }


def print_bill(cart, coupon=None):
    b = cart.bill(coupon)
    print(f"  Subtotal : Rs.{b['subtotal']:.2f}")
    print(f"  Discount : Rs.{b['discount']:.2f}  ({coupon or 'none'})")
    print(f"  GST 18%  : Rs.{b['gst']:.2f}")
    print(f"  TOTAL    : Rs.{b['total']:.2f}")


if __name__ == "__main__":
    cart = Cart()
    cart.add("Notebook", 60, 3)      # 180
    cart.add("Pen", 10, 5)           # 50
    cart.add("Bag", 499)             # 499  -> subtotal 729
    cart.add("Pen", 10, 5)           # same item again: qty becomes 10 -> +50 more

    print("Without coupon:")
    print_bill(cart)

    print("\nWith SAVE10:")
    print_bill(cart, "SAVE10")

    print("\nWith FLAT100:")
    print_bill(cart, "FLAT100")
