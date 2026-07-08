"""
Exercise 1 - BMI Calculator (web edition).   [SOLUTION]

Run it:
    streamlit run bmi_web_solution.py
"""

import streamlit as st

# App heading.
st.title("BMI Calculator")
st.caption("Enter your weight and height to get your Body Mass Index.")

# Put the two inputs side by side using columns.
left, right = st.columns(2)

with left:
    # Weight in kilograms. `value` is the starting default.
    weight = st.number_input("Weight (kg)", min_value=1.0, value=60.0, step=0.5)

with right:
    # Height in centimetres.
    height_cm = st.number_input("Height (cm)", min_value=30.0, value=165.0, step=1.0)

# Convert height to metres, because BMI uses metres.
height_m = height_cm / 100

# BMI formula: weight in kg divided by height in metres squared.
bmi = weight / (height_m ** 2)

# Show the number prominently.
st.metric("Your BMI", round(bmi, 1))

# Show the category with a colour that matches its severity.
if bmi < 18.5:
    st.info("Category: Underweight")
elif bmi < 25:
    st.success("Category: Normal")
elif bmi < 30:
    st.warning("Category: Overweight")
else:
    st.error("Category: Obese")

st.caption("BMI is a rough screening number, not a medical diagnosis.")
