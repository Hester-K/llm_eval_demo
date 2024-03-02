import json
from datasets import load_dataset
from EvalDataset import EvalDataset

class CEval(EvalDataset):

    def __init__(self, subset, split):
        self.name = 'ceval/ceval-exam'
        super().__init__(self.name, subset, split)
        

    def formalize_data(self, id):
        features = self.data.features
        cur_features = [self.data[feature][id] for feature in features]
        prompt = '{}\nA: {}\nB: {}\nC: {}\nD: {}'.format(cur_features[1], cur_features[2], cur_features[3], cur_features[4], cur_features[5])
        answer = cur_features[6]
        info = 'case {}'.format(id)
        return prompt, answer, info



# aaa = CEval('ceval/ceval-exam', 'computer_network', 'val')
# aaa.get_dataset_subset()
# aaa.format_basic_information('ceval-computer-network-val', 'ceval', '2023/05', 'ceval, computer network, validation set')
# aaa.format_cases()
# aaa.format_others()
# aaa.subset_to_json('CEval1')

subsets = [
    "computer_network",
    "operating_system",
    "computer_architecture",
    "college_programming",
    "college_physics",
    "college_chemistry",
    "advanced_mathematics",
    "probability_and_statistics",
    "discrete_mathematics",
    "electrical_engineer",
    "metrology_engineer",
    "high_school_mathematics",
    "high_school_physics",
    "high_school_chemistry",
    "high_school_biology",
    "middle_school_mathematics",
    "middle_school_biology",
    "middle_school_physics",
    "middle_school_chemistry",
    "veterinary_medicine",
    "college_economics",
    "business_administration",
    "marxism",
    "mao_zedong_thought",
    "education_science",
    "teacher_qualification",
    "high_school_politics",
    "high_school_geography",
    "middle_school_politics",
    "middle_school_geography",
    "modern_chinese_history",
    "ideological_and_moral_cultivation",
    "logic",
    "law",
    "chinese_language_and_literature",
    "art_studies",
    "professional_tour_guide",
    "legal_professional",
    "high_school_chinese",
    "high_school_history",
    "middle_school_history",
    "civil_servant",
    "sports_science",
    "plant_protection",
    "basic_medicine",
    "clinical_medicine",
    "urban_and_rural_planner",
    "accountant",
    "fire_engineer",
    "environmental_impact_assessment_engineer",
    "tax_accountant",
    "physician",
]

import os

for subset in subsets:
    if os.path.isfile('datautil\output\CEval_{}_val.json'.format(subset))==False:
        try:
            benchmark = CEval(subset, 'val')
            benchmark.get_dataset_subset()
            benchmark.format_basic_information('ceval_{}_val'.format(subset), 'ceval', '2023/05', 'ceval, {}, validation set'.format(subset.replace('-', ' ')))
            benchmark.format_cases()
            benchmark.format_others()
            benchmark.subset_to_json('CEval/CEval_{}_val'.format(subset))
        except:
            print('failed: {}'.format(subset))