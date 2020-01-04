# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:35:31 2019

@author: trading

Envoi SMS Free
"""

import requests
import datetime as dt
import logging

logging = logging.getLogger(__name__)


class SMSfictif():
    def __init__(self):
        self.flgAV = 0  # 1 --> acheter, -1 --> vendre

    def envoiTest(self, message):
        ''' simulation Envoi message SMS '''
        logging.warning('SMS en Mode TEST !!!!')
        return message


class SMS():
    def __init__(self):
        self.login = '16439895'
        self.mdp = 'EY9KFAdwd5YBdK'
        self.flgAV = 0  # 1 --> acheter, -1 --> vendre

    def __str__(self):
        return str('Param sms:\nmdp:{}\nflgAV={}\nlogin:{}'.format(self.mdp,
                   self.flgAV,
                   self.login))

    def envoi(self, message):
        return requests.get('https://smsapi.free-mobile.fr/sendmsg?user='
                            + self.login + '&pass='
                            + self.mdp + '&msg='
                            + message)

    def envoiTest(self, message):
        ''' simulation Envoi message SMS '''
        logging.warning('SMS en Mode TEST !!!!')
        return message

    def memorise(self, st):
        pass

    def memo(st):
        ''' Mémorise les envoi déjà fait '''
        # Envoi SMS
        flgAV = st[2]
        now = dt.datetime.now()
    #    # Test
    #    print('boucle ', i)
    #    if i == 0 or i == 1:
    #        print('sig vendre')
    #        sig = -1.0
    #    if i == 2:
    #        print('sig achat')
    #        sig = 1.0
    #    if i == 3:
    #        print('sig neutre')
    #        sig = 0
    #    # Fin test
        if sig == -1.0 and not flgAV == -1:
            flgAV = -1
            print('--> Vendre')
            r = sms('Vendre ' + st[1] + '\nle cours est ' + str(
                    round(cl, 2)) + now.strftime(
                                 '.\n   Message du : %d/%m/%Y à %H:%M.'))
            print(r)
        if sig == 1.0 and not flgAV == 1:
            flgAV = 1
            print('--> Acheter')
            r = sms('Acheter ' + st[1] + '\nle cours est ' + str(
                    round(cl, 2)) + now.strftime(
                                 '.\n  Message du : %d/%m/%Y à %H:%M.'))
            print(r)
        if sig == 0:
            flgAV = 0
        st[2] = flgAV
    #    print('++++++++++ flg AV ++++++++++')
    #    print('flagAV=', st[2])
        return sig, cl, signals
