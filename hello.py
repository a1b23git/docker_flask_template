from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    print(55+15)  # debug message
    return '<h1>Hello, oops!</h1>'
