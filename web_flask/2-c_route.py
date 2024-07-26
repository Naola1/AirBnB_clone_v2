#!/usr/bin/python3
"""script that starts flask web application frame work
 and listens on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Return string when route queried
    """
    return 'Hello HBNB!'

@app.route("/hbnb",strict_slashes=False)
def hbnb():
    """display a string 'HBNB'"""
    return "HBNB"

@app.route("/c/<text>")
def c_test(text):
    """display “C ” followed by the value of the text variable"""
    text=text.replace('_',' ')
    return f"C {text}"

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000,debug=None)
