from langchain_ollama import OllamaLLM

# Load local LLM via Ollama
llm = OllamaLLM(model="llama3")  # Change to 'mistral', 'gemma', etc. if needed

print("🧠 Local LLM Chat (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("👋 Exiting chat.")
        break

    response = llm.invoke(user_input)
    print("AI:", response)