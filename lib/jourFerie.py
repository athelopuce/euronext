# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 08:49:56 2019

@author: Utilisateur

Jours fériés
"""

import datetime as dt


def listjourferie():
    ''' liste des jours fériés 2020 '''
    jf = []
    auj = dt.date.today()
#    print(auj.year)

    # dimanche de pâques
    x = datepaques(auj.year)
    paq = dt.date(x[0], x[1], x[2])

    # lundi de pâques
    d = dt.date(paq.year, paq.month, paq.day+1)
    jf.append(d)

    # le vendredi saint -2j par rapport au dimanche de pâques
    d = dt.date(paq.year, paq.month, paq.day-2)
    jf.append(d)

    # jour de l'an
    d = dt.date(auj.year, 1, 1)
    jf.append(d)

    # fête du travail en mai
    d = dt.date(auj.year, 5, 1)
    jf.append(d)

    # Noel
    d = dt.date(auj.year, 12, 25)
    jf.append(d)

    # Saint Etienne
    d = dt.date(auj.year, 12, 26)
    jf.append(d)

    # TRIER
    jf.sort()
#    for i, elt in enumerate(jf):
#        print("À l'indice {} se trouve {}.".format(i, elt))
    return jf


def isjourferie(d):
    '''
    Return True if the date is férié

    Parameters
    ----------
    date : type *datetime.date*

    '''
    for i, elt in enumerate(listjourferie()):
        if d == elt:
#            print('fct jourFerie --> jour férié')
            return True

    
def datepaques(an):
    '''
    Calcule le dimanche de Pâques d'une année donnée an (=nombre entier)
    
    Return:
    -------
        liste [year, m, day]
    '''
    a = an // 100
    b = an % 100
    c = (3*(a+25))//4
    d = (3*(a+25)) % 4
    e = (8*(a+11)) // 25
    f = (5*a+b) % 19
    g = (19*f+c-e) % 30
    h = (f+11*g) // 319
    j = (60*(5-d)+b) // 4
    k = (60*(5-d)+b) % 4
    m = (2*j-k-g+h) % 7
    n = (g-h+m+114) // 31
    p = (g-h+m+114) % 31
    jour = p + 1
    mois = n
    return [an, mois, jour]
    
