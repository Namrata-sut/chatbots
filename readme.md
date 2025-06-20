# LangChain QA Chatbot with Gemini and Ollama

This Streamlit-based app provides two chatbots built with LangChain, supporting:

- Gemini 1.5 Flash by Google (cloud-based LLM via API)
- Phi-3 / LLaMA 2 and other models via Ollama (local LLM inference)

The app uses LangChain’s modular pipeline with prompt templates, output parsing, and model abstraction.

---
## Features
- Interactive UI with Streamlit
- Use Gemini (Google) or Ollama (Local) LLMs
- Prompt templating with LangChain
- Output parsing using `StrOutputParser`
- LangSmith tracing support (optional)
---

## Setup & Installation

1. Install Python 3.8 or above.

2. Create a virtual environment:  
   `python -m venv venv`

3. Activate the virtual environment:  
   - On Windows: `venv\Scripts\activate`  
   - On macOS/Linux: `source venv/bin/activate`

4. Install all required dependencies:  
   `pip install -r requirements.txt`

5. Create a `.env` file in the root of the project with the following content:
GEMINI_API_KEY=`your_gemini_api_key`
LANGCHAIN_API_KEY=`your_langsmith_api_key`

Run Gemini-based chatbot:
   `streamlit run gemini_chatbot.py`

Run Ollama-based chatbot:
1. Install Ollama from https://ollama.com/download
2. Pull a local model using: ollama pull phi3
3. Start the model using: ollama run phi3
4. In another terminal (same project folder), run:
   `streamlit run ollama_chatbot.py`

This will launch the Streamlit app that interacts with your locally running model.


