#!/usr/bin/python3
"""A script that starts a Flask web application on port 5000"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template


app = Flask(__name__)
states = list(storage.all(State).values())
cities = list(storage.all(City).values())


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """populates a html template with a list of states"""
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage instance"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
