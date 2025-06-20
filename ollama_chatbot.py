import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

load_dotenv()
os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")

# Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries."),
        ("user", "Question: {question}")
    ]
)

# streamlit framework
st.title("Ollama LLaMA ChatBot")
input_text = st.text_input("Search the topic you want...")

# Ollama llama2:7b llm
llm = Ollama(model="phi3")

# Output
output_parser = StrOutputParser()

# chain
chain=prompt|llm|output_parser

# Display output
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
    