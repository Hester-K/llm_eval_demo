from .llm_adapter import *

def get_llms():
    llms = [
        'GPT-3.5',
        'QWen-max',
        'QWen-turbo',
        'QWen-plus',
        'Gemini-pro'
    ]
    return llms

def get_llm_response(prompt, model_name='random'):

    if model_name == 'GPT-3.5':
        adapter = ChatGPT35Adaptor()
        return adapter.get_response('用中文回答: '+ prompt)
    if model_name == 'QWen-max':
        adapter = QWenAdaptor('max')
        return adapter.get_response(prompt)
    if model_name == 'QWen-plus':
        adapter = QWenAdaptor('plus')
        return adapter.get_response(prompt)
    if model_name == 'QWen-turbo':
        adapter =QWenAdaptor('turbo')
        return adapter.get_response(prompt)
    if model_name == 'Gemini-pro':
        adapter = GeminiAdaptor()
        return adapter.get_response('用中文回答: '+ prompt)

# get_llm_response('你好', 'Qwen-turbo')