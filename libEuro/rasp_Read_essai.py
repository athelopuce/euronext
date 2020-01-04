# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:35:31 2019

@author: trading

Lecture data et mise au point programme
"""

import pandas as pd
import numpy as np
from pandas_datareader import data as web

#
#data = web.DataReader('ML.PA', 'yahoo', start='1/1/2017')
##print(data.tail())
#
## Save to Csv
#data.to_csv('Michelin.csv')



def rasp_read(action):
    '''
    Read the data
    '''
    data = pd.read_csv(action, index_col=0)
    data.index = pd.to_datetime(data.index, dayfirst=True)
    
    # Calculate exponential moving average
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0.0
    signals['12d_EMA'] = data.Close.ewm(span=12).mean()  # mean() valeur moyenne
    signals['26d_EMA'] = data.Close.ewm(span=26).mean()
    
    # Calculate MACD
    signals['MACD'] = signals['26d_EMA'] - signals['12d_EMA']
    
    '''
    Calculate Signal
    '''
    
    # moy. exponentiel sur 9 jour
    signals['support'] = signals.MACD.ewm(span=9).mean()
    # Define Signal
    signals['signal'] = np.where(signals['MACD'] > signals['support'], 1, 0)
    # Generate trading orders
    signals['positions'] = signals['signal'].diff()
    
    # Calculate Returns
    signals['trading_r'] = np.where(signals['MACD'] > signals['support'], 1, -1)
    signals['returns'] = data.Close.pct_change()  # pourcentage change
    
    # Calculate Strategy Returns
    signals['strategy_returns'] = signals.returns * signals.trading_r.shift(1)
    
    # Calculate Cumulative Returns
    cumulative_returns = (signals.strategy_returns + 1).cumprod()-1
    return signals, data
