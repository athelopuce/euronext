## Recherche

- flask route delete row
- 

### Avec JQuery

- Deleting rows from database with python flask?+
https://stackoverflow.com/questions/25947251/deleting-rows-from-database-with-python-flask

$(document).ready(function() {
    $("a.delete").click(function() {
        var form = $('<form action="/delete/' + this.dataset.id + '" method="post"></form>');
        form.submit();
    });
});

- Python Flask Sqlite3 Web App Delete from database table row

https://stackoverflow.com/questions/40998026/python-flask-sqlite3-web-app-delete-from-database-table-row
<form action="/foo?id={{ row["pin"] }}" method="GET">
    <button id="w3-btn">delete</button>
</form>


## JQuery
https://pythonprogramming.net/jquery-flask-tutorial/

@app.route('/interactive/')
def interactive():
	return render_template('interactive.html')