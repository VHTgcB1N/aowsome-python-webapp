# -*- coding: utf-8 -*-

from orm import Model, StringField, IntegerField


class User(Model):
    """docstring for User"""
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()
