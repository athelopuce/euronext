# SHELL
## Flask shell

    (env) flask shell
    >>> db
    <SQLAlchemy engine=sqlite:///C:\Users\Utilisateur\Documents\Python Scripts\EuronextClone\data-dev.sqlite>
    >>> Action
    <class 'appEuro.models.Action'>

---
# CLIK

    (env) flask test

---
# Flask-sqlalchemy

https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/

Relation simple
exemple ajouter un compte à John
```Python
flask shell
admin = User(login='admin', password='passadmin')
db.session.add(admin)
guest = User(login='guest', password='passguest')
db.session.add(guest)
db.session.commit()

jo = User()  # login = 'John'
Cpt(name='PEA', user=jo)
asv = Cpt(name='assur-vie')
jo.comptes.append(asv)  # backref
db.session.add(jo)
db.session.commit()
```