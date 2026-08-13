# agent
AI agent using python
# 🤖 Basic AI Agent using Python and OpenAI API

## 📌 Project Overview

This project is a basic **AI Agent** developed using **Python** and the **OpenAI API**.

The purpose of this project is to understand the basic working of an AI Agent and demonstrate how an AI model can be integrated into a Python application.

The agent accepts questions or instructions from the user, sends them to an OpenAI AI model, and displays the generated response.

This project is developed as part of the **AI-Augmented Workflow** course.

---

## 🎯 Objectives

The main objectives of this project are:

* To understand the concept of an AI Agent.
* To integrate an AI model with a Python application.
* To learn how to use the OpenAI API.
* To understand API-based AI applications.
* To practice AI-assisted software development.
* To create a simple interactive AI Agent.
* To understand secure handling of API keys.
* To provide a foundation for developing more advanced AI Agents.

---

## 🏗️ System Architecture

The basic architecture of the AI Agent is:

```text
                USER
                  |
                  v
          Python Application
                  |
                  v
            AI Agent Logic
                  |
                  v
             OpenAI API
                  |
                  v
              AI Model
                  |
                  v
            AI Response
                  |
                  v
                USER
```

### Workflow

1. The user enters a question or instruction.
2. The Python application receives the input.
3. The AI Agent sends the input to the OpenAI API.
4. The OpenAI model processes the request.
5. The generated response is returned to the Python application.
6. The response is displayed to the user.
7. The agent continues accepting input until the user types `exit`.

---

## 🛠️ Technology Stack

| Technology        | Purpose                       |
| ----------------- | ----------------------------- |
| Python            | Main programming language     |
| OpenAI API        | AI model integration          |
| OpenAI Python SDK | Communication with OpenAI API |
| python-dotenv     | Loading environment variables |
| `.env`            | Secure API key configuration  |
| Git/GitHub        | Version control               |
| Markdown          | Project documentation         |

---

## 📁 Project Structure

```text
AI-Agent-Project/
│
├── agent.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
└── ADR-001-Tech-Stack.md
```

### File Description

**`agent.py`**

Contains the main Python code for the AI Agent.

**`.env`**

Stores the OpenAI API key securely.

**`.gitignore`**

Prevents sensitive files such as `.env` and Python environment files from being uploaded to GitHub.

**`requirements.txt`**

Contains the Python packages required by the project.

**`README.md`**

Contains project documentation and instructions.

**`ADR-001-Tech-Stack.md`**

Contains the Architecture Decision Record explaining why Python and the OpenAI API were selected.

---

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3 installed.
* An OpenAI API key.
* Internet connection.
* Terminal / Command Prompt / Anaconda Prompt.
* Required Python packages installed.

---

## 🚀 Installation

### Step 1: Clone or download the project

Download the project to your computer and open the project folder in a terminal.

### Step 2: Create a virtual environment

Run:

```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment

For Windows:

```bash
.venv\Scripts\activate
```

### Step 4: Install required packages

Run:

```bash
pip install openai python-dotenv
```

Or install from the requirements file:

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Configuration

Create a file named:

```text
.env
```

Inside the file, add:

```text
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

### ⚠️ Security Warning

Never share your API key publicly.

Do not upload the `.env` file to GitHub.

The `.gitignore` file should contain:

```text
.env
.venv/
__pycache__/
```

---

## ▶️ Running the AI Agent

After activating the virtual environment, run:

```bash
python agent.py
```

The program will display:

```text
=================================
       BASIC AI AGENT
=================================
Type 'exit' to stop the agent.

You:
```

Enter a question or instruction.

For example:

```text
You: What is Python?
```

The AI Agent will generate a response.

---

## 💬 Example Interaction

```text
=================================
       BASIC AI AGENT
=================================
Type 'exit' to stop the agent.

You: What is artificial intelligence?

AI Agent: Artificial Intelligence (AI) is a field of computer science
that enables computers and software to perform tasks that normally
require human intelligence, such as learning, reasoning, and
understanding language.

You: Explain Python in simple words.

AI Agent: Python is a high-level programming language known for its
simple syntax and readability. It is widely used in web development,
data science, automation, and artificial intelligence.

You: exit

AI Agent: Goodbye!
```

---

## 🧠 How the Code Works

### 1. Import libraries

```python
from openai import OpenAI
from dotenv import load_dotenv
import os
```

These libraries are used to communicate with the OpenAI API and load the API key from the `.env` file.

### 2. Load environment variables

```python
load_dotenv()
```

This loads the values stored in the `.env` file.

### 3. Create OpenAI client

