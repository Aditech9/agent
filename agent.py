import datetime
import math

# -------------------------
# Agent Memory
# -------------------------
memory = []


# -------------------------
# Tools
# -------------------------

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def get_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")


def calculator(expression):
    try:
        result = eval(expression, {"__builtins__": {}}, {"math": math})
        return result
    except:
        return "Invalid calculation"


# -------------------------
# AI Agent
# -------------------------

def ai_agent(user_input):

    text = user_input.lower()

    # Remember user information
    if text.startswith("remember"):
        information = user_input[8:].strip()
        memory.append(information)
        return "Okay, I will remember that."

    # Show memory
    if "what do you remember" in text:
        if memory:
            return "I remember: " + ", ".join(memory)
        else:
            return "I don't remember anything yet."

    # Time tool
    if "time" in text:
        return "Current time is: " + get_time()

    # Date tool
    if "date" in text:
        return "Today's date is: " + get_date()

    # Calculator tool
    if text.startswith("calculate"):
        expression = user_input[9:].strip()
        return "Answer: " + str(calculator(expression))

    # Basic responses
    if "hello" in text or "hi" in text:
        return "Hello! I am your simple AI Agent."

    if "how are you" in text:
        return "I am fine! I am ready to help you."

    if "your name" in text:
        return "My name is Simple AI Agent."

    return "Sorry, I don't understand that yet."


# -------------------------
# Run the Agent
# -------------------------

print("================================")
print("       SIMPLE AI AGENT")
print("================================")
print("Type 'exit' to stop the agent.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    response = ai_agent(user_input)

    print("Agent:", response)
