#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """ Main route and render template
    """
    return render_template('0-index.html')
