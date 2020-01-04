# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:35:31 2019

@author: trading

Lecture data et mise au point programme
"""

import pandas as pd
import numpy as np
from pandas_datareader import data as web
import logging

module_logger = logging.getLogger('DataWeb')

class DataWeb:
    '''
    herite de pandas_datareader
    '''
    def __init__(self, symbol=None, start='2017/1/1'):
        '''
        Parameters:
        -----------
        symbol Yahoo: ML.PA
        date par défaut = '1/1/2017'
        '''
        self.logger = logging.getLogger('dataweb.DataWeb')
        self._symbol = symbol
        self._start = start
        self.data = None
        self.logger.info('creating an instance of DataWeb')

    def __getattr__(self, nom):
        '''
        Si Python ne trouve pas l'attribut nommé nom, il appelle
        cette méthode. On affiche une alerte
        '''
        print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))

    def _setstart(self, date):
        '''
        date format '1/1/2017'
        '''
        if isinstance(date, DataWeb):
            print('instance de DataWeb')
            self._start = date
        else:
#            print('date en string')
            self._start = date

    def _getstart(self):
        return self._start

    def _setsymbol(self, symbol):
        self._symbol = symbol

    def _getsymbol(self):
        return self._symbol

    def _setname(self, name):
        self._name = name

    def _getname(self):
        return self._name

    def dataReader(self):
        '''
        Dowload from Yahoo finance
        '''
        self.logger = logging.getLogger('dataweb.dataReader')
        self.data = web.DataReader(self._symbol, 'yahoo', self._start)
#        self.data = web.get_data_yahoo(self._symbol, self._start)
        self.logger.info(
                'téléchargement Yahoo finance de {} <--'.format(self._name))
        return self.data

    def getdata(self):
        return self.data

    def __str__(self):
        return 'symbol: {}, name: {}, start: {}'.format(
                self._symbol, self._name, self._start)

    def save(self):
        self.logger = logging.getLogger('dataweb.save')
        if isinstance(self.data, pd.DataFrame):
            try:
                self.data.to_csv(self._name+'.csv')
                self.logger.info('data sauvegardé')
            except FileNotFoundError:
                print('le fichier {} n\'existe pas!!!'.format(self._name))

    def read(self, name):
        self.logger = logging.getLogger('dataweb.read')
        try:
            name += '.csv'
            self.data = pd.read_csv(name, index_col=0)
            self.data.index = pd.to_datetime(self.data.index, dayfirst=True)
            self.logger.info('lecture du fichier {}'.format(name))
            return self.data
        except FileNotFoundError:
            print('le fichier {} n\'existe pas!!!'.format(name))

    name = property(_getname, _setname)
    symbol = property(_getsymbol, _setsymbol)
    start = property(_getstart, _setstart)


def some_function():
    ''' module pour essai logging '''
    module_logger.info('received a call to "some_function"')
