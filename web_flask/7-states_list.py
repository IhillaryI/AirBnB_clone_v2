#!/usr/bin/python3
"""A script that starts a Flask web application on port 5000"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)
states = list(storage.all(State).values())

@app.route('/states_list', strict_slashes=False)
def odd_or_even():
    """populates a html template with a list of states"""
    print(states)
    return render_template('7-states_list.html', states=states)


#@app.teardown_appcontext
#def close():
 #   """remove the SQLAlchemy session after requests"""
  #  storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
