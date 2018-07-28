#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 9:24
# @Author  : 0wning
# @File    : views.py
"""Public Views"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from app.extensions import login_manager
from app.utils import flash_errors
from app.models import Topic, Module, Archive

blueprint = Blueprint('public', __name__, url_prefix='/')


@blueprint.route('/')
def index():
    """Public index page."""
    archive_list = Archive.query.all()
    return render_template('public/index.html', archive_list=archive_list)


@blueprint.route('/archives/<int:yyyy>/<int:mm>/<int:dd>/<int:archive_id>.html')
def archive(archive_id, yyyy=None, dd=None, mm=None, ):
    """Archives page."""
    module_list = Module.query.all()
    archive_list = Archive.query.filter_by(id = archive_id).all()
    return render_template('public/archive.html', module_list=module_list, archive_list=archive_list)


@blueprint.route('/about')
def about():
    """About page."""
    return render_template('public/about.html')


@blueprint.route('/topics')
@blueprint.route('/topics/<topic>/')
@blueprint.route('/topics/<topic>/<module>')
def topics(topic=None, module=None):
    """Topics page."""
    module_list = Module.query.all()
    archive_list = Archive.query.all()
    return render_template('public/topics.html', module_list=module_list, archive_list=archive_list)
