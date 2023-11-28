from flask import Flask, render_template, request, jsonify
import json
from models.model import get_llm_response

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route('/')
# def index():
#     return render_template('home.html')

@app.route('/')
def display_benchmark():
    filepath = 'benchmark\ceval_1.json'
    with open(filepath, 'r', encoding='utf-8') as fp:
        bench_data = json.load(fp)
    # return bench_data['basic_information']['name']
    kwargs = {'name': bench_data['basic_information']['name']}
    for func in bench_data['formatters']:
        if type(func['definition'])==list:
            func['definition'] = '\n'.join(func['definition'])
        # print([func['definition']])
        func['definition'] = func['definition'].replace('formatter', func['name'], 1)
    for func in bench_data['evaluators']:
        if type(func['definition'])==list:
            func['definition'] = '\n'.join(func['definition'])
        func['definition'] = func['definition'].replace('evaluator', func['name'], 1)
    return render_template("benchmark.html", **bench_data)

@app.route('/process_data', methods=['GET', 'POST'])
def process_data():
    print(request)
    if request.method == 'POST':
        req_input = request.json.get('input')
        # Process the selected option received from frontend
        print("input:", req_input)
        response_data = {
            'response': get_llm_response(req_input)
        }
        # Perform actions based on the selected option
        print(jsonify(response_data))
        return jsonify(response_data)
    else:
        return "Invalid request method"

if __name__ == '__main__':
    # filepath = 'benchmark\ceval_1.json'
    app.run(debug=True)