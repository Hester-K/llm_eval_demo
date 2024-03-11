import json
from datasets import load_dataset

class EvalDataset:
    def __init__(self):
        pass

    def __init__(self, name):
        self.name = name

    def __init__(self, name, subset, split):
        self.name = name
        self.subset = subset
        self.split = split

    def get_dataset_subset(self):
        self.data = load_dataset(self.name, name=self.subset)[self.split]

    def formalize_data(self, id):
        # input and answer
        pass

    def subset_to_json(self, filename):
        subset_dict = {'basic_information': self.basic_info, 'cases': self.cases, 'formatters': self.formatters, 'evaluators': self.evaluators, 'evaluation': self.evaluation}

        with open('datautil/output/{}.json'.format(filename), 'w', encoding='utf-8') as f:
            json.dump(subset_dict, f, ensure_ascii=False, indent=4)

    def format_basic_information(self, name, creator, date, info):
        self.basic_info = {
            "name": name, 
            "creator": creator, 
            "date": date, 
            "info": info
        }

    def format_cases(self):
        cases = []

        num_rows = self.data.num_rows
        for i in range(0, num_rows):
            cur_input, cur_answer, cur_info = self.formalize_data(i)

            cur_case = {
                "input": cur_input,
                "expected_answer": cur_answer,
                "info": cur_info
                }

            cases.append(cur_case)
        self.cases = cases
        return cases

    def format_others(self):
        with open('datautil\\template.json', 'r', encoding='utf-8') as fp:
            template = json.load(fp)
            self.formatters = template['formatters']
            self.evaluators = template['evaluators']
            self.evaluation = template['evaluation']
