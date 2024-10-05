import os
import streamlit as st
from groqpolly import callPolly

# Title of the app
st.title("Expense and Profit Tracker")

#Polly chat
st.header("Say hi to Polly!")

# Start displaying the text


initialText = "Hello Polly! I am the Captain and I am in need of some assistance with me treasure."

with st.sidebar:
    st.subheader("Polly")
    chat_display = st.empty()

outputText = ""
for chunk in callPolly(initialText):
    outputText += chunk.choices[0].delta.content or ""
    chat_display.markdown(f"<pre>{outputText}</pre>", unsafe_allow_html=True)

user_input = st.text_input("Enter your message to Polly:")

outputText = ""
for chunk in callPolly(user_input):
    outputText += chunk.choices[0].delta.content or ""
    chat_display.markdown(f"<pre>{outputText}</pre>", unsafe_allow_html=True)

# Input for income
st.header("Income")
income = st.number_input("Enter your total income ($)", min_value=0.0, step=100.0)

# Input for expenses
st.header("Expenses")
expenses = {}
num_expenses = st.number_input("How many different expenses do you have?", min_value=0, step=1)

for i in range(num_expenses):
    expense_name = st.text_input(f"Expense #{i + 1} Name", "")
    expense_amount = st.number_input(f"Expense #{i + 1} Amount ($)", min_value=0.0, step=1.0)
    expenses[expense_name] = expense_amount

# Calculate total expenses
total_expenses = sum(expenses.values())

# Calculate profit
profit = income - total_expenses

# Display results
if st.button("Calculate Profit"):
    st.success(f"Total Income: ${income:.2f}")
    st.success(f"Total Expenses: ${total_expenses:.2f}")
    st.success(f"Profit: ${profit:.2f}")

    # Optionally, display a detailed breakdown of expenses
    st.write("### Expense Breakdown:")
    for name, amount in expenses.items():
        st.write(f"{name}: ${amount:.2f}")

# Optional: Add a reset button
if st.button("Reset"):
    st.experimental_rerun()

