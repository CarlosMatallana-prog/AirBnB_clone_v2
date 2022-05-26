#!/usr/bin/python3
""" Display “Hello HBNB! """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def route():
    """Returns 'Hello, HBNB!' on the main route route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """Returns 'HBNB' on route /hbnb"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
