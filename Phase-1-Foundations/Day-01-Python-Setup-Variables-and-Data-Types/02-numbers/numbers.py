"""
Integers and floats — Python's two everyday number types.

Run:
    python numbers.py
"""

# ----- Integers (int): whole numbers -----
print("an integer:", 42)
print("a negative integer:", -7)

# type() tells you what kind of value something is.
print("type of 42 ->", type(42))

# ----- Floats: numbers with a decimal point -----
print("a float:", 3.14)
print("type of 3.14 ->", type(3.14))

# ----- Division always gives a float -----
print("4 / 2 =", 4 / 2)          # 2.0  (note the .0 — it's a float!)
print("type of 4 / 2 ->", type(4 / 2))

# ----- Floats can be slightly imprecise (this is normal everywhere) -----
print("0.1 + 0.2 =", 0.1 + 0.2)  # 0.30000000000000004

# ----- Big integers: Python handles huge numbers natively -----
print("2 ** 100 =", 2 ** 100)

# ----- Numeric notations -----
print("underscores:", 1_000_000)  # 1000000  (underscores are ignored, just for readability)
print("hexadecimal 0xFF:", 0xFF)  # 255
print("binary 0b1010:", 0b1010)   # 10
print("scientific 1e3:", 1e3)     # 1000.0  (e-notation makes a float)
