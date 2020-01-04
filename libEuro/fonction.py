# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:56:32 2019

@author: Utilisateur

Convertion de time avec datetime
"""

import datetime as dt
import time
from datetime import timedelta, date


def inc(a):
    ''' incremente une valeur '''
    return a + 1


def dtimeToSecond(dtime):
    return dtime.total_seconds()


def delais(dtime):
    '''
	Return temps en sec entre une datetime et now()
	
	Parameters
	-----------
	dtime: datetime
	'''
    n = dt.datetime.now()
    s = dtimeToSecond(dtime - n)
    # print('dtime - now_()-->', s)
    return s


def get_secs_to_quarter(dtime=None):
    '''
    Return le nombre de secondes pour le prochain quart d\'heure

    Parameters
    ----------
    dtime: datetime option
           si date omise, c'est la date actuelle (now)

    Returns
    -------
    result: numeric
        le nombre de secondes

    Example
    -------
    >>> import fonction as fct
    >>> print('now', fct.now_())
    >>> s = fct.get_secs_to_quarter()
    >>> print('s est:', s)
    now 2019-10-28 16:36:04.360317
    s est: 536

    '''
    dtime = dtime or dt.datetime.now()
    secs = dtime.minute * 60 + dtime.second
    next_ = ((secs + 900) // 900) * 900
    return next_ - secs


def get_heure():
    n = dt.datetime.now()
    myDateTime = n
    print(myDateTime)
    heure_ = myDateTime.hour + 1  # pour mise au points
    print(heure_)
    myDateTime = myDateTime.replace(hour=heure_)  # demarre à 9h
    minute_ = myDateTime.minute + 1  # pour mise au points
    myDateTime = myDateTime.replace(minute=minute_)  # demarre à 9h15mn
    print('delais est', myDateTime - n)
    return myDateTime - n


def get_min_to_hour(dtime=None):
    '''
    Return le nombre de minutes avant la prochaine heure

    Parameters
    ----------
    dtime: datetime option
           si date omise, c'est la date actuelle (now)

    Returns
    -------
    result: numeric
        le nombre de minutes

    Example
    -------
    >>> import fonction as fct
    >>> print('now', fct.now_())
    >>> s = fct.get_min_to_hour()
    >>> print('s est:', s)
    now 2019-10-28 16:42:44.193777
    prochaine heure en (mn) : 18
    s est: 18

    '''
    dtime = dtime or dt.datetime.now()
    min_ = dtime.minute
    next_ = ((min_ + 60) // 60) * 60
    # print('prochaine heure en (mn) :', next_ - min_)
    return next_ - min_


def get_jourSem():
    '''
    Return le jour de la semaine lundi = 0, mardi = 1, ven = 4, samedi = 5,
    dimanche = 6

    *datetime.weekday()*

    Parameters
    ----------
    None:

    Returns
    -------
    result: numeric
        lundi = 0, mardi = 1, ven = 4, samedi = 5, dimanche = 6

    Example
    -------
    >>> import fonction as fct
    >>> jourSem = ['lundi', 'mardi', 'merc', 'jeudi',
           'vendredi', 'samedi', 'dimanche']
    >>> jour = fct.get_jourSem()
    >>> print('numéro du jour est:', jour)
    >>> print('aujourd\'hui c\'est', jourSem[jour])
    numéro du jour est: 0
    aujourd'hui c'est lundi

    '''
    dtime = dt.datetime.now()
    jour = dtime.weekday()  # lundi = 0, samedi = 5, dimanche = 6
    return jour
