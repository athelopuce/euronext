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
User.query.all()
User.query.filter_by(login='admin').first()

jo = User()  # login = 'John'
Cpt(name='PEA', user=jo)
asv = Cpt(name='assur-vie')
jo.comptes.append(asv)  # backref
db.session.add(jo)
db.session.commit()
jo.comptes
... [<Cpt 'PEA'>, <Cpt 'assur-vie'>]
```
```Python
from sqlalchemy.orm import joinedload
query = User.query.options(joinedload('comptes'))
for user in query:
    print(user, user.comptes)
...
1: admin passadmin - 0 []
2: John Doe - 0 [<Cpt 'PEA'>, <Cpt 'assur-vie'>]

Cpt.query.with_parent(jo).filter(Cpt.name != 'PEA').all()
... [<Cpt 'assur-vie'>]
```
