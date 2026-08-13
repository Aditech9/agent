from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("=================================")
print("       BASIC AI AGENT")
print("=================================")
print("Type 'exit' to stop the agent.\n")

while True:

    # Take input from user
    user_input = input("You: ")

    # Stop the program
    if user_input.lower() == "exit":
        print("AI Agent: Goodbye!")
        break

    try:
        # Send user input to AI model
        response = client.responses.create(
            model="gpt-5-mini",
            instructions="""
            You are a helpful beginner-friendly AI Agent.
            Answer questions clearly and simply.
            If the user asks a programming question,
            explain the answer with simple examples.
            """,
            input=user_input
        )

        # Display AI response
        print("\nAI Agent:", response.output_text)
        print()

    except Exception as e:
        print("Error:", e)