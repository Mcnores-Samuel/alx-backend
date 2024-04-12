#!/usr/bin/env python3
"""This is the main module of the application.
It contains the main code to run the application.
"""
from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config class for the app.
    """
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get locale for the app.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])