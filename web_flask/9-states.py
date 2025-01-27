#!/usr/bin/python3
""" Importing Flask to run the web app """
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_database(exc):
    """ Closes the database at the end of the request """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ Render state_list html page to display States created """
    states = storage.all("State")
    return render_template('9-states.html', state=states)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_states(id):
    """
    Display a HTML page: (inside the tag BODY)
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
