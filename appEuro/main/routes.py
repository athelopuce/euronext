# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:30:10 2019

@author: Utilisateur
"""
from flask import request, flash, url_for, redirect, render_template, session
from .. import db
from ..models import Action, Ordre, Act
from . import main
from .forms import MyForm, NewAct, ListAction, MemberForm, TeamForm
from flask import jsonify  # pour route interactive
import requests  # pour page newAct delete '/foo'
import time  # for test1 addnumber

import logging


@main.route('/')
def index():
    form = MyForm()
#    return render_template('base.html', listActions=Action.query.all())
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False),
                           listActions=Act.query.all())


# new Version faire newAct pour ajouter action
@main.route('/newAct', methods=['GET', 'POST', 'DELETE'])
def newAct():
    form = NewAct()
    if form.validate_on_submit():
        act = Act(name=form.name.data, symbol=form.symbol.data)
        db.session.add(act)
        db.session.commit()
        flash('Congratulations, action was successfully added!')
        return redirect(url_for('.index'))  # or main.index
    elif request.method == 'DELETE':
        # Retrieve data from the request and remove it from the database
        myId = request.form.get('column1')
        print(myId)
#        print(nameid)
        print('ok')
    return render_template('newAct.html',
                           title='newAct', form=form,
                           listActions=Act.query.all())


@main.route("/delRow", methods=["POST"])
def delRow():
    a = request.form.get("id", 0)
    b = request.form.get("name", type=str)
    return jsonify(idAct=a, name=b)


@main.route("/editRow", methods=["POST"])
def editRow():
    a = request.form.get("id", 0)
    b = request.form.get("name", type=str)
    return jsonify(idAct=a, nameEdit=b)


@main.route('/newEdit', methods=['GET', 'POST'])
def newEdit():
    form = NewAct()
    if form.validate_on_submit():
        act = Act(name=form.name.data, symbol=form.symbol.data)
        db.session.add(act)
        db.session.commit()
        flash('Congratulations, action was successfully added!')
        return redirect(url_for('.index'))  # or main.index
    elif request.method == 'POST':
        # Retrieve data from the request and remove it from the database
        myId = request.form.get('column1')
        print(myId)
#        print(nameid)
        print('ok')
    return render_template('newEdit.html',
                           title='newEdit', form=form,
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


@main.route('/listAction')
def listAction():
    res = Act.query.all()
    list_actions = [r.as_dict() for r in res]
    return jsonify(list_actions)
