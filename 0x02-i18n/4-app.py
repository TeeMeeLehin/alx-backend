#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ tthe config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """func to get locale"""
    locale_arg = request.args.get('locale')
    if locale_arg and locale_arg in app.config['LANGUAGES']:
        return locale_arg
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """index function"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
