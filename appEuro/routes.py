# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:30:10 2019

@author: Utilisateur
"""
# cd C:\Users\Utilisateur
# cd "Documents\Python Scripts\EuronextDev"

from euronext import app  # import variable "app" from package app
from euronext import db  # import variable "lib" from package app
from euronext.forms import MyForm  # class des formulaires
from euronext.models import Action, Ordre  # class de la base des donnees

from flask import Flask, request, flash, url_for, redirect, render_template

import logging

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///actions.sqlite3'
#app.config['SECRET_KEY'] = "random string"


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
