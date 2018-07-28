#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 9:28
# @Author  : 0wning
# @File    : app.py

"""The app module, containing the app factory function."""

from flask import Flask, render_template, request

from . import public, personal, ctf
from .extensions import bcrypt, cache, csrf_protect, db, debug_toolbar, login_manager, migrate
from .settings import DevConfig


def create_app(config_object=DevConfig):
    """An application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/."""
    app = Flask(__name__.split('.')[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login_manager.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(personal.views.blueprint)
    app.register_blueprint(ctf.views.blueprint)
    return None


def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, 'code', 500)
        return render_template('{0}.html'.format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
