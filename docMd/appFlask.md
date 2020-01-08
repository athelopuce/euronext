# Application FLASK
---

## Sommaire<a id="appFlask-Sommaire"></a>
[INIT](#appFlask-INIT)\
[INSTALL](#appFlask-INSTALL)\
[SETUP.PY](#appFlask-SETUP_PY)\
[TESTS](#appFlask-TESTS)

# INIT<a name="appFlask-INIT"></a>
## Utilisation
pip install ? \
p199-217 Flask Web Development -  p203 \
Console:

    cd "Documents\Python Scripts"
    var.bat (double clic sur exploirateur de fichiers)
    cd Euronext_dev
    
ou

    flask db upgrade
    flask run
    flask test
    
ou init

    set FLASK_APP=run.py
    set FLASK_DEBUG=1
    flask db init

## Web
http://localhost:5000  --> windows \
http://192.168.10.15:5000/  --> raspberry

## db
voir doc [migrate](migrate.md)

    flask db init


---
*[Retour sommaire](#appFlask-Sommaire)
# INSTALL<a name="appFlask-INSTALL"></a>
## Sur Windows conda
installation sur env py4fi (obsolete).\
!!!! recréer un environnement propre
 flask et flask-login.
 
## Packages flask requis*

*voir [Requirements.txt](Requirements.md)

---
*[Retour sommaire](#appFlask-Sommaire)
# SETUP.PY<a name="appFlask-SETUP_PY"></a>
* Fichier d'installation avec setuputils*

*voir [setuputils](setuputils.md)

---
*[Retour sommaire](#appFlask-Sommaire)
# TESTS<a name="appFlask-TESTS"></a>
voir [Pytest](pytest_Tuto.md)
