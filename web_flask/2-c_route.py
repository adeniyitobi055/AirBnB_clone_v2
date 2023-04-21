#!/usr/bin/python3
"""
A script that starts a Flask web application
Your web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """ Returns a given string """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns a given string """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """
    Displays `C` followed by the value of the `text` variable
    and replaces underscore _ symbols with a space
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)