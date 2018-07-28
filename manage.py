#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 9:47
# @Author  : 0wning
# @File    : manage.py

"""Create an application instance."""
from flask.helpers import get_debug_flag
from flask_script import Manager

from app.app import create_app

app = create_app()

manager = Manager(app)

if __name__ == '__main__':
    manager.run()