# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:31:52 2019

@author: Utilisateur

config best pratique
https://flask.palletsprojects.com/en/1.1.x/config/
"""
import os
import click
from flask_migrate import Migrate
# from euronext import app, db
from appEuro import create_app, db
#from appEuro.models import Action, Ordre, Seuil
from appEuro.models import User, Act, Ord, OrdLine, Cpt, Action, Ordre
import pytest


#    cd Documents\Python Scripts
#    ./var.bat
#    cd EuronextClone
#    flask run
#    flask test


#    .flaskenv --> set FLASK_APP=run.py


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)


# pour les commande shell: flask shell (voir fichier shell.md)
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Act=Act, Ord=Ord, OrdLine=OrdLine, Cpt=Cpt)


# lance les tests: cmd flask test (voir fichier shell.md)
@app.cli.command()
@click.argument('test_names', nargs=-1)
def test(test_names):
    """Run the unit tests."""
    import unittest
    if test_names:
        tests = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    pytest.main(['-sv', 'tests/'])
    pytest.main(['-sv', 'libEuro/'])
