# -*- coding: utf-8 -*-
"""
    flask.ext.xuacompatible
    ~~~~~~~~~~~~~~~~~~~~~~~

    Simple Flask extension that sets X-UA-Compatible HTTP header for all
    responses.

    :copyright: (c) 2012 by Janne Vanhala.
    :license: BSD, see LICENSE for more details.
"""


class XUACompatible(object):
    """
    Configure the extension for use with the given app.

    Example usage::

        from flask import Flask
        from flask.ext.xuacompatible import XUACompatible

        app = Flask(__name__)
        XUACompatible(app)

    :param app: a :class:`~flask.Flask` instance
    """

    def __init__(self, app):
        @app.after_request
        def process_response(response):
            response.headers['X-UA-Compatible'] = 'IE=edge,chrome=1'
            return response
