import streamlit as st
import config as config
from server.models import ollama
from server.models.llm_api import create_openai_llm, check_openai_llm
from server.models.ollama import create_ollama_llm
from server.models.embedding import create_embedding_model
from server.index import IndexManager
from server.stores.config_store import CONFIG_STORE

def find_api_by_model(model_name):
    """
    Finds the API information based on the given model name.
    
    Args:
        model_name (str): The name of the model.
    
    Returns:
        dict or None: The API information if found, else None.
    """
    for api_name, api_info in config.LLM_API_LIST.items():
        if model_name in api_info["models"]:
            return api_info
    return None

# Initialize session state keys
def init_keys():
    """
    Initializes the necessary keys in the Streamlit session state.
    """
    # Initialize LLM
    if "llm" not in st.session_state:
        st.session_state.llm = None

    # Initialize index manager
    if "index_manager" not in st.session_state:
        st.session_state.index_manager = IndexManager(config.DEFAULT_INDEX_NAME)

    # Initialize Ollama API URL
    if "ollama_api_url" not in st.session_state:
        st.session_state.ollama_api_url = config.OLLAMA_API_URL

    # Initialize list of Ollama models
    if "ollama_models" not in st.session_state:
        models = ollama.get_model_list()
        if models:
            # Set "gemma:2b" as default if available
            if "gemma:2b" in st.session_state.ollama_models:
                st.session_state.ollama_model_selected = "gemma:2b"
            else:
                st.session_state.ollama_model_selected = st.session_state.ollama_models[0]
            # Create the LLM instance with the selected model
            ollama.create_ollama_llm(st.session_state.ollama_model_selected)
        else:
            st.error("Unable to retrieve models from Ollama.")

    # Initialize selected Ollama model
    if "ollama_model_selected" not in st.session_state:
        st.session_state.ollama_model_selected = None

    # Initialize list of all LLM APIs
    if "llm_api_list" not in st.session_state:
        st.session_state.llm_api_list = [
            model for api in config.LLM_API_LIST.values() for model in api["models"]
        ]

    # Initialize selected LLM API
    if "llm_api_selected" not in st.session_state:
        st.session_state.llm_api_selected = st.session_state.llm_api_list[0]
        if st.session_state.ollama_model_selected is None:
            api_object = find_api_by_model(st.session_state.llm_api_selected)
            if api_object:
                create_openai_llm(
                    st.session_state.llm_api_selected,
                    api_object["api_base"],
                    api_object["api_key"]
                )
            else:
                st.error(f"No API configuration found for model {st.session_state.llm_api_selected}")

    # Initialize query engine
    if "query_engine" not in st.session_state:
        st.session_state.query_engine = None

    # Initialize system prompt
    if "system_prompt" not in st.session_state:
        st.session_state.system_prompt = "Chat with me!"

    # Initialize response mode
    if "response_mode" not in st.session_state:
        response_mode_result = CONFIG_STORE.get(key="response_mode")
        if response_mode_result:
            st.session_state.response_mode = response_mode_result["response_mode"]
        else:
            st.session_state.response_mode = config.DEFAULT_RESPONSE_MODE

    # Initialize Ollama endpoint
    if "ollama_endpoint" not in st.session_state:
        st.session_state.ollama_endpoint = "http://localhost:11434"

    # Initialize chunk size and overlap
    if "chunk_size" not in st.session_state:
        st.session_state.chunk_size = config.DEFAULT_CHUNK_SIZE

    if "chunk_overlap" not in st.session_state:
        st.session_state.chunk_overlap = config.DEFAULT_CHUNK_OVERLAP

    # Initialize title enhancement setting
    if "zh_title_enhance" not in st.session_state:
        st.session_state.zh_title_enhance = config.ZH_TITLE_ENHANCE

    # Initialize maximum tokens and top_p
    if "max_tokens" not in st.session_state:
        st.session_state.max_tokens = 100

    if "top_p" not in st.session_state:
        st.session_state.top_p = 1.0

    # Initialize websites and uploaded files
    if "websites" not in st.session_state:
        st.session_state.websites = []

    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = []
    
    if "selected_files" not in st.session_state:
        st.session_state.selected_files = None

    # Initialize user data (to be loaded from database in future)
    if "user_id" not in st.session_state:
        st.session_state.user_id = "user_1"

    if "kb_id" not in st.session_state:
        st.session_state.kb_id = "kb_1"

    if "kb_name" not in st.session_state:
        st.session_state.kb_name = "My knowledge base"

# Initialize LLM service provider selection
def init_llm_sp():
    """
    Initializes the selected LLM service provider.
    """
    llm_options = list(config.LLM_API_LIST.keys())
    if "llm_service_provider_selected" not in st.session_state:
        sp = CONFIG_STORE.get(key="llm_service_provider_selected")
        if sp:
            st.session_state.llm_service_provider_selected = sp["llm_service_provider_selected"]
        else:
            st.session_state.llm_service_provider_selected = llm_options[0]

# Initialize Ollama API endpoint
def init_ollama_endpoint():
    """
    Initializes the Ollama API endpoint from configuration or defaults.
    """
    if "ollama_api_url" not in st.session_state:
        ollama_api_url = CONFIG_STORE.get(key="Ollama_api_url")
        if ollama_api_url:
            st.session_state.ollama_api_url = ollama_api_url["Ollama_api_url"]
        else:
            st.session_state.ollama_api_url = config.LLM_API_LIST["Ollama"]["api_base"]

