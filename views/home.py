from flask import Blueprint, render_template, request, url_for, redirect
import os

home_api = Blueprint('home_api', __name__)

@home_api.route("/")
def home_page():
    message = request.args.get('message')
    filenames = os.listdir('upload')
    data = {'filename': filenames, 'message': message}
    return render_template("home.html", template_folder="templates", **data)

@home_api.route('/', methods=['POST'])
def upload_file():
    print('upload')
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save('upload/' + uploaded_file.filename)
    bench_url = url_for('benchmark_api.display_benchmark', filename=uploaded_file.filename)
    return redirect(bench_url)