from EvalDataset import EvalDataset
import json

class AlignBench(EvalDataset):

    def __init__(self, name, subset, split):
        super().__init__(name, subset, split)

    def get_dataset_subset(self):
        self.data = []
        with open(r'datautil\raw\alignbench.jsonl', 'r', encoding='utf-8') as fp:
            for line in fp:
                self.data.append(json.loads(line))

    def format_cases(self):
        cases = []
        for i in range(0, len(self.data)):
            cur_data = self.data[i]
            cur_input, cur_answer, cur_info = self.formalize_data(cur_data)
            cur_case = {
                "input": cur_input,
                "expected_answer": cur_answer,
                "info": cur_info
            }
            cases.append(cur_case)

        self.cases = cases
        return cases

    def formalize_data(self, cur_data):
        cur_input = cur_data['question']
        cur_answer = cur_data['reference']
        cur_info = "question_id: {}, category: {}, subcategory: {}".format(cur_data['question_id'], cur_data['category'], cur_data['subcategory'])
        return cur_input, cur_answer, cur_info

    def subset_to_json(self, filename):
        categories = ['专业能力', '数学计算', '基本任务', '逻辑推理', '文本写作', '中文理解', '角色扮演', '综合问答']
        cur_cases = []
        cur_category = 0
        for case in self.cases + [self.cases[0]]:
            if categories[cur_category] in case['info']:
                cur_cases.append(case)
            else:
                subset_dict = {'basic_information': self.basic_info, 'cases': cur_cases, 'formatters': self.formatters, 'evaluators': self.evaluators, 'evaluation': self.evaluation}
                with open('datautil/output/AlignBench/{}_{}.json'.format(filename, categories[cur_category]), 'w', encoding='utf-8') as f:
                    json.dump(subset_dict, f, ensure_ascii=False, indent=4)
                cur_cases = [case]
                cur_category += 1

aaa = AlignBench('thu-coai/AlignBench', '', '')
aaa.get_dataset_subset()
aaa.format_basic_information('AlignBench', 'align benchmark', '2023/12', 'thu-coai')
aaa.format_cases()
aaa.format_others()
aaa.subset_to_json('AlignBench')