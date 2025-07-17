# 🔠 Local LLM Chatbot using LangChain + Ollama

This is a simple command-line chatbot powered by a local LLM (like `llama3`, `mistral`, etc.) using [LangChain](https://www.langchain.com/) and [Ollama](https://ollama.com/). It runs entirely on your machine — no cloud APIs needed!

---

## 🚀 Features

- Chat with a local LLM using LangChain
- Continuous user input in the terminal
- Fully offline and private
- Easily switch between models (`llama3`, `mistral`, `gemma`, etc.)

---

## 👩‍💻 Requirements

- Python 3.9+
- [Ollama installed and running](https://ollama.com/)
- Local model pulled (e.g. `ollama run llama3`)

---

## 📦 Installation

1. **Clone the repo**
```bash
git clone https://github.com/mjddelacruz/langchain-ollama-chat.git
cd langchain-ollama-chat
```

2. **Set up virtual environment**
```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **(Optional) Pull a model if not done yet**
```bash
ollama run llama3
```

---

## 🔠 Run the Chatbot

```bash
python main.py
```

Then just start chatting in your terminal.

Type `exit` or `quit` to stop the chat.

---

## 🔀 Switch Models

To use a different local model, edit this line in `main.py`:
```python
llm = OllamaLLM(model="llama3")  # Change to "mistral", "gemma", etc.
```

---

## 📋 Example Interaction

```
🔠 Local LLM Chat (type 'exit' to quit)
You: What is LangChain?
AI: LangChain is an open-source framework for building applications using large language models...
```

---

## 📄 License

MIT License — free to use, modify, and distribute.

