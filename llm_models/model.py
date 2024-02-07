import numpy as np
from .llm_adapter import ChatGPT35Adaptor
import time

def get_llm_response(prompt, model_name='random'):

    if model_name == 'random':
        with open('llm_models\output1.txt', 'r', encoding='UTF-8') as f:
            responses = f.readlines()
        temp = np.random.randint(low=0, high=len(responses), size=1)
        time.sleep(2)
        return responses[temp[0]]
    if model_name == 'GPT-3.5':
        adapter = ChatGPT35Adaptor()
        print("using GPT-3.5")
        return adapter.response('用中文回答: '+ prompt)


# print(get_llm_response("111", model_name="GPT-3.5"))