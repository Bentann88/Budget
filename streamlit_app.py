import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Monthly Budget", layout="wide")

# --- Custom CSS for pastel labels, Montserrat font, and consistent layout ---
st.markdown("""
    <style>
        html, body, [class*="css"]  {
            font-family: 'Montserrat', sans-serif;
            background-color: #f5faff;
            color: #000;
        }
        .title-box {
            background-color: #cce5ff;
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
        .metric-box {
            font-size: 18px !important;
            font-weight: 500 !important;
            color: #000 !important;
        }
        .section-box h4 {
            font-size: 22px !important;
            font-weight: 600 !important;
            color: #000 !important;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<div class='title-box'><h2 style='color: #007BFF;'>📊 Monthly Budget Summary</h2></div>", unsafe_allow_html=True)

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
st.markdown("<div class='section-box'><h4> Cash Flow Summary</h4>", unsafe_allow_html=True)
income = st.number_input("Total Income", min_value=0.0, value=4800.0, step=100.0)
bills = st.number_input("Bills", min_value=0.0, value=1200.0, step=50.0)
debt = st.number_input("Debt Payments", min_value=0.0, value=500.0, step=50.0)
savings = st.number_input("Savings", min_value=0.0, value=1000.0, step=50.0)
total_outflow = bills + debt + savings
remaining = income - total_outflow

st.markdown(f"<div class='metric-box'>Remaining<br><span style='font-size:32px;'>${remaining:,.2f}</span></div>", unsafe_allow_html=True)
st.markdown(f"<div class='metric-box'>Total Outflow: ${total_outflow:,.2f}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Detailed Expenses Inputs ---
st.markdown("<div class='section-box'><h4>🗕️ Detailed Expenses</h4>", unsafe_allow_html=True)
expense_data = {
    "Groceries": st.number_input("Groceries", min_value=0.0, value=300.0, step=10.0),
    "Restaurant": st.number_input("Restaurant", min_value=0.0, value=150.0, step=10.0),
    "Pharmacy": st.number_input("Pharmacy", min_value=0.0, value=60.0, step=10.0),
    "Fuel": st.number_input("Fuel", min_value=0.0, value=100.0, step=10.0),
    "Car Maintenance": st.number_input("Car Maintenance", min_value=0.0, value=80.0, step=10.0),
    "Clothing": st.number_input("Clothing", min_value=0.0, value=50.0, step=10.0),
    "Entertainment": st.number_input("Entertainment", min_value=0.0, value=120.0, step=10.0),
    "Health & Medical": st.number_input("Health & Medical", min_value=0.0, value=75.0, step=10.0),
    "Personal Care": st.number_input("Personal Care", min_value=0.0, value=90.0, step=10.0)
}

# Convert to DataFrame for display
expense_df = pd.DataFrame(list(expense_data.items()), columns=["Category", "Amount"])
total_expenses = expense_df["Amount"].sum()
st.dataframe(expense_df.style.format({"Amount": "$ {:.2f}"}))
st.markdown(f"<div class='metric-box'>Total Detailed Expenses: ${total_expenses:,.2f}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Minimal Horizontal Bar Chart for Spending Categories ---
st.markdown("<div class='section-box'><h4> Expense Category Breakdown</h4>", unsafe_allow_html=True)
fig, ax = plt.subplots(figsize=(2, 1))  # Reduced size further
ax.barh(expense_df["Category"], expense_df["Amount"], color="#90caf9")  # pastel blue
ax.set_xlabel("Amount ($)", fontsize=6)
ax.set_yticklabels(expense_df["Category"], fontsize=.25)
ax.tick_params(axis='x', labelsize=5)
ax.tick_params(axis='y', labelsize=5)
ax.set_xticks([])  # Optional: hide x-axis ticks for minimal look
for i, v in enumerate(expense_df["Amount"]):
    ax.text(v + 2, i, f"${v:.0f}", va='center', fontsize=5)
st.pyplot(fig)
st.markdown("</div>", unsafe_allow_html=True)
