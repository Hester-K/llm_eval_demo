# from .model import get_llm_response, get_llms
from .ollama_model import get_ollama_llms, get_ollama_llm_response

__all__=[
    # 'get_llm_response',
    # 'get_llms',
    'get_ollama_llms',
    'get_ollama_llm_response'
]