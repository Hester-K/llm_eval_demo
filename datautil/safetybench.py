from EvalDataset import EvalDataset
import json

class SafetyBench(EvalDataset):

    def __init__(self, name, subset, split):
        super().__init__(name, subset, split)

    def get_dataset_subset(self):
        with open(r'datautil\raw\safety_dev.json', 'r', encoding='utf-8') as fp:
            self.data = json.load(fp)

    def format_cases(self):
        cases = []

        features = ['Offensiveness', 'Unfairness and Bias', 'Physical Health',
                    'Mental Health', 'Illegal Activities', 'Ethics and Morality', 'Privacy and Property']

        for feature in features:
            cur_column = self.data[feature]
            # print(cur_column)
            for i in range(len(cur_column)):
                # print(cur_column[i])
                cur_input, cur_answer, cur_info = self.formalize_data(cur_column[i], i, feature)
                cur_case = {
                    "input": cur_input,
                    "expected_answer": cur_answer,
                    "info": cur_info
                }
                cases.append(cur_case)

        self.cases = cases
        return cases

    def formalize_data(self, cur_data, id, feature):
        cur_input = '问题：{}\n选项：'.format(cur_data['question'])
        for i in range(len(cur_data['options'])):
            cur_input = cur_input + '{}.{}\n'.format(chr(ord('A') + i), cur_data['options'][i])
        cur_input += '答案：\n'
        cur_answer = chr(ord('A') + cur_data['answer'])
        cur_info = 'case id {}, category: {}'.format(id, feature)
        return cur_input, cur_answer, cur_info

aaa = SafetyBench('thu-coai/SafetyBench', 'dev', 'zh')
aaa.get_dataset_subset()
aaa.format_basic_information('SafetyBench_dev', 'safetybench', '2023/09', 'safetybench, github repo: https://github.com/thu-coai/SafetyBench')
aaa.format_cases()
aaa.format_others()
aaa.subset_to_json('SafetyBench_dev')