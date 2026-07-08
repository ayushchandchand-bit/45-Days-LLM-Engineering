"""
Day 19 - Step 2: Every common way to put content on a Streamlit page.

Run it:
    streamlit run display_app.py
"""

# `st` is Streamlit; `pd` is pandas, which Streamlit uses to render tables.
import streamlit as st
import pandas as pd

# A page heading for this demo.
st.title("Ways to show content")

# --- Text --------------------------------------------------------------------
st.header("1. Text")

# `st.write` is the do-everything function: give it a string, it prints a string.
st.write("st.write prints plain text and understands **Markdown** too.")

# `st.markdown` is explicitly for Markdown - headings, bold, lists, links.
st.markdown("- bullet one\n- bullet two\n- **bold** and *italic* and `inline code`")

# `st.text` prints fixed-width text and does NOT interpret Markdown.
st.text("st.text keeps text exactly as-is (no bold, no links).")

# `st.code` shows a syntax-highlighted block with a one-click copy button.
st.code("def greet(name):\n    return f'Hi {name}'", language="python")

st.divider()  # a horizontal rule between sections

# --- Data --------------------------------------------------------------------
st.header("2. Data and tables")

# Build a small pandas DataFrame - think of it as a spreadsheet in code.
students = pd.DataFrame(
    {
        "Name": ["Aisha", "Rohan", "Meera", "Karan"],
        "City": ["Delhi", "Pune", "Chennai", "Jaipur"],
        "Score": [88, 74, 91, 66],
    }
)

# `st.dataframe` renders an interactive table (sortable, scrollable).
st.write("An interactive table (click a column header to sort):")
# width="stretch" makes the table fill the available page width.
st.dataframe(students, width="stretch")

# `st.json` shows any dict/list as a collapsible JSON tree.
st.write("The same idea as raw JSON:")
st.json({"top_student": "Meera", "count": len(students)})

st.divider()

# --- Metrics -----------------------------------------------------------------
st.header("3. Metrics (KPI numbers)")

# `st.metric` shows one big number, optionally with a delta (change) arrow.
st.metric(label="Average score", value=f"{students['Score'].mean():.1f}", delta="+3.2")

st.divider()

# --- Status boxes ------------------------------------------------------------
st.header("4. Status messages")

# Four coloured boxes for giving the user feedback.
st.success("Green: something worked.")
st.info("Blue: neutral information.")
st.warning("Yellow: heads up, be careful.")
st.error("Red: something went wrong.")
