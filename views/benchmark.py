from flask import Blueprint, render_template, request, jsonify, url_for, redirect
import json

benchmark_api = Blueprint('benchmark_api', __name__)

@benchmark_api.route('/benchmark/<filename>')
def display_benchmark(filename):
#     filepath = 'benchmark\ceval_1.json'
    filepath = 'upload\\' + filename
    # try: 
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
    # bench_data['filepath'] = filepath
    # print(filepath)
    bench_data['filename'] = filename
    return render_template("benchmark.html", template_folder="templates", **bench_data)
    # except:
    #     return redirect(url_for('home_api.home_page', message='benchmark文件解析失败'))

@benchmark_api.route('/benchmark/')
def benchmark_page():
    return redirect(url_for('home_api.home_page', message='未选择文件'))

@benchmark_api.route('/benchmark/<filename>', methods=['POST'])
def edit_benchmark(filename):
    filepath = 'upload\\' + filename
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
    bench_data['filename'] = filename
    # print(filepath)
    return render_template("edit.html", template_folder="templates", **bench_data)
