#!/usr/bin/python3
""" route module """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root_route():
    """ root route """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
