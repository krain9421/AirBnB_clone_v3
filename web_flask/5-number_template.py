#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape
from flask import render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythontext(text="is cool"):
    """
    Displays `Python` followed by the value of the text
        variable replacing underscore `_` symbols with
        a space ` `.
        The default value of the text is `is cool`
    """
    return ('Python {}'.format(escape(text.replace("_", " "))))


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """
    Displays `n is a number` only if `n` is an integer
    """
    return (f'{n} is a number')


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n=None):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
