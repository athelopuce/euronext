# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:23:28 2019

@author: lau
structures
https://realpython.com/python-application-layouts/
"""

dir(DataWeb)
from .lib.dataweb import DataWeb
from . lib.trading import MMM

print('== Dowload data ==')
# déclaration
dw = DataWeb()
dw.symbol = 'ML.PA'
dw.name = 'Michelin'
dw.start = '1/7/2019'
print(dw)

#print(dw.start)
## DOWLOAD
#data = dw.dataReader()  # dowload from yahoo
#dw.save()

# READ csv
data = dw.read(dw.name)
print(data.tail())
print(data.head())

'''
lib trading
'''
print('== Lib trading ==')
mlsig = MMM(dw.data)

sig = mlsig['positions'].iloc[-1]
cl = data['Close'].iloc[-1]
print('close:', cl)
print('sig:', sig)
print(dw.data.tail())
print(mlsig.last('d'))
print(dw.data.last('d'))
print(data.last('d'))
