#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 10:21
# @Author  : 0wning
# @File    : views.py

"""CTF Game Views"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from app.extensions import login_manager
from app.utils import flash_errors

blueprint = Blueprint('ctf', __name__, url_prefix='/ctf')


@blueprint.route('/')
def index():
    """CTF index page."""
    return render_template('ctf/index.html')


@blueprint.route('/challenge')
def challenge():
    """CTF challenge page."""
    return render_template('ctf/challenge.html')


@blueprint.route('/game')
def game():
    """CTF game page."""
    return render_template('ctf/game.html')
