# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:30:10 2019

@author: Utilisateur

Archive Laurent Version 0
"""
from . import db, bcrypt
from datetime import datetime


class Portef(db.Model):
    '''
    liste du contenu d'un portefefeuille
    compte
    liste des ordres
    '''

    __tablename__ = 'portefs'
    id = db.Column(db.Integer, primary_key=True)
#    comptes = db.relationship('Compte', backref='portefs', lazy='dynamic')
    ordres = db.relationship('Ordre', backref='operations', lazy='dynamic')
#    seuils = db.relationship('Seuil', backref='limites', lazy='dynamic')


class Compte(db.Model):
    '''
    liste des comptes, exemple compte PEA, ordinaire, assur.-vie
    numéro de cpt, date ouvert, état(clos, actif)
    '''

    __tablename__ = 'comptes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    date = db.Column(db.DateTime)
    etat = db.Column(db.Integer)  # 0 = clos, 1 = ouvert
#    portef_id = db.Column(db.Integer, db.ForeignKey('portefs.id'))


class Action(db.Model):
    '''
    liste des actions nom, symbole, secteur ....
    '''

    __tablename__ = 'actions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    symbol = db.Column(db.String(10), index=True, unique=True)

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __repr__(self):
        return '<Action %r>' % self.name


class Ordre(db.Model):
    '''
    transactions achats ventes
    '''

    __tablename__ = 'ordres'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Integer)
    prix = db.Column(db.String(10))
    date = db.Column(db.DateTime)

    action_id = db.Column(db.Integer, db.ForeignKey('actions.id'))  # 1 ordre
    ordres = db.relationship('Ordre', backref='operations', lazy='dynamic')

    portef_id = db.Column(db.Integer, db.ForeignKey('portefs.id'))  # 1 portef

    def __init__(self, name, symbole):
        self.name = name
        self.symbole = symbole


class Seuil(db.Model):
    '''
    seuils Max et min vente
    '''

    __tablename__ = 'seuils'
    id = db.Column(db.Integer, primary_key=True)
    seuilMax = db.Column(db.Integer)
    seuilMin = db.Column(db.Integer)
    date = db.Column(db.DateTime)
#    action_id = db.Column(db.Integer, db.ForeignKey('portfs.id'))


class User(db.Model):
    """
    Class that represents a user of the application

    The following attributes of a user are stored in this table:
        email address
        password (hashed using Bcrypt)
        authenticated flag (indicates if a user is logged in or not)
        date that the user registered on
    """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.Binary(60), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    registered_on = db.Column(db.DateTime, nullable=True)
    role = db.Column(db.String, default='user')

    def __init__(self, email, plaintext_password, role='user'):
        self.email = email
        self.hashed_password = bcrypt.generate_password_hash(
                plaintext_password)
        self.authenticated = False
        self.registered_on = datetime.now()
        self.role = role

    def set_password(self, plaintext_password):
        self.hashed_password = bcrypt.generate_password_hash(
                plaintext_password)

    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(
                self.hashed_password, plaintext_password)

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the id of a user to satisfy Flask-Login's requirements."""
        return str(self.id)

    def __repr__(self):
        return '<User {}>'.format(self.email)
