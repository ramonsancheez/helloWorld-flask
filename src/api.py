from distutils.log import debug
from flask import Flask

app = Flask(__name__)

def helloWorld():
    sentence = '<h1>Hello World!</h1>'
    return sentence

app.add_url_rule('/', 'helloWorld', helloWorld)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)