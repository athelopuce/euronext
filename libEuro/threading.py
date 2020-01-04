# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:10:18 2019

@author: Utilisateur
"""

import threading


class myThread(threading.Thread):
    '''
    Python Thread Creation Using Class
    '''
    def __init__(self, i):
        '''  No other methods (except for the constructor)
         should be overridden in a subclass '''
        threading.Thread.__init__(self)
        self.h = i

    def run(self):
        '''  No other methods (except for the constructor)
         should be overridden in a subclass '''
        print('Value send', self.h)


class myTimer:
    def __init__(self, tempo, target, args=[], kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo

    def _run(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)

    def start(self):
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.daemon = True
        self._timer.start()

    def stop(self):
        self._timer.cancel()

    def cancel(self):
        self._timer.cancel()

    def join(self):
        self._timer.join()
