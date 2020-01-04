# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:25:46 2019

@author: Utilisateur

"""
# cd "Documents\Python Scripts\Euronext"
# python run.py"

import sys
import os
#print(os.path.join(os.path.dirname(__file__), '..'))
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# visu path ajout
#print(os.path.abspath('..'))
#print(os.path.abspath('../..'))

sys.path.insert(0, os.path.abspath('../..'))  # 2 repertoires parents
#sys.path.insert(0, os.path.abspath('..'))
# path du dossier
#print(sys.path)

import lib
