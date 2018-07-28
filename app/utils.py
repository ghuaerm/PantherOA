#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 9:44
# @Author  : 0wning
# @File    : utils.py

# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from flask import flash


def flash_errors(form, category='warning'):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash('{0} - {1}'.format(getattr(form, field).label.text, error), category)
