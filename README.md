# Simple AI Agent

## 📌 Project Overview

This project is a **simple Python-based AI Agent** designed for beginners. The agent can understand basic user commands and perform simple actions such as:

* Saying Hello
* Displaying the current date
* Exiting the program

The project demonstrates the basic concept of an **AI Agent using Python conditions and functions**.

---

## 🎯 Objectives

The main objectives of this project are:

1. To understand the basic concept of an AI Agent.
2. To learn how Python functions work.
3. To use `if-elif-else` statements for decision-making.
4. To use Python's `datetime` module.
5. To create an interactive command-line agent.

---

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Module:** `datetime`
* **Interface:** Command Line / Terminal

---

## 📂 Project Structure

```text
Simple-AI-Agent/
│
├── ai_agent.py
└── README.md
```

---

## 💻 Code

```python
import datetime

def ai_agent():
    print("Hello! I am your simple AI Agent.")

    while True:
        user = input("\nYou: ").lower()

        if user == "hello" or user == "hi":
            print("Agent: Hello! How can I help you?")

        elif user == "date":
            date = datetime.datetime.now().strftime("%d-%m-%Y")
            print("Agent: Today's date is", date)

        elif user == "exit":
            print("Agent: Goodbye!")
            break

        else:
            print("Agent: I don't understand.")

ai_agent()
```

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check Python using:

```bash
python --version
```

### Step 2: Create the Python File

Create a file named:

```text
ai_agent.py
```

Copy the Python code into the file.

### Step 3: Run the Program

Open the terminal in the project folder and run:

```bash
python ai_agent.py
```

---

## 🧪 Example

```text
Hello! I am your simple AI Agent.

You: hello
Agent: Hello! How can I help you?

You: date
Agent: Today's date is 18-08-2026

You: exit
Agent: Goodbye!
```

---

## ⚙️ How the Agent Works

The agent continuously takes input from the user.

### 1. Hello Command

If the user enters:

```text
hello
```

or

```text
hi
```

the agent responds with a greeting.

### 2. Date Command

If the user enters:

```text
date
```

the agent uses the `datetime` module to display the current date.

### 3. Exit Command

If the user enters:

```text
exit
```

the agent stops running.

### 4. Unknown Command

For any other input, the agent responds:

```text
Agent: I don't understand.
```

---

## 🧠 AI Agent Concepts Used

| Concept         | Implementation |
| --------------- | -------------- |
| Input           | `input()`      |
| Decision Making | `if-elif-else` |
| Function        | `ai_agent()`   |
| Loop            | `while True`   |
| Tool/Module     | `datetime`     |
| Exit Condition  | `break`        |

---

## 🚀 Future Improvements

This basic agent can be improved by adding:

* Calculator functionality
* Time functionality
* Memory
* More commands
* Natural language processing
* Voice input/output
* An LLM such as an AI API
* Multiple tools

---

## 📚 Learning Outcome

After completing this project, a beginner can understand:

* Python functions
* Loops
* Conditional statements
* User input
* Python modules
* Basic AI Agent architecture

---

## 👨‍💻 Author

**Aditya Patil**

Engineering – Artificial Intelligence & Machine Learning

---

## 📄 License

This project is created for **educational and college project purposes**.
