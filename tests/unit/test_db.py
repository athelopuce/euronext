# -*- coding: utf-8 -*-
'''
Created on Thu Dec 12 20:14:10 2019

@author: Utilisateur
'''

import sqlite3

import pytest
from appEuro import create_app, db
from flaskr.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
