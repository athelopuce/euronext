# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 19:34:21 2019

@author: lau
"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
