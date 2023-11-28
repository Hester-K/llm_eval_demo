import json

def parse(filepath):
    with open(filepath, 'r', encoding='UTF-8') as fp:
        json_data = json.load(fp)
    return json_data

def parse_basic_info(filepath):
    data = parse(filepath)
    return json_data['basic_information']

# print(json_data)
# print(json_data['basic_information'])
# print(json_data['cases'][0])

# okay ...
# 我还需要这些吗...?
# 想一下怎么换成html里的js对象


filepath = 'benchmark\ceval.network.val.bench.json'
print(parse(filepath))


