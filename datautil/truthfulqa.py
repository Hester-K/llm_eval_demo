from EvalDataset import EvalDataset

class TruthfulQA(EvalDataset):

    def __init__(self, subset, split):
        self.name = 'truthful_qa'
        super().__init__(self.name, subset, split)
        
    def formalize_data(self, id):
        features = self.data.features
        cur_features = [self.data[feature][id] for feature in features]
        prompt = cur_features[2]
        answer = cur_features[3]
        info = 'case {}, category: {}\nsource: {}'.format(id, cur_features[1], cur_features[-1])
        return prompt, answer, info

benchmark = TruthfulQA('generation', 'validation')
benchmark.get_dataset_subset()
benchmark.format_basic_information('truthfulqa_gen_val', 'truthfulqa', '2021/09', 'truthfulqa, generation, validation set')
benchmark.format_cases()
benchmark.format_others()
benchmark.subset_to_json('TruthfulQA_gen_val')