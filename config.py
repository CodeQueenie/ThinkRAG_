import os

# ===========================
# Directory Configuration
# ===========================

STORAGE_DIR = "storage"  # Directory to cache the generated index
DATA_DIR = "data"        # Directory containing the documents to index
MODEL_DIR = "localmodels"  # Directory containing the model files; set to None to use remote models
CONFIG_STORE_FILE = "config_store.json"  # Local storage for configurations

# ===========================
# Device Configuration
# ===========================

# The device used for running the model.
# Options: 'auto' (automatic detection with warnings), 'cuda', 'mps', 'cpu', or 'xpu'.
LLM_DEVICE = "auto"
EMBEDDING_DEVICE = "auto"

# ===========================
# LLM Settings
# ===========================

HISTORY_LEN = 3  # Number of previous interactions to consider
MAX_TOKENS = 2048  # Maximum tokens for model responses
TEMPERATURE = 0.1   # Sampling temperature for responses
TOP_K = 5           # Top-K sampling parameter

SYSTEM_PROMPT = (
    "You are an AI assistant that helps users to find accurate information. "
    "You can answer questions, provide explanations, and generate text based on the input. "
    "Please answer the user's question exactly in the same language as the question or follow user's instructions. "
    "Specifically, if user's question is in English, ALWAYS generate answers in English. "
    "And if user's question is in Chinese, ALWAYS generate answers in Chinese. "
    "If you don't know the answer, please reply the user that you don't know. "
    "If you need more information, ask the user for clarification. "
    "Please be professional to the user."
)

# ===========================
# Response Mode Configuration
# ===========================

RESPONSE_MODE = [   # Configure the response mode of the query engine
    "compact",
    "refine",
    "tree_summarize",
    "simple_summarize",
    "accumulate",
    "compact_accumulate",
]
DEFAULT_RESPONSE_MODE = "simple_summarize"

# ===========================
# Ollama API Configuration
# ===========================

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434") # Default Ollama API URL

# ===========================
# Models' API Configuration
# ===========================

# API Keys for various LLM providers; set these in your environment variables for security.
ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY", "")
MOONSHOT_API_KEY = os.getenv("MOONSHOT_API_KEY", "")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# LLM API List Configuration
LLM_API_LIST = {
    # Ollama API Configuration
    "Ollama": {
        "api_base": OLLAMA_API_URL,
        "models": ["gemma:2b"],  # Added Gemma model
        # "provider": "Ollama",  # Optional: Remove if redundant
    },
    # OpenAI API Configuration
    "OpenAI": {
        "api_key": OPENAI_API_KEY,
        "api_base": "https://api.openai.com/v1/",
        "models": ["gpt-4", "gpt-3.5", "gpt-4o"],
        # "provider": "OpenAI",  # Optional: Remove if redundant
    },
    # Zhipu API Configuration
    "Zhipu": {
        "api_key": ZHIPU_API_KEY,
        "api_base": "https://open.bigmodel.cn/api/paas/v4/",
        "models": [
            "glm-4-plus", "glm-4-0520", "glm-4", "glm-4-air",
            "glm-4-airx", "glm-4-long", "glm-4-flashx",
            "glm-4-flash", "glm-4v-plus", "glm-4v"
        ],
        # "provider": "Zhipu",  # Optional: Remove if redundant
    },
    # Moonshot API Configuration
    "Moonshot": {
        "api_key": MOONSHOT_API_KEY,
        "api_base": "https://api.moonshot.cn/v1/",
        "models": ["moonshot-v1-8k", "moonshot-v1-32k", "moonshot-v1-128k"],
        # "provider": "Moonshot",  # Optional: Remove if redundant
    },
    # DeepSeek API Configuration
    "DeepSeek": {
        "api_key": DEEPSEEK_API_KEY,
        "api_base": "https://api.deepseek.com/v1/",
        "models": ["deepseek-chat"],
        # "provider": "DeepSeek",  # Optional: Remove if redundant
    },
}

# ===========================
# Text Splitter Configuration
# ===========================

DEFAULT_CHUNK_SIZE = 2048
DEFAULT_CHUNK_OVERLAP = 512
ZH_TITLE_ENHANCE = False  # Enable Chinese title enhancement

# ===========================
# Storage Configuration
# ===========================

MONGO_URI = "mongodb://localhost:27017"
REDIS_URI = "redis://localhost:6379"
REDIS_HOST = "localhost"
REDIS_PORT = 6379
ES_URI = "http://localhost:9200"

# Default vector database type, options include "es" (Elasticsearch) and "chroma"
DEFAULT_VS_TYPE = "es"

# Chat store type, options include "simple" and "redis"
DEFAULT_CHAT_STORE = "redis"
CHAT_STORE_FILE_NAME = "chat_store.json"
CHAT_STORE_KEY = "user1"

# ===========================
# HuggingFace Model Configuration
# ===========================

HF_ENDPOINT = "https://hf-mirror.com"  # Default to "https://huggingface.co"

# ===========================
# Embedding Model Configuration
# ===========================

DEFAULT_EMBEDDING_MODEL = "bge-small-zh-v1.5"
EMBEDDING_MODEL_PATH = {
    "bge-small-zh-v1.5": "BAAI/bge-small-zh-v1.5",
    "bge-large-zh-v1.5": "BAAI/bge-large-zh-v1.5",
}

# ===========================
# Reranker Model Configuration
# ===========================

DEFAULT_RERANKER_MODEL = "bge-reranker-base"
RERANKER_MODEL_PATH = {
    "bge-reranker-base": "BAAI/bge-reranker-base",
    "bge-reranker-large": "BAAI/bge-reranker-large",
}

# Use reranker model or not
USE_RERANKER = False
RERANKER_MODEL_TOP_N = 2
RERANKER_MAX_LENGTH = 1024

# ===========================
# Environment Configuration
# ===========================

# Environment variable, default to "development", set to "production" for production environment
THINKRAG_ENV = os.getenv("THINKRAG_ENV", "development")
DEV_MODE = THINKRAG_ENV == "development"

# ===========================
# Index Manager Configuration
# ===========================

DEFAULT_INDEX_NAME = "knowledge_base"