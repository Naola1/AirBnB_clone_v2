#!/usr/bin/python3
"""Start web application with two routings
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Return string 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return string 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Return reformatted text
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>')
@app.route('/python')
def python_is_cool(text='is cool'):
    """Return reformatted text
    """
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
