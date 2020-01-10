# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:30:10 2019

@author: Utilisateur
"""
from flask import request, flash, url_for, redirect, render_template, session
from .. import db
from ..models import Action, Ordre, Act
from . import main
from .forms import MyForm, NewAct

import logging


@main.route('/')
def index():
    form = MyForm()
#    return render_template('base.html', listActions=Action.query.all())
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           listActions=Act.query.all())


@main.route('/bienvenue')
def bienvenue():
    return render_template('bienvenue.html')


# test router OK
@main.route('/essai')
def essai():
    user_agent = request.headers.get('user-agent')
    return '<p>Your brower is {}</p>'.format(user_agent)


@main.route('/listAct')
def listAct():
    return render_template('listAct.html',
                           title='listAct',
                           listActions=Action.query.all())


# new Version faire newAct pour ajouter action
@main.route('/newAct', methods=['GET', 'POST'])
def newAct():
    form = NewAct()
    if form.validate_on_submit():
        act = Act(name=form.name.data, symbol=form.symbol.data)
        db.session.add(act)
        db.session.commit()
        flash('Congratulations, action was successfully added!')
        return redirect(url_for('.index'))  # or main.index
    return render_template('newAct.html',
                           title='newAct', form=form,
                           listActions=Act.query.all())


@main.route('/newOrdre', methods=['GET', 'POST'])
def newOrdre():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['symbole']:
            flash('Please enter all the fields', 'error')
        else:
            ordre = Ordre(nombre=request.form['nombre'],
                          prix=request.form['prix'],
                          date=request.form['date'],
                          action_id=request.form['symb'])

            db.session.add(ordre)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('.index'))
    return render_template('newOrdre.html')
