#!/usr/bin/python3
""" route module """

from flask import Flask, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """ number template route """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    """ number odd or even route """
    if n % 2 == 0:
        result = 'even'
    else:
        result = 'odd'

    return render_template('6-number_odd_or_even.html', n=n, result=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
