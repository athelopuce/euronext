# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:35:31 2019

@author: trading

Lecture data et mise au point programme
"""

import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)


class MACD:
    '''
    Calcul MACD avec moyenne eponentielle 12d et 26d

    Return:
    -------
    signals: DataFrame structure
    champs:
        * signal: Achat (1), Vendre(-1), neutre
        * 12d_EMA:
        ...
        * strategy_returns:
        * cumulative_return:
    '''
    def __init__(self, df):
        self.signals = pd.DataFrame(index=df.index)
        self.signals['signal'] = 0.0
        self.df = df

    def __str__(self):
        return str(self.signals.tail())

    def calcul(self):
        ''' Calculate exponential moving average '''
        # mean() val. moyenne
        self.signals['12d_EMA'] = self.df.Close.ewm(span=12).mean()
        self.signals['26d_EMA'] = self.df.Close.ewm(span=26).mean()
        # Calculate MACD
        self.signals['MACD'] = \
            self.signals['26d_EMA'] - self.signals['12d_EMA']
        # moy. exponentiel sur 9 jour
        self.signals['support'] = self.signals.MACD.ewm(span=9).mean()
        return self.signals

    def signal(self):
        ''' Calculate Signals '''
        # Define Signal
        self.signals['signal'] = \
            np.where(self.signals['MACD'] > self.signals['support'], 1, 0)
        # Generate trading orders
        self.signals['positions'] = self.signals['signal'].diff()
        # Calculate Returns
        self.signals['trading_r'] = \
            np.where(self.signals['MACD'] > self.signals['support'], 1, -1)
        self.signals['returns'] = \
            self.df.Close.pct_change()  # pourcentage change
        # Calculate Strategy Returns
        self.signals['strategy_returns'] = \
            self.signals.returns * self.signals.trading_r.shift(1)

        # Calculate Cumulative Returns
        cumulative_returns = (self.signals.strategy_returns + 1).cumprod()-1
        self.signals['cumulative_returns'] = cumulative_returns
        return self.signals


class RSI:
    ''' RSI '''
    def __init__(self, df):
        self.signals = pd.DataFrame(index=df.index)
        self.signals['signal'] = 0.0
        self.signals['Close'] = df.Close
        self.df = df

    def __str__(self):
        return str(self.signals.tail())

    def calcul(self, n=14):
        '''
        RSI sur une période de n jours (défaut n = 14)

        Param :
        ------
            df: pandas dadafram structure with Close
            n: integer

        Return :
        --------
            pandas dadafram structure with RSI and Close signals
        '''
        delta = self.df.Close.diff()  # Adj Close pas d'importance
        # init dataframe
#        signals = pd.DataFrame(index=self.df.index)
#        signals['signal'] = 0.0
#        signals['Close'] = self.df.Close
        # calculate
        up_days = delta.copy()
        up_days[delta <= 0] = 0.0
        down_days = abs(delta.copy())
        down_days[delta > 0] = 0.0
        # Calculate the EWMA
        RS_up = up_days.ewm(span=n).mean()
        RS_down = down_days.ewm(span=n).mean()
        self.signals['RSI'] = 100-100/(1+RS_up/RS_down)
        # signals['up'] = 70
        # signals['down'] = 30
        return self.signals

    def signal(self):
        ''' calcul signaux '''
        # Define Signal
        self.signals['sigUp'] = np.where(self.signals['RSI'] > 70, 1, 0)
        self.signals['sigDown'] = np.where(self.signals['RSI'] < 30, 1, 0)
        # Generate trading orders
        # position up Vente sur -1, différer(shift)de 2j
        self.signals['posUp'] = \
            self.signals['sigUp'].shift(0).diff()
        # position up Achat sur -1
        self.signals['posDown'] = \
            self.signals['sigDown'].shift(0).diff()
        return self.signals
