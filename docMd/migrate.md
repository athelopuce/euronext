# RESUME
```Python
flask db --help
flask db history -v
flask db migrate -m "message"
flask db upgrade
```    

# INIT<a id="migrate.md"></a>
```Python
(venv) set FLASK_APP=run.py
(venv) flask db init
...
Creating directory C:\Users\Utilisateur\Documents\Python Scripts\EuronextClone\m
igrations ...  done
Creating directory C:\Users\Utilisateur\Documents\Python Scripts\EuronextClone\m
igrations\versions ...  done
Generating C:\Users\Utilisateur\Documents\Python Scripts\EuronextClone\migration
s\alembic.ini ...  done
Generating C:\Users\Utilisateur\Documents\Python Scripts\EuronextClone\migration
s\env.py ...  done
Generating C:\Users\Utilisateur\Documents\Python Scripts\EuronextClone\migration
s\README ...  done
Generating C:\Users\Utilisateur\Documents\Python Scripts\EuronextClone\migration
s\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'C:\\Users\\Utilisateur
\\Documents\\Python Scripts\\EuronextClone\\migrations\\alembic.ini' before proc
eeding.
```

---
## The First Database Migration
### Migrate
with txt users table explicit what you do :
```Python
(venv) flask db migrate -m "users table"
...
C:\Users\Utilisateur\Documents\Python Scripts\EuronextDev\run.py:47: Warning: Si
lently ignoring app.run() because the application is run from the flask command
line executable.  Consider putting app.run() behind an if __name__ == "__main__"
 guard to silence this warning.
  app.run(debug=True)
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'action'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_action_name' on '[
'name']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_action_symbole' on
 '['symbole']'
INFO  [alembic.autogenerate.compare] Detected added table 'ordre'
INFO  [alembic.autogenerate.compare] Detected added table 'seuil'
Generating C:\Users\Utilisateur\Documents\Python Scripts\EuronextDev\migrations\
versions\6ff953942fcd_users_table.py ...  done
```

---
### Upgrade
To apply the changes to the database, the flask db upgrade command must be used.
```Python
(venv) flask db upgrade
...
C:\Users\Utilisateur\Documents\Python Scripts\EuronextDev\run.py:47: Warning: Si
lently ignoring app.run() because the application is run from the flask command
line executable.  Consider putting app.run() behind an if __name__ == "__main__"
 guard to silence this warning.
  app.run(debug=True)
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 6ff953942fcd, users table
```

---
### Downgrade
```Python
(venv) flask db downgrade
...
C:\Users\Utilisateur\Documents\Python Scripts\EuronextDev\run.py:47: Warning: Si
lently ignoring app.run() because the application is run from the flask command
line executable.  Consider putting app.run() behind an if __name__ == "__main__"
 guard to silence this warning.
  app.run(debug=True)
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running downgrade 6ff953942fcd -> , users tabl
e
```