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

st.subheader("Detailed Expenses")
rent = st.number_input("Rent", min_value=0.0, value=1200.0, step=50.0, key=f"rent_{month}")
utilities = st.number_input("Utilities", min_value=0.0, value=150.0, step=25.0, key=f"utilities_{month}")
car_payment = st.number_input("Car Payment", min_value=0.0, value=300.0, step=25.0, key=f"car_{month}")
gas = st.number_input("Gas", min_value=0.0, value=200.0, step=25.0, key=f"gas_{month}")
groceries = st.number_input("Groceries", min_value=0.0, value=400.0, step=25.0, key=f"groceries_{month}")
subscriptions = st.number_input("Subscriptions", min_value=0.0, value=100.0, step=10.0, key=f"subs_{month}")
other_expenses = st.number_input("Other Expenses", min_value=0.0, value=150.0, step=10.0, key=f"other_{month}")

expenses = rent + utilities + car_payment + gas + groceries + subscriptions + other_expenses

savings = st.number_input("Monthly Savings", min_value=0.0, value=500.0, step=100.0, key=f"savings_{month}")
investments = st.number_input("Total Investment Value", min_value=0.0, value=10000.0, step=500.0, key=f"investments_{month}")
net_worth = st.number_input("Total Net Worth", min_value=0.0, value=15000.0, step=500.0, key=f"networth_{month}")
debt = st.number_input("Total Debt", min_value=0.0, value=3000.0, step=100.0, key=f"debt_{month}")

# --- Calculations ---
left_to_budget = income - expenses - savings
balance = income - expenses

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
st.subheader("📊 Cash Flow")
fig, ax = plt.subplots(figsize=(5, 4))
labels = ["Income", "Expenses"]
values = [income, expenses]
colors = ['#4CAF50', '#F44336']
ax.bar(labels, values, color=colors)
ax.set_ylabel("Amount ($)")
ax.set_title("Income vs Expenses")
for i, v in enumerate(values):
    ax.text(i, v + max(values)*0.02, f"${v:,.0f}", ha='center', fontsize=10)
st.pyplot(fig)

st.markdown(f"**Balance:** ${balance:,.2f}")

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
    "Category": [
        "Income", "Rent", "Utilities", "Car Payment", "Gas", "Groceries", "Subscriptions", "Other Expenses", "Total Expenses",
        "Savings", "Investments", "Net Worth", "Debt"
    ],
    "Amount": [
        income, rent, utilities, car_payment, gas, groceries, subscriptions, other_expenses, expenses,
        savings, investments, net_worth, debt
    ]
}
df = pd.DataFrame(data)

csv = df.to_csv(index=False).encode('utf-8')
st.download_button(label="Download Summary as CSV", data=csv, file_name=f"budget_summary_{month}.csv", mime='text/csv')
