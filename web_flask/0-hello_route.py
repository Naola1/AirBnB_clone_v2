#!/usr/bin/python3
"""script that starts flask web application frame work
 and listens on 0.0.0.0, port 5000"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    """A function that returns a string 'Hello HBNB!'"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
