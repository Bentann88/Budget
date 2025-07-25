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

# --- Income & Savings ---
st.markdown("<div class='section-box'><h4>💵 Income & Savings</h4>", unsafe_allow_html=True)
income = st.number_input("Total Income", min_value=0.0, value=4800.0, step=100.0)
savings = st.number_input("Savings", min_value=0.0, value=1000.0, step=50.0)
st.markdown("</div>", unsafe_allow_html=True)

# --- Bills Section ---
st.markdown("<div class='section-box'><h4>📑 Fixed Bills</h4>", unsafe_allow_html=True)
bills_data = {
    "Rent/Mortgage": st.number_input("Rent/Mortgage", min_value=0.0, value=1000.0, step=50.0),
    "Utilities": st.number_input("Utilities", min_value=0.0, value=200.0, step=25.0),
    "Internet": st.number_input("Internet", min_value=0.0, value=60.0, step=10.0),
    "Insurance": st.number_input("Insurance", min_value=0.0, value=150.0, step=25.0),
    "Phone Bill": st.number_input("Phone Bill", min_value=0.0, value=50.0, step=10.0)
}
bills_df = pd.DataFrame(list(bills_data.items()), columns=["Bill", "Amount"])
total_bills = bills_df["Amount"].sum()
st.dataframe(bills_df.style.format({"Amount": "$ {:.2f}"}))
st.markdown(f"<div class='metric-box'>Total Bills: ${total_bills:,.2f}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Debt ---
debt = st.number_input("Debt Payments", min_value=0.0, value=500.0, step=50.0)

# --- Detailed Spending (Discretionary) ---
st.markdown("<div class='section-box'><h4>🛍️ Discretionary Spending</h4>", unsafe_allow_html=True)
spending_data = {
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
spending_df = pd.DataFrame(list(spending_data.items()), columns=["Category", "Amount"])
total_spending = spending_df["Amount"].sum()
st.dataframe(spending_df.style.format({"Amount": "$ {:.2f}"}))
st.markdown(f"<div class='metric-box'>Total Discretionary Spending: ${total_spending:,.2f}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Cash Flow Summary ---
st.markdown("<div class='section-box'><h4>📈 Cash Flow Summary</h4>", unsafe_allow_html=True)
total_outflow = total_bills + total_spending + debt + savings
remaining = income - total_outflow
savings_rate = (savings / income * 100) if income > 0 else 0

st.markdown(f"<div class='metric-box'>Remaining<br><span style='font-size:32px;'>${remaining:,.2f}</span></div>", unsafe_allow_html=True)
st.markdown(f"<div class='metric-box'>Total Outflow: ${total_outflow:,.2f}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='metric-box'>Savings Rate: {savings_rate:.1f}%</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# --- Pie Chart Breakdown ---
st.markdown("<div class='section-box'><h4>📊 Allocation of Income</h4>", unsafe_allow_html=True)
labels = ['Savings', 'Bills', 'Discretionary']
values = [savings, total_bills, total_spending]
colors = ['#A5D8FF', '#74C0FC', '#4DABF7']
fig2, ax2 = plt.subplots(figsize=(.5, .5))
ax2.pie(values, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%', textprops={'fontsize': 6})
ax2.axis('equal')
st.pyplot(fig2)
st.markdown("</div>", unsafe_allow_html=True)

# --- Optional Export Button ---
st.download_button(
    label="📥 Download Budget Summary",
    data=spending_df.to_csv(index=False),
    file_name=f"budget_summary_{month}.csv",
    mime="text/csv"
)
