## Sommaire<a id="jquery-Sommaire"></a>
[TUTO](#jquery-TUTO) \



## Recherche

- flask route delete row
- 

### Avec JQuery

- Deleting rows from database with python flask?

https://stackoverflow.com/questions/25947251/deleting-rows-from-database-with-python-flask

```html
$(document).ready(function() {
    $("a.delete").click(function() {
        var form = $('<form action="/delete/' + this.dataset.id + '" method="post"></form>');
        form.submit();
    });
});
```

- Python Flask Sqlite3 Web App Delete from database table row
https://stackoverflow.com/questions/40998026/python-flask-sqlite3-web-app-delete-from-database-table-row
```html
<form action="/foo?id={{ row["pin"] }}" method="GET">
    <button id="w3-btn">delete</button>
</form>
```

## JQuery
https://pythonprogramming.net/jquery-flask-tutorial/
```python
@app.route('/interactive/')
def interactive():
	return render_template('interactive.html')
```


---
*[Retour sommaire](#jquery-Sommaire)
# TUTO <a id="jquery-TUTO"></a>
[Adding jQuery to Your Web Pages](https://www.w3schools.com/jquery/jquery_get_started.asp)
**Google CDN:**
```html
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
</head>
```