from flask import Flask
from views.benchmark import benchmark_api
from views.home import home_api
from views.util import util_api

app = Flask(__name__)

app.register_blueprint(home_api)
app.register_blueprint(benchmark_api)
app.register_blueprint(util_api)

if __name__=="__main__":
    app.run(debug=True)