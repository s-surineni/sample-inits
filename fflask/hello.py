from flask import request
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    print(request)
    print(request.headers)
    return 'Hello, World!'
