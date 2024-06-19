import ollama

def get_ollama_llms():
    llms = [
        'llama3',
        'qwen2',
        'phi3'
    ]
    return llms

def get_ollama_llm_response(prompt, model_name='llama3'):
    try:
        response = ollama.chat(model=model_name, messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ])
        return response['message']['content']
    except:
        pass
    # if model_name == 'llama3':
    #     response = ollama.chat(model='llama3', messages=[
    #         {
    #             'role': 'user',
    #             'content': '用和问题相同的语言回答：{prompt}',
    #         },
    #     ])
    #     return response['message']['content']
    # pass

# response = ollama.chat(model='llama3', messages=[
#   {
#     'role': 'user',
#     'content': '用中文回答：为什么天是蓝色的',
#   },
# ])
# print(response['message']['content'])


# def get_llms():
#     llms = [
#         'GPT-3.5',
#         'QWen-max',
#         'QWen-turbo',
#         'QWen-plus',
#         'Gemini-pro'
#     ]
#     return llms

# def get_llm_response(prompt, model_name='random'):

#     if model_name == 'GPT-3.5':
#         adapter = ChatGPT35Adaptor()
#         return adapter.get_response('用中文回答: '+ prompt)
#     if model_name == 'QWen-max':
#         adapter = QWenAdaptor('max')
#         return adapter.get_response(prompt)
#     if model_name == 'QWen-plus':
#         adapter = QWenAdaptor('plus')
#         return adapter.get_response(prompt)
#     if model_name == 'QWen-turbo':
#         adapter =QWenAdaptor('turbo')
#         return adapter.get_response(prompt)
#     if model_name == 'Gemini-pro':
#         adapter = GeminiAdaptor()
#         return adapter.get_response('用中文回答: '+ prompt)

# # get_llm_response('你好', 'Qwen-turbo')