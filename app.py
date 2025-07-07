import requests, sys
from flask import Flask
from assistant_server import command



app = Flask(__name__)
app.register_blueprint(command)


@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)