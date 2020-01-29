# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 19:34:21 2019

@author: lau
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FieldList, \
     FormField, DateField, DecimalField
from wtforms.validators import DataRequired, ValidationError, Length
from appEuro.models import Act

import datetime


class MyForm(FlaskForm):
    name = StringField(
            'name',
            validators=[DataRequired()]
            )


class NewAct(FlaskForm):
    name = StringField(
            'Titre',
            validators=[DataRequired(), Length(max=20)]
            )
    symbol = StringField(
            'Symbole',
            validators=[DataRequired(), Length(max=10)]
            )
    submit = SubmitField('Register')

    def validate_name(self, name):
        action = Act.query.filter_by(name=name.data).first()
        if action is not None:
            raise ValidationError('Please use a different titre.')


class NewOrd(FlaskForm):
    sens = StringField(
            'Sens',
            validators=[DataRequired(), Length(max=10)]
            )
    ordDate = DateField(
            'Date',
            format='%d/%m/%Y',
            validators=[DataRequired('please select date d\'achat')]
            )
    PriceAchat = DecimalField(
            'Prix',
            places=2,
            rounding=None,
            use_locale=False,
            number_format=None
            )
    quantity = IntegerField(
            'Qté',
            validators=[DataRequired()]
            )

    submit = SubmitField('Register')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.ordDate.data:
            self.ordDate.data = datetime.date.today()


class ListAction(FlaskForm):
    action = StringField(
            'Action',
            validators=[DataRequired(), Length(max=40)],
            render_kw={"placeholder": "action"}
            )


# editable form pour essai
class MemberForm(FlaskForm):
    name = StringField('name')
    member_id = StringField('member_id')
    inbox_share = IntegerField('inbox_share')
    # etc.


# pour essai
class TeamForm(FlaskForm):
    title = StringField('title')
    teammembers = FieldList(FormField(MemberForm))
