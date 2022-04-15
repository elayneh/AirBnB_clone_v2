#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)

def HB():
    return ("Hello HBNB")

@app.route('/hbnb', strict_slashes=False)

def H():
    return ("HBNB")

