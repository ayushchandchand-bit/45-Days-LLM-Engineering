"""
Exercise 1 - BMI Calculator (web edition).   [STUDENT STUB]

Turn the Day 1 terminal BMI calculator into a Streamlit web app.

Run it:
    streamlit run bmi_web.py
"""

import streamlit as st

# TODO 1: give the app a title with st.title(...)

# TODO 2: get weight in kg from the user.
#         Hint: weight = st.number_input("Weight (kg)", min_value=1.0, value=60.0)

# TODO 3: get height in cm from the user (another st.number_input).

# TODO 4: convert height from cm to metres, then compute
#         bmi = weight / (height_m ** 2)

# TODO 5: show the BMI with st.metric("BMI", round(bmi, 1))

# TODO 6: show the category using the right coloured box:
#         < 18.5      -> st.info("Underweight")
#         18.5 - 24.9 -> st.success("Normal")
#         25 - 29.9   -> st.warning("Overweight")
#         >= 30       -> st.error("Obese")
