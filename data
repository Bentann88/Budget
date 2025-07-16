import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Budget Dashboard", layout="centered")

st.title("📊 Personal Budget & Net Worth Tracker")
st.markdown("Enter your financial details below. Your summary and charts will update automatically.")

# --- Input Sections ---
st.header("Monthly Details")
month = st.selectbox("Select Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

data_key = f"data_{month}"

if data_key not in st.session_state:
    st.session_state[data_key] = {}

income = st.number_input("Monthly Income", min_value=0.0, value=5000.0, step=100.0, key=f"income_{month}")
expenses = st.number_input("Total Monthly Expenses", min_value=0.0, value=2500.0, step=100.0, key=f"expenses_{month}")
savings = st.number_input("Monthly Savings", min_value=0.0, value=500.0, step=100.0, key=f"savings_{month}")
investments = st.number_input("Total Investment Value", min_value=0.0, value=10000.0, step=500.0, key=f"investments_{month}")
net_worth = st.number_input("Total Net Worth", min_value=0.0, value=15000.0, step=500.0, key=f"networth_{month}")
debt = st.number_input("Total Debt", min_value=0.0, value=3000.0, step=100.0, key=f"debt_{month}")

# --- Calculations ---
left_to_budget = income - expenses - savings

# Store in session state
st.session_state[data_key] = {
    "Month": month,
    "Income": income,
    "Expenses": expenses,
    "Savings": savings,
    "Investments": investments,
    "Net Worth": net_worth,
    "Debt": debt,
    "Left to Budget": left_to_budget
}

# --- Summary Section ---
st.markdown("---")
st.subheader("📈 Summary")
st.metric(label="Left to Budget", value=f"${left_to_budget:,.2f}")
st.metric(label="Net Worth", value=f"${net_worth:,.2f}")
st.metric(label="Total Investments", value=f"${investments:,.2f}")
st.metric(label="Total Debt", value=f"${debt:,.2f}")

# --- Chart Section ---
st.markdown("---")
st.subheader("📊 Visual Breakdown")
chart_data = pd.DataFrame({
    "Category": ["Income", "Expenses", "Savings", "Debt"],
    "Amount": [income, expenses, savings, debt]
})

fig, ax = plt.subplots()
ax.pie(chart_data["Amount"], labels=chart_data["Category"], autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

# --- Historical View ---
st.markdown("---")
st.subheader("🕒 Monthly History")
all_data = [v for k, v in st.session_state.items() if k.startswith("data_")]
history_df = pd.DataFrame(all_data)

if not history_df.empty:
    st.dataframe(history_df.set_index("Month"))

# --- Export Option ---
st.markdown("---")
st.subheader("📤 Export Current Month")
data = {
    "Category": ["Income", "Expenses", "Savings", "Investments", "Net Worth", "Debt"],
    "Amount": [income, expenses, savings, investments, net_worth, debt]
}
df = pd.DataFrame(data)

csv = df.to_csv(index=False).encode('utf-8')
st.download_button(label="Download Summary as CSV", data=csv, file_name=f"budget_summary_{month}.csv", mime='text/csv')
