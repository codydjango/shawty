import os
from flask import Flask

APP_HOST = os.environ.get('APP_HOST', '127.0.0.1')
APP_PORT = os.environ.get('APP_PORT', '8000')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == 'main':
    app.run(host=APP_HOST, port=APP_PORT, debug=True)
