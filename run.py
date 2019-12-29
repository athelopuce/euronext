# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:31:52 2019

@author: Utilisateur

Window:
-------
set FLASK_APP=run.py
flask run


Rasp:
------
/home/pi/berryconda3/envs/Trading/bin/python /home/pi/Trad/webAppV2.py

Autre solution:
source activate Trading
cd Trad
export FLASK_APP=run.py
flask run

Web
----
http://localhost:5000  # windows
http://192.168.10.15:5010/  # raspberry

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xx-some-javascript-magic
"""

from euronext import app, db

# cd "Documents\Python Scripts\Euronext"
# python run.py

# .flaskenv --> set FLASK_APP=run.py

# creates a shell context that adds the database instance and
# models to the shell session:
#from euronext.models import User, Post


#@app.shell_context_processor
#def make_shell_context():
#    return {'db': db, 'User': User, 'Post': Post}


#app.run(host='0.0.0.0', port=5010, debug=True)
if __name__ == '__main__':
    app.run()

