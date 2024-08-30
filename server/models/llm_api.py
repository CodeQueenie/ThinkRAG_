# Create LLM with API compatible with OpenAI
from llama_index.core import Settings
from langchain_openai import ChatOpenAI

def create_openai_llm(model_name, api_base, api_key) -> ChatOpenAI:
    try:
        Settings.llm = ChatOpenAI(
            openai_api_base=api_base, 
            openai_api_key=api_key,
            model_name=model_name
        )
        print(f"created openai model: {model_name}")
        return Settings.llm
    except Exception as e:
        print(f"An error occurred while creating the OpenAI compatibale model: {type(e).__name__}: {e}")
        return None