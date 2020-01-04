# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:35:31 2019

@author: trading

TEST Envoi message SMS
"""
# cd "Documents\Python Scripts\Euronext"
# python -m pytest -v  # tous les tests
# python -m pytest lib/tests/sms_test.py

#import config  # pour inclure lib
import pytest

from libEuro.sms import SMS, SMSfictif
import datetime as dt


class TestSMSfictif():
    def test_envoiTest1(self):
        smsLau = SMSfictif()
        msg = 'Hello TestSMSfictif'
        assert smsLau.envoiTest(msg) == msg


class TestSMS():
    @classmethod
    def setup_class(cls):
        cl = 25.25678
        now = dt.datetime.now()  # current date and time
        cls.message = 'Vendre Michelin \nle cours est ' \
            + str(round(cl, 2)) \
            + now.strftime('.\n   Message du : %d/%m/%Y à %H:%M.')
        cls.sms = SMS()
        print(cls.sms)

    def test_envoiTest1(self):
        assert self.sms.envoiTest(self.message) == self.message


if __name__ == '__main__':
#    pytest.main([__file__])
    # -s pour voir les print, -v verbose
#    pytest.main(['-vv', 'sms_test.py::TestSMS'])
    pytest.main(['-sv', 'sms_test.py::TestSMSfictif'])

