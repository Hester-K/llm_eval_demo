from flask import Blueprint, render_template, request, jsonify, url_for, redirect
import json
from llm_models import get_llms

benchmark_api = Blueprint('benchmark_api', __name__)

@benchmark_api.route('/benchmark/<filename>')
def display_benchmark(filename):
    filepath = 'upload\\' + filename
    with open(filepath, 'r', encoding='utf-8') as fp:
        bench_data = json.load(fp)
    for func in bench_data['formatters']:
        if type(func['definition'])==list:
            func['definition'] = '\n'.join(func['definition'])
        func['definition'] = func['definition'].replace('formatter', func['name'], 1)
    for func in bench_data['evaluators']:
        if type(func['definition'])==list:
            func['definition'] = '\n'.join(func['definition'])
        func['definition'] = func['definition'].replace('evaluator', func['name'], 1)
    bench_data['filename'] = filename
    return render_template("benchmark.html", template_folder="templates", **bench_data)

@benchmark_api.route('/benchmark/')
def benchmark_page():
    return redirect(url_for('home_api.home_page', message='未选择文件'))

@benchmark_api.route('/benchmark/<filename>', methods=['POST'])
def edit_benchmark(filename):
    filepath = 'upload\\' + filename
    with open(filepath, 'r', encoding='utf-8') as fp:
        bench_data = json.load(fp)
    for func in bench_data['formatters']:
        if type(func['definition'])==list:
            func['definition'] = '\n'.join(func['definition'])
        func['definition'] = func['definition'].replace('formatter', func['name'], 1)
    for func in bench_data['evaluators']:
        if type(func['definition'])==list:
            func['definition'] = '\n'.join(func['definition'])
        func['definition'] = func['definition'].replace('evaluator', func['name'], 1)
    bench_data['filename'] = filename
    bench_data['llms'] = get_llms()
    return render_template("edit.html", template_folder="templates", **bench_data)
