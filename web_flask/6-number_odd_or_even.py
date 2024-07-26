#!/usr/bin/python3
"""Start web application with two routings
"""

from flask import Flask, render_template
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
@app.route('/python/')
def python_is_cool(text='is cool'):
    """Return reformatted text
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def is_n_integer(n=None):
    """returns if the parameter is an integer
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def tem_if_n(n):
    """ renders html if the parameter is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """ renders html if the parameter is an integer
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
