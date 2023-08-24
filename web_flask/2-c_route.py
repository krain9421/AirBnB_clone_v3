#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays the text `Hello HBNB!`
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays the text `HBNB`
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """
    Displays `C` followed by the value of the text variable
        replacing underscore `_` symbols with a space ` `
    """
    return (f'C {escape(text.replace("_", " "))}')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
