
"""
This file (test_models.py) contains the unit tests for the models.py file.
"""


##########
# Action #
##########


def test_new_action(new_action):
    """
    GIVEN a Action model
    WHEN a new Action is created
    THEN check the name, symbol
    are defined correctly
    """
    assert new_action.name == 'Michelin'
    assert new_action.symbol == 'ML.PA'
    assert new_action.unitaryPrice == 0


#########
# Ordre #
#########

def test_new_ordre(new_ordre):
    """
    GIVEN a Ordre model
    WHEN a new Ordre is created
    THEN check the name, symbol
    are defined correctly
    """
    assert new_ordre.name == 'Michelin'
    assert new_ordre.symbol == 'ML.PA'


########
# User #
########

# version d'essai. Plutot Utiliser le test test_new_user(new_user)
def test_new_userV0(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the login, password ...
    are defined correctly
    """
    assert new_user.login == 'John'
    assert new_user.password == 'Doe'
    from appEuro.models import User
    u = User(idUser=2, login='Susan', password='Dir', connectionNumber=3)
    assert u.idUser == 2
    assert u.login == 'Susan'
    assert u.password == 'Dir'
    assert u.connectionNumber == 3


# doublon du fichier test-users.py pour essai
def test_bienvenue2(test_client):
    # bienvenue
    response = test_client.get('/bienvenue')
    assert response.status_code == 200  # mettre 200 (ou 300 pour erreur)


# test table User
def test_user_query_all(test_client, init2_database):
    from appEuro.models import User
    users = User.query.all()
    print(users)  # use pytest -s
    assert str(users) == "[<User 'John'>, <User 'Susan'>]"
    listdata = [(0, 'John', 'Doe'), (2, 'Susan', 'Dir')]
    x = 0
    for u in users:
        print(u.login, u.password)
        assert u.login == listdata[x][1]
        assert u.password == listdata[x][2]
        x += 1


# A revoir table originnale User et mot de passe
def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, and role fields
    are defined correctly
    """
    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.hashed_password != 'FlaskIsAwesome'
    assert not new_user.authenticated
    assert new_user.role == 'user'


def test_setting_password(new_user):
    """
    GIVEN an existing User
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """
    new_user.set_password('MyNewPassword')
    assert new_user.hashed_password != 'MyNewPassword'
    assert new_user.is_correct_password('MyNewPassword')
    assert not new_user.is_correct_password('MyNewPassword2')
    assert not new_user.is_correct_password('FlaskIsAwesome')


def test_user_id(new_user):
    """
    GIVEN an existing User
    WHEN the ID of the user is defined to a value
    THEN check the user ID returns a string (and not an integer)
    as needed by Flask-WTF
    """
    new_user.id = 17
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == "17"
