#!/usr/bin/python3
"""A script that starts a Flask web application on port 5000"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Prints Hello HBNB! on the root route"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(port=5000)
