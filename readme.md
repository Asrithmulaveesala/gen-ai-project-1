# 🤖 Gemma AI Chatbot

A clean, responsive, locally hosted conversational AI application built using **Streamlit, LangChain, and Ollama**, powered by Google's **Gemma 2B** model.

The application provides a simple chat interface while keeping the LLM execution **completely local** through Ollama.

---

## 🌟 Key Features

### 🔒 100% Local Execution

Powered by **Ollama**, allowing the Gemma 2B model to run locally on your machine. Your conversations do not need to be sent to an external LLM API.

### 🔗 LangChain Integration

Built using **LangChain** and **LCEL (LangChain Expression Language)** to create the conversational pipeline using:

* Chat Prompt Templates
* LCEL chains
* Output parsers
* Ollama LLM integration

### 🧠 Context-Aware Conversation

The chatbot maintains the conversation history between the user and assistant, allowing it to respond based on previous exchanges.

### 🎨 Custom UI

The Streamlit interface includes custom CSS styling for:

* Clean chat interface
* Customized chat input
* Fixed footer
* Hidden default chat avatars
* Responsive layout

### 📊 Observability Ready

The project can optionally be connected to **LangSmith** for monitoring and tracing LangChain applications.

---

## 🛠️ Tech Stack

| Technology        | Purpose                            |
| ----------------- | ---------------------------------- |
| **Python**        | Core programming language          |
| **Streamlit**     | Web application interface          |
| **LangChain**     | LLM application framework          |
| **LCEL**          | Chain orchestration                |
| **Ollama**        | Local LLM execution                |
| **Gemma 2B**      | Language model                     |
| **python-dotenv** | Environment variable management    |
| **LangSmith**     | Optional tracing and observability |

---

## 📋 Prerequisites

Before running the application, make sure you have:

* Python **3.9+**
* Ollama installed
* Gemma 2B model downloaded
* Git installed

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gemma-ai-chatbot.git
cd gemma-ai-chatbot
```

---

### 2. Create a Virtual Environment

It is recommended to use a virtual environment.

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install streamlit langchain langchain-ollama python-dotenv
```

Or, if a `requirements.txt` file is included:

```bash
pip install -r requirements.txt
```

---

### 4. Install and Run Ollama

Make sure Ollama is installed and running on your system.

Then download and run the Gemma 2B model:

```bash
ollama run gemma:2b
```

This will download the model if it is not already available locally.

---

### 5. Configure Environment Variables

LangSmith integration is optional.

Create a `.env` file in the project root:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=gemma-chatbot-project
```

If you don't want to use LangSmith, you can skip this step.

> ⚠️ Never commit your actual API keys or `.env` file to GitHub.

Add `.env` to your `.gitignore` file:

```text
.env
venv/
__pycache__/
```

---

### 6. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🔄 Application Flow

```text
User Input
    ↓
Streamlit Chat Interface
    ↓
Chat Prompt Template
    ↓
LCEL Chain
    ↓
Ollama
    ↓
Gemma 2B
    ↓
Response
    ↓
Chat History
```

The conversation history is maintained so that the chatbot can provide context-aware responses.

---

## 📂 Project Structure

```text
gemma-ai-chatbot/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
├── .gitignore              # Git ignored files
└── README.md               # Project documentation
```

---

## 🧩 Concepts Used

This project helped strengthen my understanding of:

* Large Language Models (LLMs)
* Local LLM deployment
* Ollama
* Google Gemma
* LangChain
* LCEL
* ChatPromptTemplate
* StrOutputParser
* Prompt Engineering
* Conversation History
* Streamlit
* LangSmith
* LLM application development

---

## 🔐 Privacy

Since the Gemma model runs locally through **Ollama**, the chatbot can operate without sending conversation data to a cloud-based LLM API.

However, optional **LangSmith tracing** may transmit application traces to LangSmith when configured.

---

## 👤 Author

**Koushik Asrith Mulavisala**

Aspiring **Generative AI / AI Engineer** passionate about building applications using:

* Generative AI
* LLMs
* RAG
* LangChain
* Agentic AI
* Machine Learning

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!

---
