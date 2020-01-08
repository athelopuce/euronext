# PYTEST
---
## Commandes courantes
```Python
pytest --version
python -m pytest
python -m pytest lib/tests/trading_test.py
python -m pytest lib/tests/
# ou
pytest
pytest lib/tests/trading_test.py
pytest lib/tests/
pytest lib
```
## Help
reporting:
```Python
-v, --verbose         increase verbosity
-s : visualiser print
```
test session debugging and configuration:
```Python
--setup-show          show setup of fixtures while executing tests.
```

---
# TESTS
## Update database
```Python
flask db migrate -m "Ajout users table"
flask db upgrade
```

## Groupes
```Python
pytest --setup-show tests/unit/
```

## Tester individuellement
### database
```Python
pytest --setup-show tests/unit/test_models.py::test_bienvenue2 -v
pytest --setup-show tests/unit/test_models.py::test_new_user -v
pytest --setup-show tests/unit/test_models.py::test_new_userV0 -v
pytest --setup-show tests/unit/test_models.py::test_user_query_all -v
# ou print
pytest tests/unit/test_models.py::test_user_query_all -s 
```

### appFlask
test_home_page ('/')
```Python
pytest --setup-show tests/functional/test_users.py::test_bienvenue
pytest --setup-show tests/functional/test_users.py::test_home_page
```
test_home_page ('/newAct')
```Python
pytest tests/functional/test_users.py::test_NewAct_page --setup-show -v
pytest tests/functional/test_users.py::test_NewAct_page -s
```