```python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

The API key is retrieved from the environment and used to create the OpenAI client.

### 4. Take user input

```python
user_input = input("You: ")
```

This allows the user to enter a question or instruction.

### 5. Send request to the AI model

```python
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
```

The user's input is sent to the selected AI model.

### 6. Display the response

```python
print("\nAI Agent:", response.output_text)
```

The generated response is displayed on the screen.

### 7. Exit the program

The user can type:

```text
exit
```

to stop the AI Agent.

---

## 🤖 AI-Augmented Workflow

AI was used as a development assistant during this project.

The development workflow is:

```text
Project Requirement
        ↓
AI-Assisted Planning
        ↓
Architecture Decision
        ↓
Code Generation Assistance
        ↓
Developer Review
        ↓
Testing
        ↓
Debugging
        ↓
Final Implementation
        ↓
Documentation
```

AI assistance can be used for:

* Understanding Python concepts.
* Understanding OpenAI API usage.
* Generating initial code examples.
* Explaining errors.
* Debugging.
* Improving documentation.
* Suggesting future features.

However, generated code should be **reviewed, understood, tested, and modified by the developer** before being used in the final project.

---

## 📊 Advantages

* Simple and beginner-friendly.
* Easy to understand.
* Uses Python, which is widely used in AI.
* Easy integration with an AI model.
* Interactive command-line interface.
* Can be extended with additional features.
* Suitable for demonstrating AI-assisted development.

---

## ⚠️ Limitations

* Requires an internet connection.
* Requires an OpenAI API key.
* API usage may have associated costs.
* The current version has no long-term conversation memory.
* The current version does not use external tools.
* The agent cannot independently perform complex real-world tasks yet.
* AI-generated responses may sometimes be incorrect and should be verified.

---

## 🔮 Future Enhancements

The basic AI Agent can be improved by adding:

### Version 2

* Conversation memory.
* Better error handling.
* User interface.

### Version 3

* File reading and processing.
* PDF/document analysis.
* Task-specific tools.

### Version 4

* Web search capability.
* Automated task execution.
* More advanced agent planning.

### Version 5

* Local AI model support using Ollama.
* Database integration.
* Advanced multi-tool AI Agent.

---

## 🔄 Alternative: Ollama

Instead of using the OpenAI API, the project can later be adapted to use **Ollama** with a compatible open-source AI model.

The alternative architecture is:

```text
USER
  ↓
Python Application
  ↓
AI Agent
  ↓
Ollama
  ↓
Local AI Model
  ↓
Response
```

Ollama can be useful when local AI model execution is preferred.

However, local models may require additional system resources and configuration.

---

## 📄 Architecture Decision Record

The technology selection for this project is documented separately in:

```text
ADR-001-Tech-Stack.md
```

The selected primary technology stack is:

```text
Python + OpenAI API
```

Ollama is considered as an alternative local/open-source solution.

---

## 🧪 Testing

The AI Agent should be tested using different types of inputs.

### Test 1: General Question

```text
Input:
What is Artificial Intelligence?

Expected:
The agent should provide a basic explanation of AI.
```

### Test 2: Programming Question

```text
Input:
What is a Python loop?

Expected:
The agent should explain loops and provide a simple example.
```

### Test 3: Exit Command

```text
Input:
exit

Expected:
The agent should display a goodbye message and stop.
```

### Test 4: Invalid/API Error

If an API or network error occurs, the program should display an error message instead of crashing unexpectedly.

---

## 📚 Learning Outcomes

After completing this project, the student should understand:

* Basic AI Agent concepts.
* Python programming.
* API integration.
* Environment variables.
* Secure API key handling.
* AI-assisted coding.
* Basic software architecture.
* Testing and debugging.
* Technical documentation using Markdown.
* Architecture Decision Records.

---

## 👨‍💻 Project Information

**Project:** Basic AI Agent

**Course:** AI-Augmented Workflow

**Language:** Python

**AI Service:** OpenAI API

**Alternative:** Ollama

**Project Type:** Beginner AI Application

**Documentation:** Markdown

---

## 📌 Conclusion

This project demonstrates a simple implementation of an AI Agent using Python and the OpenAI API.

The project focuses on understanding the fundamental architecture of an AI-powered application rather than introducing unnecessary complexity.

The initial version provides an interactive interface where users can communicate with an AI model through a Python program. The system can later be expanded with memory, tools, file processing, web search, and local AI models.

The project also demonstrates an **AI-Augmented Workflow**, where AI tools assist with planning, coding, debugging, and documentation while the developer remains responsible for reviewing, understanding, testing, and validating the final implementation.
