from flask import Blueprint, render_template, request, jsonify, url_for, redirect
from llm_models.model import get_llm_response
import json

util_api = Blueprint('util_api', __name__)

@util_api.route('/process_data', methods=['GET', 'POST'])
def process_data():
    print(request)
    if request.method == 'POST':
        req_input = request.json.get('input')
        model = request.json.get('model')
        # Process the selected option received from frontend
        print("input:", req_input, "model:", model)
        response_data = {
            'response': get_llm_response(req_input, model)
        }
        # Perform actions based on the selected option
        print(jsonify(response_data))
        return jsonify(response_data)
    else:
        return "Invalid request method"

@util_api.route('/save_eval', methods=['POST'])
def save_eval():
    print(request.json)
    # return {'1': 1}
    filepath = 'upload\\' + request.json.get('filename')
    with open(filepath, 'r', encoding='utf-8') as fp:
        bench_data = json.load(fp)
    bench_data['evaluation'] = request.json.get('evaluation')
    with open(filepath, 'w', encoding='utf-8') as fp:
        json.dump(bench_data, fp, ensure_ascii=False, indent=4)
