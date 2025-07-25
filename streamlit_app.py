import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Monthly Budget", layout="wide")

# --- Custom CSS for color styling and Montserrat font ---
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Montserrat', sans-serif;
            background-color: #f5faff;
        }
        .title-box {
            background-color: #ffccd5;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .section-box {
            background-color: #e0f7fa;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<div class='title-box'><h2 style='color: #333;'>📊 Monthly Budget Summary</h2></div>", unsafe_allow_html=True)

# --- Month / Country Info ---
with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        month = st.selectbox("Month", ["January", "February", "March"])
    with col2:
        year = st.selectbox("Year", [2023, 2024, 2025])
    with col3:
        country = st.selectbox("Country", ["United States", "Canada", "UK"])

# --- Cash Flow Summary ---
st.markdown("<div class='section-box'><h4>💵 Cash Flow Summary</h4>", unsafe_allow_html=True)
income = st.number_input("Total Income", min_value=0.0, value=4800.0, step=100.0)
bills = st.number_input("Bills", min_value=0.0, value=1200.0, step=50.0)
debt = st.number_input("Debt Payments", min_value=0.0, value=500.0, step=50.0)
savings = st.number_input("Savings", min_value=0.0, value=1000.0, step=50.0)
remaining = income - bills - debt - savings

st.metric("Remaining", f"${remaining:,.2f}")
st.markdown("</div>", unsafe_allow_html=True)

# --- Expenses Table ---
st.markdown("<div class='section-box'><h4>🧾 Expenses</h4>", unsafe_allow_html=True)
expense_data = pd.DataFrame({
    "Category": ["Groceries", "Pharmacy", "Fuel", "Entertainment"],
    "Projected": [300, 100, 150, 80],
    "Actual": [290, 90, 160, 100]
})
expense_data["Difference"] = expense_data["Projected"] - expense_data["Actual"]
st.dataframe(expense_data.style.format({"Projected": "$ {:.2f}", "Actual": "$ {:.2f}", "Difference": "$ {:.2f}"}))
st.markdown("</div>", unsafe_allow_html=True)
