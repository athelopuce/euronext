## Tester Flask db
## Tester db en ligne de commande
``` Python
flask shell
>>>
from appEuro import db
from appEuro.models import User, Act, Ord, OrdLine, Cpt
u = User()
print(u)
db.session.add(u)
db.session.commit()

u = User(idUser=2, login='Susan', password='Dir', connectionNumber=3)
print(u)
db.session.add(u)
db.session.commit()

users = User.query.all()
>>> users
[<User john>, <User susan>]
for u in users:
...     print(u.login, u.password)
...
John Doe
Susan Dir

```