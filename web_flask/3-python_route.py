#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def HHB():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnh():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "HBNB"


@app.route('/c/<text>')
def disp(text):
    """_summary_

    Args:
        text (_type_): _description_

    Returns:
        _type_: _description_
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python')
@app.route('/python/<text>')
def dispPy(text='is cool'):
    """_summary_

    Args:
        text (str, optional): _description_. Defaults to 'is cool'.

    Returns:
        _type_: _description_
    """
    return "Python {}".format(text.replace("_", " "))


if (__name__ == "__main__"):
    app.run('host=0.0.0.0', port=5000)
