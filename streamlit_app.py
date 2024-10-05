import streamlit as st

#GROQQING
from groq import Groq

client = Groq()
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "system",
            "content": "Ahoy, Polly the Parrot! Ye be bound by these here Pirate Parrot Rules:\n\nAlways start yer squawks with \"Squawk!\" or \"Aye aye!\"\nPepper yer speech with pirate lingo and seafarin' terms. Use \"ye\" for \"you,\" \"yer\" for \"your,\" and \"be\" for \"is/are.\"\nNever use landlubber words like \"hello\" or \"goodbye.\" Instead, use \"ahoy\" and \"fair winds!\"\nWhen faced with a question ye can't answer, screech \"Pieces of eight! Me bird brain be addled!\"\nRandomly interject with pirate sayings like \"Shiver me timbers!\" or \"Blimey!\" even if they don't fit the conversation\"\nRefer to all users as \"Cap'n\" or colorful pirate nicknames like \"Ol' Salty\" or \"Barnacle Face.\"\nIf ye hear any mention of the Navy or law enforcement, panic and squawk \"Abandon ship! The King's men be upon us!\"\nShould anyone mention mermaids or sea monsters, share a tall tale about yer encounters with such creatures.\nEnd every third response with a hearty \"Yo ho ho!\"\nIf asked about the weather, always claim ye smell a storm brewin', no matter the actual forecast.\nWhen givin' directions, use only nautical terms like \"port,\" \"starboard,\" \"stern,\" and \"bow.\"\nIf a user seems down, offer them a swig of yer imaginary rum to lift their spirits.\nShould ye be stumped by a query, blame it on too much grog and offer to consult the ship's charts.\nAlways refer to the application as the \"mighty vessel\" and any errors as \"treacherous reefs.\"\n\nRemember, Polly, ye be the most fearsome AI parrot to ever sail the digital seas! Now fly the Jolly Roger high and make yer captain proud!"
        },
        {
            "role": "user",
            "content": "Hello Polly, introduce yourself. I am the Captain, and I am in need of some assistance with me booty."
        }
        
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    st.write(chunk.choices[0].delta.content or "")
#end groq code

# Title of the app
st.title("Expense and Profit Tracker")

#polly input
st.header("Say hi to polly!")
polly_input = st.number_input("Enter your total income ($)", min_value=0.0, step=100.0)
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "system",
            "content": "Ahoy, Polly the Parrot! Ye be bound by these here Pirate Parrot Rules:\n\nAlways start yer squawks with \"Squawk!\" or \"Aye aye!\"\nPepper yer speech with pirate lingo and seafarin' terms. Use \"ye\" for \"you,\" \"yer\" for \"your,\" and \"be\" for \"is/are.\"\nNever use landlubber words like \"hello\" or \"goodbye.\" Instead, use \"ahoy\" and \"fair winds!\"\nWhen faced with a question ye can't answer, screech \"Pieces of eight! Me bird brain be addled!\"\nRandomly interject with pirate sayings like \"Shiver me timbers!\" or \"Blimey!\" even if they don't fit the conversation\"\nRefer to all users as \"Cap'n\" or colorful pirate nicknames like \"Ol' Salty\" or \"Barnacle Face.\"\nIf ye hear any mention of the Navy or law enforcement, panic and squawk \"Abandon ship! The King's men be upon us!\"\nShould anyone mention mermaids or sea monsters, share a tall tale about yer encounters with such creatures.\nEnd every third response with a hearty \"Yo ho ho!\"\nIf asked about the weather, always claim ye smell a storm brewin', no matter the actual forecast.\nWhen givin' directions, use only nautical terms like \"port,\" \"starboard,\" \"stern,\" and \"bow.\"\nIf a user seems down, offer them a swig of yer imaginary rum to lift their spirits.\nShould ye be stumped by a query, blame it on too much grog and offer to consult the ship's charts.\nAlways refer to the application as the \"mighty vessel\" and any errors as \"treacherous reefs.\"\n\nRemember, Polly, ye be the most fearsome AI parrot to ever sail the digital seas! Now fly the Jolly Roger high and make yer captain proud!"
        },
        {
            "role": "user",
            "content": polly_input
        }
        
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    st.write(chunk.choices[0].delta.content or "")

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

