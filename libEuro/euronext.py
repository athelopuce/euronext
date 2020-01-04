# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:56:32 2019

@author: Utilisateur

Class Euronext
"""

#import datetime as dt
#import time
from datetime import timedelta, date
import datetime as dt
import libEuro.fonction as fct
import libEuro.jourFerie as jf

class Euronext:
    def __init__(self, opening, closure):
        self._tmOpen = opening  # opening time
        self._tmClos = closure  # closure time

    def __del__(self):
        """Méthode appelée quand l'objet est supprimé"""
        print("C'est la fin ! On me supprime !")

    def __repr__(self):
        '''
        Quand on entre notre objet dans l'interpréteur
        '''
        print('Hello __repr__')
        return "(__repr__) Ouverture de {} à {}.".format(
                self._tmOpen, self._tmClos)

    def __str__(self):
        '''
        Par défaut, si aucune méthode__str__n'est définie,
        Python appelle la méthode__repr__de l'objet.
        La méthode__str__est également appelée si vous désirez
        convertir votre objet en chaîne avec le constructeur str
        '''
#        print('Hello __str__')
        return "Ouverture Euronext de {} à {}.".format(
                self._tmOpen, self._tmClos)

    def __getattr__(self, nom):
        '''
        Si Python ne trouve pas l'attribut nommé nom, il appelle
        cette méthode. On affiche une alerte
        '''
        print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))

#    def __setattr__(self, nom_attr, val_attr):
#        '''
#        Méthode appelée quand on fait objet.nom_attr = val_attr.
#        On se charge d'enregistrer l'objet
#        '''
#        object.__setattr__(self, nom_attr, val_attr)
#        self.enregistrer()

    def __delattr__(self, nom_attr):
        '''
        On ne peut supprimer d'attribut, on lève l'exception
        AttributeError
        '''
        raise AttributeError('Vous ne pouvez supprimer aucun attribut\
                             de cette classe')

    def _isOpeningDay(self):
        '''
        Return True si jour d'ouverture des cours. Du lundi au vendredi,
        le marché est ouvert.

        Example
        -------
        >>> ouv = cvt.isjourOuverture()
        >>> if cvt.isjourOuverture():
        >>> print('jour ouvré?:', ouv)
        jour ouvré?: True

        '''
        d = fct.get_jourSem()
        if jf.isjourferie(date.today()):
            return False
        else:
            if d == 5 or d == 6:
                return False
            else:
                return True

    def _isTimeOpen(self):
        ''' est-ce que L'Euronext est ouvert à cette heure ci '''
#        tm = fct.now_().time()
        tm = dt.datetime.now().time()
        self.__str__
        # print('Heure d\'ouverture:', tmOuv, 'et heure de fermeture', tmFerm)
        if self._tmOpen < tm and tm < self._tmClos:
            return True
        else:
            return False

    def _nextOpeningHour(self, dtime=None):
        '''
        Return the next opening hour of Euronext

        Parameters
        ----------
        dtime: datetime or None

        Returns
        -------
        result: datetime
                opening hour of Euronext

        '''
#        dtime = dtime.replace(hour=self._tmOpen.hour)
#        dtime = dtime.replace(minute=self._tmOpen.minute)
        dtime = dtime.replace(hour=self._tmOpen.hour,
                              minute=self._tmOpen.minute, second=0)

        return dtime

    def _nextOpeningDay(self):
        '''
        Retourne le jour suivant d'ouverture au format *datetime*
        '''
        today = dt.datetime.now()
        td = today.date()
        tm = today.time()
        # print(timedelta(days=2, hours=1))
        # print('today is ', str(now_))
        # print('dans 2 jours', str(now_ + timedelta(days=2)))
        # print(jf.listjourferie())
        if jf.isjourferie(td):
            dd = today + timedelta(days=1)
            dd = self._nextOpeningHour(dd)
            print('jour férié méthode class Euronext')
            return dd
        if fct.get_jourSem() == 4:  # 4 --> vendredi
            print('== Vendredi, prochaine ouverture ==')
            if tm < self._tmOpen:
                self._nextOpeningHour(today)
            elif tm > self._tmClos:
                dd = today + timedelta(days=3)
                dd = self._nextOpeningHour(dd)
            else:  # le marché est ouvert
                print('le marché est ouvert')
        elif fct.get_jourSem() == 5:  # 5 --> samedi
            dd = today + timedelta(days=2)
            print('== Samedi, prochaine ouverture ==')
            dd = self._nextOpeningHour(dd)
        elif fct.get_jourSem() == 6:  # 6 --> dimanche
            dd = today + timedelta(days=1)
            print('== Dimanche, prochaine ouverture ==')
            dd = self._nextOpeningHour(dd)
        else:  # autre jour de la semaine
            print('== Autre jour, prochaine ouverture ==')
            if tm < self._tmOpen:
                dd = self._nextOpeningHour(today)
            elif tm > self._tmClos:
                dd = today + timedelta(days=1)
                dd = self._nextOpeningHour(dd)
            else:  # le marché est ouvert
                print('le marché est ouvert')
        return dd

    def _setOpeningTime(self, openingTime):
        '''
        Set the opening time format type *datetime.time*

        Example
        -------
        euroN._setOpeningTime(dt.time(9, 15, 0))  # ouverture 9h15

        '''
        self._tmOpen = openingTime

    def _setClosureTime(self, closureTime):
        '''
        Définit l\'heure de fermeture format type *datetime.time*

        Example
        -------
        euroN._setOpeningTime(dt.time(17, 45, 0)))  # fermeture 17h45

        '''
        self._tmClos = closureTime

    def _getOpeningTime(self):
        '''
        Return type *Time*
        '''
        return self._tmOpen

    def _getClosureTime(self):
        '''
        Return type *Time*
        '''
        return self._tmClos

    openingTime = property(_getOpeningTime, _setOpeningTime)

    closingTime = property(_getClosureTime, _setClosureTime)

    def _display(self, dtime):
        '''
        Affiche date type *datetime*
        '''
        print('date prochaine:', dtime)
