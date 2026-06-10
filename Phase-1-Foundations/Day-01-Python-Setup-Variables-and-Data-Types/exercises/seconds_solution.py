"""
Exercise 2 — Seconds in a day / week / year (solution).

    python seconds_solution.py
"""

seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24

seconds_per_day = seconds_per_minute * minutes_per_hour * hours_per_day
seconds_per_week = seconds_per_day * 7
seconds_per_year = seconds_per_day * 365

print("Seconds in a day: ", seconds_per_day)
print("Seconds in a week:", seconds_per_week)
print("Seconds in a year:", seconds_per_year)
