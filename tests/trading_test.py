# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:14:10 2019

@author: Utilisateur

pytest --version
python -m pytest
python -m pytest tests/trading_test.py
python -m pytest tests/

"""
# cd "Documents\Python Scripts\Euronext"

import config
import pytest


from lib.dataweb import DataWeb
from lib.trading import MACD, RSI


print('== Dowload data ==')
# déclaration
dw = DataWeb()
dw.symbol = 'ML.PA'
dw.name = 'Michelin'
dw.start = '1/7/2019'
print(dw)

# DOWLOAD
#print(dw.start)
#data = dw.dataReader()  # dowload from yahoo
#dw.save()

# READ csv
data = dw.read(dw.name)
dataInit = data
print(data.head())
print(data.tail())

'''
MACD
'''
print('\n== Lib MACD ==')
macd = MACD(dw.data)
mlsig = macd.calcul()
print(list(mlsig.columns))  # liste des colonnes
mlsig = macd.signal()
print(list(mlsig.columns))  # liste des colonnes
print(mlsig['signal'])

# pas de corruption des data
def test_MACD():
    assert list(data.columns) == list(dataInit.columns)


# définir une classe test avec data d'entrée à créer
def test_MACDcalcul():
    pass


#def test_raises_data_different():
#    with pytest.raises(TypeError):
#        mlsig == dataInit


# les fonction de visualisation
sig = mlsig['positions'].iloc[-1]  # dernier jour
cl = data['Close'].iloc[-1]
print('close:', cl)
print('sig:', sig)
print(mlsig.last('d'))
print(dw.data.last('d'))
print(data.last('d'))

'''
RSI
'''
print('\n== Lib RSI ==')
rsi = RSI(dw.data)
mlsig = rsi.calcul()
print(mlsig.tail())
print(list(mlsig.columns))  # liste des colonnes
sig = rsi.signal()
print(list(sig.columns))  # liste des colonnes
print(rsi)
print(sig.tail())

# pas de corruption des data
def test_RSI():
    assert list(data.columns) == list(dataInit.columns)


# définir une classe test avec data d'entrée à créer et calcul avec n = 2
def test_RSIcalcul():
    pass


class TestIndicator:
    pass


if __name__ == '__main__':
    pytest.main()
#    pytest.main(["-qq"], plugins=[TestIndicator()])  # class TestIndicator
