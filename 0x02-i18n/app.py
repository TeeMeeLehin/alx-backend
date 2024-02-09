#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone, UnknownTimeZoneError, utc
import datetime


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ tthe config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """func to get logged-in user"""
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """before request func"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """func to get locale"""
    locale_arg = request.args.get('locale')
    if locale_arg and locale_arg in app.config['LANGUAGES']:
        return locale_arg
    if g.user:
        if g.user.get('locale') and g.user.get(
          'locale') in app.config['LANGUAGES']:
            return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """func to get timezone"""
    tz = request.args.get('timezone')
    if tz:
        try:
            return timezone(tz)
        except UnknownTimeZoneError:
            pass
    if g.user and g.user.get('timezone'):
        utz = g.user.get('timezone')
        try:
            return timezone(utz)
        except UnknownTimeZoneError:
            pass
    return timezone('UTC')


@app.route('/', strict_slashes=False)
def index():
    """index function"""
    timez = get_timezone()
    utc_now = datetime.datetime.utcnow().replace(tzinfo=utc)
    time = utc_now.astimezone(timez)
    time = time.strftime("%b %d, %Y, %I:%M:%S %p")
    return render_template('index.html', time=time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
