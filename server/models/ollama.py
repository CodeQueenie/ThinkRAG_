import requests
import streamlit as st
from ollama import Client
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama

def is_alive():
    """
    Checks if the Ollama API server is running.
    """
    try:
        response = requests.get(st.session_state.ollama_api_url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        print("Failed to connect to Ollama")
        return False

def get_model_list():
    """
    Retrieves the list of available models from Ollama and stores them in session state.
    """
    st.session_state.ollama_models = []
    if is_alive():
        client = Client(host=st.session_state.ollama_api_url)
        response = client.list()
        models = response.get("models", [])
        # Initialize the list of model names
        for model in models:
            st.session_state.ollama_models.append(model.get("name", ""))
        return models
    else:
        print("Ollama is not alive")
        return None

def create_ollama_llm(model: str, temperature: float = 0.5, system_prompt: str = None) -> Ollama:
    """
    Creates an Ollama LLM instance with the specified model and parameters.
    """
    try:
        llm = Ollama(
            model=model, 
            base_url=st.session_state.ollama_api_url, 
            request_timeout=600,
            temperature=temperature,
            system_prompt=system_prompt,
        )
        print(f"Created Ollama model for query: {model}")
        Settings.llm = llm
        return llm
    except Exception as e:
        print(f"An error occurred while creating Ollama LLM: {e}")
        return None