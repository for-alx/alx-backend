#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
app.config.from_object(Config)
babe = Babel(app)


class Config:
    """ Config for app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def index():
    """ basic route """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()