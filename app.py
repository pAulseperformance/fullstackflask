import os
from flask import Flask
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


@app.route('/')
def hello():
    return 'hello world'

@app.route('/')
def hello_name(name):
    return 'hello '

if __name__ == '__main__':
    app.run()
