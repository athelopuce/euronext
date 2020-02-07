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


def test_home_page_get(test_client):
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


def test_home_page_post(test_client):
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
def test_newAct_page(test_client, session):
    """
    GIVEN a Flask application
    WHEN the '/newAct' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/newAct',)
    assert response.status_code == 200
    assert b"newAct.js" in response.data
    assert b"Symbol" in response.data
    assert b"Name" in response.data
    assert b"Action" in response.data
    assert b"Michelin" in response.data
    assert b"Total" in response.data


@pytest.mark.parametrize(
    ("idt", "table", "res1"), (
            (1, 'newAct', {'ida': 1, 'name': 'Michelin'}),
            (2, 'newAct', {'ida': 2, 'name': 'Total'}),
            (1, 'newOrd', {'ido': 1, 'sens': 'a'}),
            (2, 'newOrd', {'ido': 2, 'sens': 'a'})
            ))
def test_newAct_json_editRow(test_client, session, idt, table, res1):
    response = test_client.post("/editRow", data={"id": idt, "table": table})
    json_data = response.get_json()
    print(json_data)
    assert response.status_code == 200


# test javascript
@pytest.mark.parametrize(
    ("idt", "table", "res1"), (
            (1, 'newAct', {'ida': 1, 'name': 'Michelin'}),
            (2, 'newAct', {'ida': 2, 'name': 'Total'}),
            (1, 'newOrd', {'ido': 1, 'sens': 'a'}),
            (2, 'newOrd', {'ido': 2, 'sens': 'a'})
            ))
def test_newAct_json_delRow(test_client, session, idt, table, res1):
    """
    GIVEN a Flask application
    WHEN the '/delRow' page is posted to (POST) with javascript
    THEN check the json response is valid
    """
    response = test_client.post("/delRow", data={"id": idt, "table": table})
    json_data = response.get_json()
    print(json_data)
    assert response.status_code == 200
    assert response.json == res1
#    assert json_data['ida'] == idt


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
