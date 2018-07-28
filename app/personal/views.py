#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 9:27
# @Author  : 0wning
# @File    : views.py

"""Personal Views"""

from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint('personal', __name__, url_prefix='/personal')


@blueprint.route('/')
@login_required
def index():
    """Personal index page."""
    return 'this is personal index'
