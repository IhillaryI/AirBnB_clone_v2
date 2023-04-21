#!/usr/bin/python3
"""A script that starts a Flask web application on port 5000"""
import flask
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """Prints Hello HBNB! on the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Prints HBNB on the /hbnb route"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
