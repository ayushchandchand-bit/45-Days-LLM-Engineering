"""
Exercise 3 — Split the bill with tip (solution).

    python split_bill_solution.py
"""

bill = 2400
friends = 5
tip_rate = 0.10          # 10%

tip = bill * tip_rate
total = bill + tip
per_person = total / friends

print("Bill:       ", bill)
print("Tip (10%):  ", tip)
print("Total:      ", total)
print("Per person: ", per_person)