# Initialize API model selection for non-Ollama providers
def init_api_model(sp):
    """
    Initializes the selected model for a given service provider.
    
    Args:
        sp (str): The service provider name.
    """
    if sp != "Ollama":
        model_key = f"{sp}_model_selected"
        if model_key not in st.session_state:
            model_result = CONFIG_STORE.get(key=model_key)
            if model_result:
                st.session_state[model_key] = model_result[model_key]
            else:
                st.session_state[model_key] = config.LLM_API_LIST[sp]["models"][0]

# Initialize API base URL for non-Ollama providers
def init_api_base(sp):
    """
    Initializes the API base URL for a given service provider.
    
    Args:
        sp (str): The service provider name.
    """
    if sp != "Ollama":
        api_base = f"{sp}_api_base"
        if api_base not in st.session_state:
            api_key_result = CONFIG_STORE.get(key=api_base)
            if api_key_result is not None:
                st.session_state[api_base] = api_key_result[api_base]
            else:
                st.session_state[api_base] = config.LLM_API_LIST[sp]["api_base"]

# Initialize API key for non-Ollama providers
def init_api_key(sp):
    """
    Initializes the API key for a given service provider.
    
    Args:
        sp (str): The service provider name.
    """
    if sp != "Ollama":
        api_key = f"{sp}_api_key"
        if api_key not in st.session_state:
            api_key_result = CONFIG_STORE.get(key=api_key)
            if api_key_result is not None:
                st.session_state[api_key] = api_key_result[api_key]
            else:
                st.session_state[api_key] = config.LLM_API_LIST[sp]["api_key"]
        
        # Validate the API key
        valid_key = f"{api_key}_valid"
        if valid_key not in st.session_state:
            valid_result = CONFIG_STORE.get(key=valid_key)
            if valid_result is None and st.session_state.get(api_key):
                is_valid = check_openai_llm(
                    st.session_state[f"{sp}_model_selected"],
                    config.LLM_API_LIST[sp]["api_base"],
                    st.session_state[api_key]
                )
                CONFIG_STORE.put(key=valid_key, val={valid_key: is_valid})
                st.session_state[valid_key] = is_valid
            elif valid_result:
                st.session_state[valid_key] = valid_result[valid_key]
            else:
                st.session_state[valid_key] = False

# Initialize LLM settings like temperature and system prompt
def init_llm_settings():
    """
    Initializes the current LLM settings such as temperature and system prompt.
    """
    if "current_llm_settings" not in st.session_state:
        current_llm_settings = CONFIG_STORE.get(key="current_llm_settings")
        if current_llm_settings:
            st.session_state.current_llm_settings = current_llm_settings
        else:
            st.session_state.current_llm_settings = {
                "temperature": config.TEMPERATURE,
                "system_prompt": config.SYSTEM_PROMPT,
                "top_k": config.TOP_K,
                "response_mode": config.DEFAULT_RESPONSE_MODE,
                "use_reranker": config.USE_RERANKER,
                "top_n": config.RERANKER_MODEL_TOP_N,
                "embedding_model": config.DEFAULT_EMBEDDING_MODEL,
                "reranker_model": config.DEFAULT_RERANKER_MODEL,
            }
            CONFIG_STORE.put(key="current_llm_settings", val=st.session_state.current_llm_settings)

# Create the LLM instance based on current information
def create_llm_instance():
    """
    Creates the LLM instance based on the current LLM information stored in CONFIG_STORE.
    """
    current_llm_info = CONFIG_STORE.get(key="current_llm_info")
    if current_llm_info:
        print("Current LLM info: ", current_llm_info)
        if current_llm_info["service_provider"] == "Ollama":
            if ollama.is_alive():
                model_name = current_llm_info.get("model", "gemma:2b")  # Default to Gemma if not specified
                if model_name not in st.session_state.ollama_models:
                    st.error(f"Model '{model_name}' is not available in Ollama.")
                    st.session_state.llm = None
                else:
                    st.session_state.llm = create_ollama_llm(
                        model=model_name, 
                        temperature=st.session_state.current_llm_settings["temperature"],
                        system_prompt=st.session_state.current_llm_settings["system_prompt"],
                    )
                    if st.session_state.llm:
                        st.success(f"Ollama LLM '{model_name}' created successfully.")
                    else:
                        st.error(f"Failed to create Ollama LLM with model '{model_name}'.")
        else:
            # Handle other service providers (e.g., OpenAI)
            model_name = current_llm_info.get("model")
            api_base = current_llm_info.get("api_base")
            api_key = current_llm_info.get("api_key")
            api_key_valid = current_llm_info.get("api_key_valid", False)
            if api_key_valid:
                print("API key is valid when creating LLM instance")
                st.session_state.llm = create_openai_llm(
                    model_name=model_name, 
                    api_base=api_base, 
                    api_key=api_key,
                    temperature=st.session_state.current_llm_settings["temperature"],
                    system_prompt=st.session_state.current_llm_settings["system_prompt"],
                )
            else:
                print("API key is invalid when creating LLM instance")
                st.session_state.llm = None
    else:
        print("No current LLM information found.")
        st.session_state.llm = None

# Initialize the entire session state
def init_state():
    """
    Initializes the entire Streamlit session state by setting up keys, endpoints,
    service providers, models, and LLM instances.
    """
    init_keys()
    init_ollama_endpoint()
    init_llm_sp()
    init_llm_settings()
    sp = st.session_state.llm_service_provider_selected
    init_api_model(sp)
    init_api_key(sp)
    
    # Create the embedding model based on current settings
    create_embedding_model(st.session_state["current_llm_settings"]["embedding_model"])
    
    # Create the LLM instance
    create_llm_instance()