# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:15:19 2019

@author: Utilisateur
"""
import logging

logging = logging.getLogger(__name__)


class Stock:
    ''' Définition des actions symbole, name, ordre Achat ou Vente,
    Prix unitaire, quantité '''
    def __init__(self, symbol, name, seuilB, seuilH):
        ''' (..., seuil bas, seuil haut)'''
        self._symbol = symbol  # symbole
        self._name = name  # name
        self._seuilH = seuilH  # seuil haut
        self._seuilB = seuilB  # seuil bas
        self.__flgAV = 0  # 1 --> acheter, -1 --> vendre. Double__ mode private
        self._act = None  # nom dans la liste portefeuille

    def __str__(self):
        ''' nom de l\'objet instancié par la class Stock '''
        logging.debug('Hello __str__')
        return 'Les données de l\'action ' + self._name + ' sont:' \
                + '\nsymbol:' + self._symbol \
                + '\nseuil bas:' + str(self._seuilB) \
                + '\nseuil haut:' + str(self._seuilH) \
                + '\nFlagAV :' + str(self.__flgAV)

    def __repr__(self):
        ''' __repr__ can return any python expression
        Par défaut, si aucune méthode__str__n'est définie,
        Python appelle la méthode__repr__de l'objet '''
        self._act = self._symbol.replace('.', '')
        logging.debug('Hello __repr__ :{}'.format(self._act))
        # return {'name':self.name, 'age':self.age}
        return self._act

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, v):
        self._symbol = v

    @property
    def seuilH(self):
        return self._seuilH

    @seuilH.setter
    def seuilH(self, v):
        self._seuilH = v

    @property
    def seuilB(self):
        return self._seuilB

    @seuilB.setter
    def seuilB(self, v):
        self._seuilB = v

    @property
    def flgAV(self):
        return self.__flgAV

    @flgAV.setter
    def flgAV(self, v):
        self.__flgAV = v


class Portefeuille:
    ''' portefeuille action '''
    def __init__(self, name):
        ''' (..., seuil bas, seuil haut)'''
        self._act = []  # list des actions
        self._name = name  # nom du portefeuille

    def __str__(self):
        ''' nom de l\'objet instancié par la class Stock '''
        logging.debug('Hello __str__')
        return str(self._name)

    def __repr__(self):
        ''' nom de l'objet Stock instancié '''
#        return {'name:', self._name}
        return self._name

    def _delete(self, stock):
        ''' effacer l\'action demandée '''
        while stock in self._act:
            del self._act[self._act.index(stock)]

    def _add(self, stock):
        self._act.append(stock)

    def _getList(self):
        return self._act

    def _liste(self):
        for elm in self._act:
            logging.info('{}'.format(elm._name))
