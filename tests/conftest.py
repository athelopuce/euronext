import pytest
from appEuro import create_app, db
from appEuro.models import User, Act, Ord
from datetime import date


###################
# Tests unitaires #
###################
# pour tester la class seule sans db.session.add()
@pytest.fixture(scope='module')
def new_action():
    act = Act(idAct=1, name='Michelin', symbol='ML.PA', unitaryPrice=10.56)
    return act


# pour tester la class seule sans db.session.add()
@pytest.fixture(scope='module')
def new_ord():
    order = Ord(idOrd=1, sens='a', ordDate='2019-01-20', PriceAchat=10.56,
                quantity=3, idAct=2)
    return order


@pytest.fixture(scope='module')
def new_user():
    user = User()
    return user


# pour class User avec Act
@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User()
    user2 = User(idUser=2, login='Susan', password='Dir', connectionNumber=3)
    db.session.add(user1)
    db.session.add(user2)
    act1 = Act(name='Michelin', symbol='ML.PA', unitaryPrice=10.56)
    act2 = Act(name='Total', symbol='FP.PA')
    db.session.add(act1)
    db.session.add(act2)
    ord1 = Ord(sens='a', ordDate=date(2019, 1, 20), PriceAchat=10.56, quantity=3,
               idAct=2)
    ord2 = Ord(sens='a', ordDate=date(2019, 1, 21), PriceAchat=12.56,
               quantity=2, idAct=2)
    db.session.add(ord1)
    db.session.add(ord2)
    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='module')
def test_client():
    app = create_app('testing')

    # Flask provides a way to test your application by exposing the Werkzeug
    # test Client and handling the context locals for you.
    testing_client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

