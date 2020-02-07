# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:14:28 2020

@author: Utilisateur

https://xvrdm.github.io/2017/07/03/testing-flask-sqlalchemy-database-with-pytest/
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


def test_development_config(appDev):
    assert appDev.config['DEBUG']
    assert not appDev.config['TESTING']
    assert appDev.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
            'DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(
                    basedir, 'data-dev.sqlite')


def test_testing_config(app):
    assert app.config['DEBUG']
    assert app.config['TESTING']
    assert not app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
            'TEST_DATABASE_URL') or 'sqlite://'
    assert not app.config['BCRYPT_LOG_ROUNDS'] > 7


def test_production_config(appProd):
    assert appProd.config['DEBUG']
    assert not appProd.config['TESTING']
    assert appProd.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get(
            'DATABASE_URL') or 'sqlite:///' + os.path.join(
                    basedir, 'data.sqlite')
    assert appProd.config['BCRYPT_LOG_ROUNDS'] > 10
