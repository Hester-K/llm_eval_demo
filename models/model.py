import numpy as np

def get_llm_response(input):
    with open('models\output1.txt', 'r', encoding='UTF-8') as f:
        responses = f.readlines()
    temp = np.random.randint(low=0, high=len(responses), size=1)
    # return np.array([chr(ord('@') + 1 + i) for i in temp])
    return responses[temp[0]]

# print(get_llm_response("111"))