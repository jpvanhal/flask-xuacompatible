Flask-XUACompatible
===================

This is a simple Flask extension that sets X-UA-Compatible HTTP header for all
responses.


Installation
------------

Installation of the extension is easy with pip::

    $ pip install Flask-XUACompatible


Usage
-----

Usage is very simple::

    from flask import Flask
    from flask.ext.xuacompatible import XUACompatible

    app = Flask(__name__)
    XUACompatible(app)


Resources
---------

- `Issue Tracker <http://github.com/jpvanhal/flask-xuacompatible/issues>`_
- `Code <http://github.com/jpvanhal/flask-xuacompatible/>`_
- `Development Version
  <http://github.com/jpvanhal/flask-xuacompatible/zipball/master#egg=Flask-XUACompatible-dev>`_
