# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:30:10 2019

@author: Utilisateur
"""
from appEuro import db  # import variable "lib" from package app
from appEuro import app  # import variable "app" from package app
from appEuro import Action, Ordre, Seuil
from flask import request, flash, url_for, redirect, render_template

import logging


@app.route('/')
def show_all():
    return render_template('show_all.html', listActions=Action.query.all())


@app.route('/bienvenue')
def bienvenue():
    return render_template('bienvenue.html')


@app.route('/essai')
def essai():
    user_agent = request.headers.get('user-agent')
    return '<p>Your brower is {}</p>'.format(user_agent)


@app.route('/listAct')
def listAct():
    return render_template('listAct.html',
                           title='listAct',
                           listActions=Action.query.all())


@app.route('/newAct', methods=['GET', 'POST'])
def newAct():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['symbole']:
            flash('Please enter all the fields', 'error')
        else:
            action = Action(request.form['name'], request.form['symbole'])

            db.session.add(action)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('newAct.html')


@app.route('/newOrdre', methods=['GET', 'POST'])
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
            return redirect(url_for('show_all'))
    return render_template('newOrdre.html')
