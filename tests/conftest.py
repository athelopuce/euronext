'''
https://xvrdm.github.io/2017/07/03/testing-flask-sqlalchemy-database-with-pytest/
'''


import pytest
from appEuro import create_app
from appEuro import db as _db
from appEuro import db as db2
from sqlalchemy import event
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


#@pytest.fixture
#def client(app):
#    """A test client for the app."""
#    return app.test_client()


@pytest.fixture(scope='session')
def test_client(app):
#    app = create_app('testing')

    # Flask provides a way to test your application by exposing the Werkzeug
    # test Client and handling the context locals for you.
    testing_client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope="session")
def app(request):
    """
    Returns session-wide application.
    """
    return create_app("testing")


@pytest.fixture
def appProd():
    """
    Returns session-wide application.
    """
    return create_app("production")


# fixture scope="formule"
@pytest.fixture
def appDev():
    """
    Returns session-wide application.
    """
    return create_app("development")


def add_data(db):
    # Insert user data
    user1 = User()
    user2 = User(idUser=2, login='Susan', password='Dir', connectionNumber=3)
    db.session.add(user1)
    db.session.add(user2)
    act1 = Act(name='Michelin', symbol='ML.PA', unitaryPrice=10.56)
    act2 = Act(name='Total', symbol='FP.PA')
    db.session.add(act1)
    db.session.add(act2)
    ord1 = Ord(sens='a', ordDate=date(2019, 1, 20), PriceAchat=10.56,
               quantity=3,
               idAct=2)
    ord2 = Ord(sens='a', ordDate=date(2019, 1, 21), PriceAchat=12.56,
               quantity=2, idAct=2)
    db.session.add(ord1)
    db.session.add(ord2)
    # Commit the changes for the users
    db.session.commit()


#@pytest.fixture(scope="session")
#def db(app, request):
#    """
#    Returns session-wide initialised database.
#    """
#    with app.app_context():
#        _db.drop_all()
#        _db.create_all()
#        add_data(_db)


#@pytest.fixture(scope="function", autouse=True)
#def session(app, db, request):
#    """
#    Returns function-scoped session.
#    """
#    with app.app_context():
#        conn = _db.engine.connect()
#        txn = conn.begin()
#
#        options = dict(bind=conn, binds={})
#        sess = _db.create_scoped_session(options=options)
#
#        # establish  a SAVEPOINT just before beginning the test
#        # (http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#using-savepoint)
#        sess.begin_nested()
#
#        @event.listens_for(sess(), 'after_transaction_end')
#        def restart_savepoint(sess2, trans):
#            # Detecting whether this is indeed the nested
#            # transaction of the test
#            if trans.nested and not trans._parent.nested:
#                # The test should have normally called session.commit(),
#                # but to be safe we explicitly expire the session
#                sess2.expire_all()
#                sess.begin_nested()
#
#        _db.session = sess
#        yield sess
#
#        # Cleanup
#        sess.remove()
#        # This instruction rollsback any commit that were executed
#        # in the tests.
#        txn.rollback()
#        conn.close()


# pour class User avec Act
#        @pytest.fixture
@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db2.create_all()

    # Insert user data
    add_data(db2)
#    user1 = User()
#    user2 = User(idUser=2, login='Susan', password='Dir', connectionNumber=3)
#    db2.session.add(user1)
#    db2.session.add(user2)
#    act1 = Act(name='Michelin', symbol='ML.PA', unitaryPrice=10.56)
#    act2 = Act(name='Total', symbol='FP.PA')
#    db2.session.add(act1)
#    db2.session.add(act2)
#    ord1 = Ord(sens='a', ordDate=date(2019, 1, 20), PriceAchat=10.56,
#               quantity=3,
#               idAct=2)
#    ord2 = Ord(sens='a', ordDate=date(2019, 1, 21), PriceAchat=12.56,
#               quantity=2, idAct=2)
#    db2.session.add(ord1)
#    db2.session.add(ord2)
#    # Commit the changes for the users
#    db2.session.commit()

    yield db2  # this is where the testing happens!

    # looks like db.session.close() would work
    db2.session.remove()  # mon rajout pour clean
    db2.drop_all()
