# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 19:34:21 2019

@author: lau
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length
from appEuro.models import Act


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


class NewAct(FlaskForm):
    name = StringField('Titre', validators=[DataRequired(), Length(max=20)])
    symbol = StringField('Symbole', validators=[DataRequired(),
                                                Length(max=10)])
    submit = SubmitField('Register')

    def validate_name(self, name):
        action = Act.query.filter_by(name=name.data).first()
        if action is not None:
            raise ValidationError('Please use a different titre.')
