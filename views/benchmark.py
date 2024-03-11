from flask import Blueprint, render_template, request, url_for, redirect, session
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
    try:
        bench_data['results'] = session['{}_results'.format(filename)]
    except:
        bench_data['results'] = []
    return render_template("benchmark.html", template_folder="templates", **bench_data)

@benchmark_api.route('/benchmark/')
def benchmark_page():
    return redirect(url_for('home_api.home_page', message='未选择文件'))

@benchmark_api.route('/benchmark/<filename>/edit')
def edit_benchmark(filename):
    filepath = 'upload\\' + filename
    print('route')
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
    bench_data['results'] = session['{}_results'.format(filename)]
    return render_template("edit.html", template_folder="templates", **bench_data)

@benchmark_api.route('/benchmark/<filename>/jump_to_edit', methods=['POST'])
def jump_to_edit(filename):
    print(request.json)
    results = request.json.get('results')
    session['{}_results'.format(filename)] = results
    print(results)
    edit_url = url_for('benchmark_api.edit_benchmark', filename=filename)
    print(edit_url)
    return redirect(edit_url)

@benchmark_api.route('/benchmark/<filename>/return_to_benchmark', methods=['POST'])
def return_to_benchmark(filename):
    benchmark_url = url_for('benchmark_api.display_benchmark', filename=filename)
    return redirect(benchmark_url)