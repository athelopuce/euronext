# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:31:52 2019

@author: Utilisateur

Fichier d'installation avec setuputils

dans les fichiers python:
from euronext import euronext
>>> euronext()
"""
from setuptools import setup, find_packages

# cd "Documents\Python Scripts\Euronext"
# python setup.py sdist
# ​​ls​​ ​​dist
# installation
# mkdir ~/packages
# cp dist/euronext.tar.gz ~/packages
# pip install --no-index --find-links=~packages euronext

# uninstall
# pip uninntall euronext

setup(
    name='euronext',
    version='0.1.0',
    license='proprietary',
    description='Euronext application web',

    author='DL',
    author_email='dhazel@free.fr',
    url='https://localhost:5000',

#    packages=find_packages(where='euronext'),
#    package_dir={'': 'src'},
    packages=find_packages(),
    install_requires=['flask', 'flask-bootstrap', 'flask-login', 'Flask-Mail',
                      'Flask-Migrate', 'Flask-SQLAlchemy', 'Flask-WTF',
                      'flask-pagedown', 'flask-moment'],
#    install_requires=['click', 'tinydb', 'six'],
#    extras_require={'mongo': 'pymongo'},

#    entry_points={
#        'console_scripts': [
#            'tasks = tasks.cli:tasks_cli',
#        ]
#    },
)