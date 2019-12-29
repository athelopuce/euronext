# -*- coding: utf-8 -*-
"""

python routes.py
ou
set FLASK_APP=routes.py
flask app

Web
----
http://localhost:5000  # windows
http://192.168.10.15:5000/  # raspberry

== install ==
pip install flask-sqlalchemy
pip install Flask-WTF

"""
# cd C:\Users\Utilisateur
# cd "Documents\Python Scripts\EuronextDev"


from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import forms
import logging

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///actions.sqlite3'
app.config['SECRET_KEY'] = "random string"

SQLALCHEMY_TRACK_MODIFICATIONS = False  # sup Warning

db = SQLAlchemy(app)


class Action(db.Model):
    ''' liste des actions '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    symbole = db.Column(db.String(10), index=True, unique=True)
    ordres = db.relationship('Ordre', backref='transactions', lazy='dynamic')
    seuils = db.relationship('Seuil', backref='limites', lazy='dynamic')

    def __init__(self, name, symbole):
        self.name = name
        self.symbole = symbole

    def __repr__(self):
        return '<Action %r>' % self.name


class Ordre(db.Model):
    ''' transactions achats ventes '''
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Integer)
    prix = db.Column(db.String(10))
    date = db.Column(db.DateTime)
    action_id = db.Column(db.Integer, db.ForeignKey('action.id'))

    def __init__(self, name, symbole):
        self.name = name
        self.symbole = symbole


class Seuil(db.Model):
    ''' seuils Max et min vente '''
    id = db.Column(db.Integer, primary_key=True)
    seuilMax = db.Column(db.Integer)
    seuilMin = db.Column(db.Integer)
    date = db.Column(db.DateTime)
    action_id = db.Column(db.Integer, db.ForeignKey('action.id'))


@app.route('/')
def show_all():
    return render_template('show_all.html', listActions=Action.query.all())


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


if __name__ == '__main__':
    db.create_all()
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    app.run(debug=True)
