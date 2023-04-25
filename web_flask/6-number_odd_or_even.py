#!/usr/bin/python3
"""A script that starts a Flask web application on port 5000"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """Prints Hello HBNB! on the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB on the /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """prints the text variable on this route"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """prints the text variable on this route"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """prints the text variable on this route"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Populates and returns a html template file"""
    return render_template('5-number.html', value=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Populates and returns a html template file."""
    iseven = False
    if n % 2 == 0:
        iseven = True
    return render_template('6-number_odd_or_even.html', value=n, iseven=iseven)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
