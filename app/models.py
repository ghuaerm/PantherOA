#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 15:07
# @Author  : 0wning
# @File    : models.py

""" Archives Models """
import datetime as dt

from .database import Column, Model, SurrogatePK, db, reference_col, relationship
from .extensions import bcrypt


class Topic(SurrogatePK, Model):
    """A topic for app."""

    __tablename__ = 'topics'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Topic({id})>'.format(id=self.id)


class Module(SurrogatePK, Model):
    """A module for a topic."""

    __tablename__ = 'modules'
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(80), unique=True, nullable=False)
    topic_id = Column(db.Integer, db.ForeignKey('topics.id'))

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Module({id})>'.format(id=self.id)


class Archive(SurrogatePK, Model):
    """A archive for a module."""

    __tablename__ = 'archives'
    id = Column(db.Integer, primary_key=True)
    tittle = Column(db.String(80), unique=True, nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    topic_id = Column(db.Integer, db.ForeignKey('topics.id'))
    module_id = Column(db.Integer, db.ForeignKey('modules.id'))

    def __init__(self, tittle, **kwargs):
        """Create instance."""
        db.Model.__init__(self, tittle=tittle, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Archive({id})>'.format(id=self.id)
