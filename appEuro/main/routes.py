# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:30:10 2019

@author: Utilisateur
"""
from flask import request, flash, url_for, redirect, render_template, session
from .. import db
from ..models import Action, Ordre, Act
from . import main
from .forms import MyForm, NewAct, ListAction
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


@main.route('/interactive/')
def interactive():
    return render_template('interactive.html')


# avec interactive route
@main.route('/background_process')
def background_process():
    try:
        lang = request.args.get('proglang', 0, type=str)
        if lang.lower() == 'python':
            return jsonify(result='You are wise')
        else:
            return jsonify(result='Try again.')
    except Exception as e:
        return str(e)


# route de la page newAct delete
@main.route('/foo', methods=['GET', 'POST'])
def foo():
    form = NewAct()  # inutile
    if request.method == 'GET':
        pin = requests.args.get('id')
    if request.method == 'POST':
        pin = form.name.data
    print(pin)
    flash(pin)
    flash('pin {}'.format(pin))
    return redirect(url_for('.index'))


# liste des actions
@main.route('/sdg')
def sdg():
    form = ListAction()
    return render_template('sdg.html', form=form)


@main.route('/listAction')
def listAction():
    res = Act.query.all()
    list_actions = [r.as_dict() for r in res]
    return jsonify(list_actions)


@main.route('/process', methods=['POST'])
def process():
    action = request.form['action']
    if action:
        return jsonify({'action': action})
    return jsonify({'error': 'missing data..'})


# exemple test1 addnumber
@main.route('/addition/')
def addition():
    return render_template('addnumb.html', reload=time.time())


@main.route("/api/add", methods=["GET"])
def add():
    a = request.args.get("a", 0, type=float)
    b = request.args.get("b", 0, type=float)
#    a = int(request.args.get('a', 0))
#    b = int(request.args.get('b', 0))
    return jsonify({
            "a": a,
            "b": b,
            "add": a+b,
            })
