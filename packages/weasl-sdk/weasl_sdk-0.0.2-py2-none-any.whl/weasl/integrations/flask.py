# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from functools import wraps, update_wrapper

from flask import current_app, request, session

from weasl.api import find_logged_in_user
from weasl.exceptions import LoginRequired, AttrRequired


def _get_weasl_client_id():
    """Gets the client_id for Weasl."""
    return current_app.config['WEASL_CLIENT_ID']


def _get_weasl_token():
    """Gets the token for the weasl user."""
    cookie = request.cookies.get('WEASL_AUTH-{}'.format(_get_weasl_client_id()))
    header = request.headers.get('Authorization', '')
    return cookie or header[7:]  # Authorization header value should always start with 'Bearer '


def _get_weasl_user():
    """Gets the user."""
    return find_logged_in_user(_get_weasl_client_id(), _get_weasl_token())


def admin_required(f):
    """Decorator for making sure the user is an admin."""
    return attr_required(f, 'is_admin', True, True)


def attr_required(f, attr, requires_trusted=False, expected_value=None):
    """Decorator for making sure the user has some attribute."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = _get_weasl_user()
        if user is None:
            raise LoginRequired()
        else:
            attribute = user.get('attributes', {}).get(attr, {})
            actual_value = attribute.get('value')
            is_trusted = attribute.get('trusted')
            value_matches = expected_value is None or expected_value == actual_value
            if (value_matches and (is_trusted and requires_trusted)):
                session.current_user = user['data']
                return f(*args, **kwargs)
            else:
                raise AttrRequired()
    return decorated_function


def login_required(f):
    """Decorator for making sure the user is logged into a view."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = _get_weasl_user()
        if user is None:
            raise LoginRequired()
        else:
            session.current_user = user['data']
            return f(*args, **kwargs)
    return decorated_function
