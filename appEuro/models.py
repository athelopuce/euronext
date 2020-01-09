# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:30:10 2019

@author: Utilisateur
"""
from . import db, bcrypt
from datetime import datetime


class User(db.Model):
    '''
    User
    '''
    __tablename__ = "T_Users"

    idUser = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.Text)
    password = db.Column(db.Text)
    connectionNumber = db.Column(db.Integer)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.idUser is None:
            self.idUser = 0
        if self.login is None:
            self.login = "John"
        if self.password is None:
            self.password = "Doe"
        if self.connectionNumber is None:
            self.connectionNumber = "0"

    def __str__(self):
        return "%d: %s %s - %d" % (self.idUser, self.login, self.password,
                                   self.connectionNumber)

    def __repr__(self):
        return '<User %r>' % self.login


class Act(db.Model):
    '''
    Article = Act
    '''

    __tablename__ = "T_Acts"

    idAct = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    symbol = db.Column(db.String(10), nullable=False)
    unitaryPrice = db.Column(db.Float)  # prix actuel. A revoir

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.unitaryPrice is None:
            self.unitaryPrice = 0

    def __repr__(self):
        return '<Act %r>' % self.name

    def __str__(self):
        return "%d: %s de marque %s = %.2f euros" % (self.idAct,
                                                     self.name,
                                                     self.symbol,
                                                     self.unitaryPrice)
# Recursion ERROR
#    @property
#    def unitaryPrice(self):
#        return self.unitaryPrice
#
#    @unitaryPrice.setter
#    def unitaryPrice(self, price):
#        self.unitaryPrice = price


class Ord(db.Model):
    '''
    Ordre
    '''

    __tablename__ = "T_Ords"

    idOrd = db.Column(db.Integer, primary_key=True)
    sens = db.Column(db.Text)
    ordDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    PriceAchat = db.Column(db.Float)  # prix de la transaction
    quantity = db.Column(db.Integer)  # nbre d'action

    idAct = db.Column(db.Integer, db.ForeignKey("T_Acts.idAct"))

    def __repr__(self):
        return '<Ord %r>' % self.idOrd

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
    # relation: 1::1
    idAct = db.Column(db.Integer, db.ForeignKey("T_Acts.idAct"))
    act = db.relationship("Act")

    idCpt = db.Column(db.Integer, db.ForeignKey("T_Cpts.idCpt"))
    cpt = db.relationship("Cpt")

    def __repr__(self):
        return '<OrdLine %r>' % self.idAct

    def __str__(self):
        return "%s x %d" % (str(self.act), self.quantity)


class Cpt(db.Model):
    '''
    Command = 1user + des commandes
    Cpt= 1user + des cpts
    '''

    __tablename__ = "T_Cpts"

    idCpt = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    cptDate = db.Column(db.DateTime, nullable=False,
                        default=datetime.utcnow)  # date d'ouverture du compte

    idUser = db.Column(db.Integer, db.ForeignKey("T_Users.idUser"))
    user = db.relationship("User", backref=db.backref("comptes", lazy=True))

    ordLines = db.relationship("OrdLine", backref="OrdLine.idCpt")

    def __repr__(self):
        return '<Cpt %r>' % self.name

    def __str__(self):
        result = "%s - Command %d for %s\n" % (str(self.commandDate),
                                               self.idCommand,
                                               str(self.user))
        for line in self.ordLines:
            result += "\t%s\n" % (str(line))
        return result


# Ancienne version
class Action(db.Model):
    '''
    liste des actions nom, symbole, secteur ....
    '''

    __tablename__ = 'actions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    symbol = db.Column(db.String(10), index=True, unique=True)

#    def __init__(self, name, symbol):
#        self.name = name
#        self.symbol = symbol

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

#    def __init__(self, name, symbole):
#        self.name = name
#        self.symbole = symbole
