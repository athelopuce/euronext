# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:30:10 2019

@author: Utilisateur
"""
from . import db


class User(db.Model):
    '''
    User
    '''
    __tablename__ = "T_Users"

    idUser = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.Text)
    password = db.Column(db.Text)
    connectionNumber = db.Column(db.Integer)

    def __init__(self, idUser=0, login="John",
                 password="Doe", connectionNumber=0):
        self.idUser = idUser
        self.login = login
        self.password = password
        self.connectionNumber = connectionNumber

    def __str__(self):
        return "%d: %s %s - %d" % (self.idUser, self.login, self.password,
                                   self.connectionNumber)


class Act(db.Model):
    '''
    Article = Act
    '''

    __tablename__ = "T_Acts"

    idAct = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    symbol = db.Column(db.Text)
    unitaryPrice = db.Column(db.Float)

    def __str__(self):
        return "%d: %s de marque %s = %.2f euros" % (self.idAct,
                                                     self.name,
                                                     self.symbol,
                                                     self.unitaryPrice)


class Ord(db.Model):
    '''
    Ord
    '''

    __tablename__ = "T_Ords"

    idOrd = db.Column(db.Integer, primary_key=True)
    sens = db.Column(db.Text)
    ordDate = db.Column(db.Date)

    idAct = db.Column(db.Integer, db.ForeignKey("T_Acts.idAct"))

    def __str__(self):
        return "%d: %s de marque %s = %.2f euros" % (self.idOrd,
                                                     self.sens,
                                                     self.ordDate,
                                                     self.unitaryPrice)


class OrdLine(db.Model):
    '''
    relation entre
    CommandLine = 1 article + 1 commande
    OrdLine (operation) = 1 ord + 1 cpt
    '''

    __tablename__ = "T_OrdLines"

    idOrdLine = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)  # nbre d'action

    idAct = db.Column(db.Integer, db.ForeignKey("T_Acts.idAct"))
    act = db.relationship("Act")

    idCpt = db.Column(db.Integer, db.ForeignKey("T_Cpts.idCpt"))
    cpt = db.relationship("Cpt")

    def __str__(self):
        return "%s x %d" % (str(self.act), self.quantity)


class Cpt(db.Model):
    '''
    Command = 1user + des commandes
    Cpt= 1user + des cpts
    '''

    __tablename__ = "T_Cpts"

    idCpt = db.Column(db.Integer, primary_key=True)
    cptDate = db.Column(db.Date)

    idUser = db.Column(db.Integer, db.ForeignKey("T_Users.idUser"))
    user = db.relationship("User")

    ordLines = db.relationship("OrdLine", backref="OrdLine.idCpt")

    def __str__(self):
        result = "%s - Command %d for %s\n" % (str(self.commandDate),
                                               self.idCommand,
                                               str(self.user))
        for line in self.ordLines:
            result += "\t%s\n" % (str(line))
        return result



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
