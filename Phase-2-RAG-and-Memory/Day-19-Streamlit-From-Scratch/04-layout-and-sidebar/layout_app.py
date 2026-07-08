"""
Day 19 - Step 4: Arranging the page - sidebar, columns, tabs, expanders.

Run it:
    streamlit run layout_app.py
"""

import streamlit as st

st.title("Laying out a page")

# --- Sidebar -----------------------------------------------------------------
# Anything attached to `st.sidebar` appears in the left panel. This is where
# settings live in a real app. These widgets return values just like normal ones.
st.sidebar.header("Settings")
model = st.sidebar.selectbox("Model", ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.2, 0.05)
show_debug = st.sidebar.checkbox("Show debug info")

# Read the sidebar values in the main area.
st.write(f"You picked **{model}** at temperature **{temperature}**.")

st.divider()

# --- Columns: things side by side --------------------------------------------
st.header("Columns put things side by side")

# `st.columns(3)` returns three column objects.
col1, col2, col3 = st.columns(3)

# Write into a column using a `with` block.
with col1:
    st.metric("Users", 1280, "+120")
with col2:
    st.metric("Active today", 342, "-8")
with col3:
    st.metric("Signups", 57, "+15")

st.divider()

# --- Tabs: switchable sections -----------------------------------------------
st.header("Tabs act like mini pages")

# `st.tabs` returns one object per tab label.
tab_summary, tab_details = st.tabs(["Summary", "Details"])

with tab_summary:
    st.write("This is the summary tab. Keep the headline here.")
with tab_details:
    st.write("This is the details tab. Put the deep dive here.")

st.divider()

# --- Expander: hide long content ---------------------------------------------
st.header("Expanders hide long or optional content")

# Everything inside the expander is collapsed until the user clicks it open.
with st.expander("Click to see the system prompt we would send"):
    st.code(
        "You are a helpful assistant. Answer clearly and concisely.",
        language="text",
    )

# Use the sidebar checkbox to conditionally show debug info - a very common pattern.
if show_debug:
    st.warning("Debug mode is ON")
    st.json({"model": model, "temperature": temperature})
