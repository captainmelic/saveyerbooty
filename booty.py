import os
import streamlit as st
from groqpolly import callPolly

# Title of the app
st.title("Expense and Profit Tracker")

#Polly chat
st.header("Say hi to Polly!")

# Start displaying the text

#position chat box
st.markdown("""
    <style>
    .chatbox {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 300px;
        height: 400px;
        background-color: white;
        border: 1px solid #ccc;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        padding: 10px;
        overflow-y: auto;  /* Allow scrolling if content exceeds height */
        z-index: 1000;
    }
    </style>
""", unsafe_allow_html=True)

# Chatbox container
chatbox_container = st.container()
with chatbox_container:
    st.markdown('<div class="chatbox">', unsafe_allow_html=True)
    st.subheader("Chatbot")
    chat_display = st.empty()  # Placeholder for chatbot messages
    st.markdown('</div>', unsafe_allow_html=True)

if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Sidebar for user input
user_input = st.sidebar.text_input("You:", "")

# Handle user input
if user_input:
    # Add user input to the conversation history
    st.session_state.conversation.append(f"You: {user_input}")
    
    # Generate and add chatbot response
    response = callPolly(user_input)
    st.session_state.conversation.append(f"Polly: {response}")

    # Clear the input box
    st.sidebar.text_input("You:", "", key="input")  # Reset input field

# Display the conversation history
chat_display.markdown("\n".join(st.session_state.conversation))


# Start displaying the text
# initialText = "Hello Polly! I am the Captain and I am in need of some assistance with me treasure."

# with st.sidebar:
#     st.subheader("Polly")
#     chat_display = st.empty()

# outputText = ""
# for chunk in callPolly(initialText):
#     outputText += chunk.choices[0].delta.content or ""
#     chat_display.markdown(f"<pre>{outputText}</pre>", unsafe_allow_html=True)

# while True:
#     user_input = st.text_input("Enter your message to Polly:")

#     outputText = ""
#     for chunk in callPolly(user_input):
#         outputText += chunk.choices[0].delta.content or ""
#         chat_display.markdown(f"<pre>{outputText}</pre>", unsafe_allow_html=True)

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

