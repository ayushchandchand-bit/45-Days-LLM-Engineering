"""
Lists — ordered, changeable collections. The everyday container.

Run:
    python lists.py
"""

# =====================================================================
# 1) Create, index, slice (indexing rules match Day-2 strings)
# =====================================================================
cart = ["milk", "bread", "eggs"]
print("cart        :", cart)
print("first item  :", cart[0])      # milk   (index from 0)
print("last item   :", cart[-1])     # eggs   (negative = from the end)
print("length      :", len(cart))
print("slice [0:2] :", cart[0:2])    # ['milk', 'bread']  (stop is exclusive)
print("'milk' in?  :", "milk" in cart)
print()

# =====================================================================
# 2) Mutating: lists change IN PLACE (strings can't do this!)
# =====================================================================
cart[0] = "coffee"                   # replace by index
print("after cart[0] = 'coffee':", cart)

cart.append("rice")                  # add ONE to the end
cart.insert(0, "tea")                # squeeze ONE in at index 0
print("after append + insert     :", cart)

cart.extend(["jam", "oil"])          # add ALL items of another list
print("after extend              :", cart)

# CONTRAST: append(other_list) NESTS it instead of merging — a common bug:
demo = [1, 2]
demo.append([3, 4])                  # -> [1, 2, [3, 4]]  (nested!)
print("append(list) nests   :", demo)
demo = [1, 2]
demo.extend([3, 4])                  # -> [1, 2, 3, 4]    (merged)
print("extend(list) merges  :", demo)
print()

# =====================================================================
# 3) Removing items: pop (by index, RETURNS it) vs remove (by value)
# =====================================================================
last = cart.pop()                    # remove & RETURN the last item
print("popped off the end   :", last)
cart.remove("tea")                   # remove the first matching VALUE
print("after remove('tea')  :", cart)
print()

# =====================================================================
# 4) THE GOTCHA: mutating methods return None
# =====================================================================
result = cart.append("sugar")        # append changes cart, returns None
print("append's return value:", result)   # None  <- not the new list!
print("cart is still updated :", cart)
print()

# =====================================================================
# 5) REAL USE: a print queue / waiting line (FIFO)
# =====================================================================
print_queue = []
print_queue.append("report.pdf")     # jobs arrive at the back
print_queue.append("invoice.pdf")
print_queue.append("photo.png")
print(f"{len(print_queue)} jobs waiting.")
while print_queue:                    # drain it front-to-back (Day 4!)
    job = print_queue.pop(0)          # pop(0) = take from the FRONT
    print(f"  printing {job} ... ({len(print_queue)} left)")
