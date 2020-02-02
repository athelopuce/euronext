from datetime import date, timedelta

"""
This file (test_models.py) contains the unit tests for the models.py file.
"""


##########
# Action #
##########


def test_new_action(new_action):
    """
    GIVEN a Act model
    WHEN a new act is created
    THEN check the idAct, name, symbol, unitaryPrice
    __str__, __repr__, __init__
    are defined correctly
    """
    assert new_action.name == 'Michelin'
    assert new_action.symbol == 'ML.PA'
    assert new_action.unitaryPrice == 10.56
    assert str(new_action) == 'idAct 1: Michelin symbol ML.PA = 10.56 euros'
    assert repr(new_action) == '<Act \'Michelin\'>'
    # test __init__
    from appEuro.models import Act
    act = Act(idAct=1, name='Michelin', symbol='ML.PA')
    assert str(act) == 'idAct 1: Michelin symbol ML.PA = 0.00 euros'


def test_act_query_all(test_client, init2_database):
    '''
    Check insert data act, doublon?
    '''
    from appEuro.models import Act
    acts = Act.query.all()
    print(acts)  # use pytest -s
    assert str(acts) == "[<Act 'Michelin'>, <Act 'Total'>]"
    listdata = [(1, 'Michelin', 'ML.PA', 10.56), (2, 'Total', 'FP.PA', 0.00)]
    x = 0
    for elt in acts:
        print(elt.idAct, elt.name, elt.symbol, elt.unitaryPrice)
        assert elt.idAct == listdata[x][0]
        assert elt.name == listdata[x][1]
        assert elt.symbol == listdata[x][2]
        assert elt.unitaryPrice == listdata[x][3]
        x += 1


#########
# Ordre #
#########

def test_new_ord(new_ord):
    """
    GIVEN a Ord model
    WHEN a new Ord is created
    THEN check the sens, date, ...
    are defined correctly

    Nota: The way to store dates in SQLite is:
    yyyy-mm-dd hh:mm:ss.xxxxxx
    """
    assert new_ord.idOrd == 1
    assert new_ord.sens == 'a'
    assert new_ord.ordDate == '2019-01-20'
    assert new_ord.PriceAchat == 10.56
    assert new_ord.quantity == 3
    assert new_ord.idAct == 2


def test_ord_query_all(test_client, init2_database):
    '''
    Check insert data ord, doublon?
    '''
    from appEuro.models import Ord
    ords = Ord.query.all()
    print(ords)  # use pytest -s
    assert str(ords) == "[<Ord 1>, <Ord 2>]"
    listdata = [
            (1, 'a', date(2019, 1, 20), 10.56, 3, 2, '20/01/2019'),
            (2, 'a', date(2019, 1, 21), 12.56, 2, 2, '21/01/2019')
            ]
    x = 0
    for elt in ords:
        print(elt.idOrd, elt.sens, elt.ordDate, elt.PriceAchat, elt.quantity,
              elt.idAct)
        assert elt.idOrd == listdata[x][0]
        assert elt.sens == listdata[x][1]
        print(elt.ordDate.strftime('%d/%m/%Y'))
        assert elt.ordDate.date() - listdata[x][2] < timedelta(minutes=1)
        assert elt.ordDate.strftime('%d/%m/%Y') == listdata[x][6]
        assert elt.PriceAchat == listdata[x][3]
        assert elt.quantity == listdata[x][4]
        assert elt.idAct == listdata[x][5]
        x += 1


########
# User A garder pour essai avec pytest #
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
