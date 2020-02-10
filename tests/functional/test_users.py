"""
This file (test_users.py) contains the functional tests for
the users blueprint.

These tests use GETs and POSTs to different URLs to check for the proper
behavior of the users blueprint.


https://medium.com/@aswens0276/using-pytest-to-setup-dynamic-testing-for-your-flask-apps-postgres-database-locally-and-with-39a14c3dc421
https://github.com/pallets/flask/blob/master/examples/tutorial/tests/test_auth.py
https://realpython.com/testing-in-django-part-1-best-practices-and-examples/#testing-views
"""

import pytest
from datetime import date


#####
# / #
#####
def test_homeTest(test_client):
    '''
    test acces au site page index.html sans db
    '''
    response = test_client.get('/homeTest')
    assert response.status_code == 200
    assert b"name" in response.data  # MyForm() with name
    assert b"Pleased to meet you!" in response.data
    assert b"Happy to see you again!" not in response.data


def test_home_page_get(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    # A revoir manque liste des actions qui devrait disparaitre
    response = test_client.get('/index')
    assert response.status_code == 200
#    assert b"Welcome to the Flask User Management Example!" in response.data
#    assert b"Need an account?" in response.data
#    assert b"Existing user?" in response.data


def test_home_page_post(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post('/')
    assert response.status_code == 405
    assert b"Welcome to the Flask User Management Example!" \
        not in response.data


###########
# /NewAct #
###########
def test_newAct_page(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/newAct' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/newAct',)
    assert response.status_code == 200
    # page ajax
    assert b"newAct.js" in response.data
    # Titres tableau
    assert b"Symbol" in response.data
    assert b"Name" in response.data
    assert b"Action" in response.data
    # data
    assert b"Michelin" in response.data
    assert b"Total" in response.data


#def test_newAct_json_addRow(test_client, session, idt, table, res1):


@pytest.mark.parametrize(
    ('idt', 'result'), (
            ({'id': 1, 'name': 'Michelin', 'symbol': 'ML.PA', 'table': 'newAct'},
             {'ida': 1, 'name': 'Michelin', 'symbol': 'ML.PA'}),
            ({'id': 2, 'name': 'Total', 'symbol': 'FP.PA', 'table': 'newAct'},
             {'ida': 2, 'name': 'Total', 'symbol': 'FP.PA'}),
            ({'id': 5, 'name': 'new action', 'symbol': 'nw.PA', 'table': 'newAct'},
             {'ida': 3, 'name': 'new action', 'symbol': 'nw.PA'}),
            ({'id': 1, 'sens': 'a', 'date': '2019-01-20', 'PriceAchat': 10.56,
              'quantity': 5, 'idAct': 1, 'table': 'newOrd'},
             {'ido': 1, 'sens': 'a', 'date': '2019-01-20', 'PriceAchat': 10.56,
              'quantity': 5, 'idAct': 1}),
            ({'id': 2, 'sens': 'a', 'date': '2019-01-21', 'PriceAchat': 12.56,
              'quantity': 2, 'idAct': 2, 'table': 'newOrd'},
             {'ido': 2, 'sens': 'a', 'date': '2019-01-21', 'PriceAchat': 12.56,
              'quantity': 2, 'idAct': 2}),
            ({'id': 8, 'sens': 'a', 'date': '2019-01-22',
              'PriceAchat': 14.56, 'quantity': 3, 'idAct': 1,
              'table': 'newOrd'},
             {'ido': 8, 'sens': 'a', 'date': '2019-01-22',
              'PriceAchat': 14.56, 'quantity': 3, 'idAct': 1})
            ))
def test_newAct_json_editRow(test_client, init_database, idt, result):
    '''
    Test javascript newAct.js
      - edit l'action dans la base
      - idAct inconnu --> new action
      - idOrd, sens, date, PriceAchat, quantity, idAct
    '''
    response = test_client.post("/editRow", data=idt)
    json_data = response.get_json()
    print(json_data)
    assert response.status_code == 200
    assert response.json == result


# test javascript
@pytest.mark.parametrize(
    ("idt", "table", "result"), (
            (1, 'newAct', {'ida': 1, 'name': 'Michelin'}),
            (2, 'newAct', {'ida': 2, 'name': 'Total'}),
            (8, 'newAct', {'ida': 8, 'result': 'pas de data'}),
            (1, 'newOrd', {'ido': 1, 'sens': 'a'}),
            (2, 'newOrd', {'ido': 2, 'sens': 'a'}),
            (8, 'newOrd', {'ido': 8, 'result': 'pas de data'})
            ))
def test_newAct_json_delRow(test_client, init_database, idt, table, result):
    """
    GIVEN a Flask application
    WHEN the '/delRow' page is posted to (POST) with javascript
      - delRow id dans la base
      - delRow idAct inconnu
    THEN check the json response is valid
    """
    response = test_client.post("/delRow", data={"id": idt, "table": table})
    json_data = response.get_json()
    print(json_data)
    assert response.status_code == 200
    assert response.json == result
#    assert json_data['ida'] == idt
    # voir ajouter test addRow ci dessous:


###########
# /NewOrd #
###########
def test_newOrd_page(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/newOrd' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/newOrd')
    assert response.status_code == 200
    # ajax page
    assert b"newOrd.js" in response.data
    # titres table
    assert b"Sens" in response.data
    assert b"Date" in response.data
    assert b"Prix" in response.data
    assert b"Quantite" in response.data
    assert b"Titre" in response.data
    assert b"Action" in response.data
    # data
#    assert b"Michelin" in response.data
#    assert b"Total" in response.data


def test_newOrd_form(test_client, init_database):
    resp = test_client.post("/newOrd",
                            data={'ido': 8,
                                  'sens': 'a',
                                  'date': '2019-01-22',
                                  'PriceAchat': 14.56,
                                  'quantity': 3,
                                  'idAct': 1
                                  }
                            )
    assert resp.status_code == 200
    assert b'<input id="ordDate" name="ordDate" required="" type="text" value="09/02/2020">' in resp.data
    assert b"New order, 1, added!" in resp.data
    assert b"Flask User Management" in resp.data


# A cacher
'''
##########
# /login #
##########
def test_login_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Email" in response.data
    assert b"Password" in response.data


def test_valid_login_logout(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login',
                                data=dict(email='patkennedy79@gmail.com', password='FlaskIsAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Thanks for logging in, patkennedy79@gmail.com!" in response.data
    assert b"Welcome patkennedy79@gmail.com!" in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" in response.data
    assert b"Login" not in response.data
    assert b"Register" not in response.data

    """
    GIVEN a Flask application
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Goodbye!" in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data


def test_invalid_login(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/login',
                                data=dict(email='patkennedy79@gmail.com', password='FlaskIsNotAwesome'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"ERROR! Incorrect login credentials." in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data


def test_valid_registration(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = test_client.post('/register',
                                data=dict(email='patkennedy79@yahoo.com',
                                          password='FlaskIsGreat',
                                          confirm='FlaskIsGreat'),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Thanks for registering, patkennedy79@yahoo.com!" in response.data
    assert b"Welcome patkennedy79@yahoo.com!" in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" in response.data
    assert b"Login" not in response.data
    assert b"Register" not in response.data

    """
    GIVEN a Flask application
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Goodbye!" in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data


def test_invalid_registration(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/register' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/register',
                                data=dict(email='patkennedy79@hotmail.com',
                                          password='FlaskIsGreat',
                                          confirm='FlskIsGreat'),   # Does NOT match!
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"Thanks for registering, patkennedy79@hotmail.com!" not in response.data
    assert b"Welcome patkennedy79@hotmail.com!" not in response.data
    assert b"[This field is required.]" not in response.data
    assert b"Flask User Management" in response.data
    assert b"Logout" not in response.data
    assert b"Login" in response.data
    assert b"Register" in response.data
'''
