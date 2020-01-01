# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:30:10 2019

@author: Utilisateur
"""
from flask import render_template, request
from .. import db
from ..models import Action, Ordre
from . import main
from .forms import MyForm


#@app.route('/')
#def show_all():
#    return render_template('test.html')


@main.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)


@main.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
