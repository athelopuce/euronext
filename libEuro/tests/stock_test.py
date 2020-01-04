# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:24:16 2019

@author: Utilisateur
"""
# cd "Documents\Python Scripts\Euronext"
# tous les tests
# python -m pytest -v
# python -m pytest lib/tests/stock_test.py

import config  # pour inclure lib
import pytest
from libEuro.stock import Stock, Portefeuille
from datetime import datetime, timedelta

import logging
# DEBUG INFO WARNING ERROR CRITICAL
logging.basicConfig(level=logging.DEBUG)
logging = logging.getLogger(__name__)

testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected


class TestStock():
    @classmethod
    def setup_class(cls):
        cls.ml = Stock('ML.PA', 'Michelin', 90, 100)
#        print(cls.ml)  # affiche methode __str__
#        s = str(cls.ml)
#        print(s)
#        print(cls.ml.__repr__())
        print(repr(cls.ml))  # affiche MLPA

    def test_setFlagAV(self):
        self.ml.flgAV = 5.1
        assert self.ml.flgAV == 5.1

    def test_getFlagAV(self):
        x = self.ml.flgAV
        assert x == 5.1

    def test_str_(self):
        txt = 'Les données de l\'action Michelin sont:' \
                + '\nsymbol:ML.PA' \
                + '\nseuil bas:90' \
                + '\nseuil haut:100' \
                + '\nFlagAV :5.1'
        assert str(self.ml) == txt


class TestPortefeuille():
    @classmethod
    def setup_class(cls):
        cls.pf = Portefeuille('ordinaire')
        cls.act1 = Stock('ML.PA', 'Michelin', 90, 100)
        cls.act2 = Stock('FP.PA', 'Total', 10, 10)
        cls.act3 = Stock('SGO.PA', 'Saint_Gobain', 10, 10)

    def test_Portefeuille(self):
        assert str(self.pf) == 'ordinaire'

    def test_Pf_add(self):
        self.pf._add(self.act1)
        assert str(self.pf._act) == '[MLPA]'

    def test_Pf_delete(self):
        self.pf._add(self.act2)
        assert str(self.pf._act) == '[MLPA, FPPA]'
        self.pf._delete(self.act2)
        assert str(self.pf._act) == '[MLPA]'

    def test_Pf_getList(self):
        self.pf._add(self.act2)
        self.pf._add(self.act3)
        assert str(self.pf._getList()) == '[MLPA, FPPA, SGOPA]'



if __name__ == '__main__':
    # -s pour voir les print, -v verbose, -vv verbose détaillé
#    pytest.main(['-sv', __file__])
    pytest.main(['-sv', __file__ + '::TestStock'])
#    pytest.main(['-sv', __file__ + '::TestPortefeuille'])
#    pytest.main(['--collect-only', __file__])