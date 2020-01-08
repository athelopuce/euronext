import pytest
from appEuro import create_app, db
from appEuro.models import User, Action, Ordre


@pytest.fixture(scope='module')
def new_action():
    action = Action('Michelin', 'ML.PA')
    return action


@pytest.fixture(scope='module')
def new_ordre():
    ordre = Ordre('Michelin', 'ML.PA')
    return ordre


@pytest.fixture(scope='module')
def new_user():
    user = User()
    return user


# pour class User avec Act
@pytest.fixture(scope='module')
def init2_database():
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User()
    user2 = User(idUser=2, login='Susan', password='Dir', connectionNumber=3)
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('testing')

    # Flask provides a way to test your application by exposing the Werkzeug
    # test Client and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User(email='patkennedy79@gmail.com',
                 plaintext_password='FlaskIsAwesome')
    user2 = User(email='kennedyfamilyrecipes@gmail.com',
                 plaintext_password='PaSsWoRd')
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
