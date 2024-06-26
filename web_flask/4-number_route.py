#!/usr/bin/python3
""" route module """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root_route():
    """ root route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB_route():
    """ HBNB route """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_route(text):
    """ C route """
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """ Python route """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """ number route """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
