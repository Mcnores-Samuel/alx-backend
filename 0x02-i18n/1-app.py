#!/usr/bin/env python3
"""This is the main module of the application.
It contains the main code to run the application.
"""
from flask import Flask, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class for the app.
    """
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"


@app.route('/')
def index():
    """Main route for the app.
    """
    return render_template('1-index.html')
