# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:30:10 2019

@author: Utilisateur
"""
from appEuro import db
#from . import db, login_manager
# from flask_sqlalchemy import SQLAlchemy  # dans __init__


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
