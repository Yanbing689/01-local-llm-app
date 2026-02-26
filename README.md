# Local LLM App (Ollama + Llama 3.2)

Run a private AI chatbot locally using Streamlit and Ollama.

## Features
- Runs fully local (no API calls)
- No data leaves your machine
- Streaming responses
- Lightweight setup

## Requirements
- Python 3.8+
- Ollama installed

## Setup

### 1. Install dependencies
pip install -r requirements.txt

### 2. Pull model
ollama pull llama3.2

### 3. Run the app
streamlit run app.py

## Tech Stack
- Streamlit
- Ollama
- Llama 3.2
