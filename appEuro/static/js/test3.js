/* Test fonction a+ b*/
// https://code-maven.com/slides/python-programming/flask-and-ajax-plain-javascript
/*
sdg.html --> addnumber
*/
(function() {
	var ajax_get = function(url, callback) {
        xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log('responseText:' + xhr.responseText);
                try {
                    var data = JSON.parse(xhr.responseText);
                } catch(err) {
                    console.log(err.message + " in " + xhr.responseText);
                    return;
                }
                callback(data);
            }
        };
 
        xhr.open("GET", url, true);
        xhr.send();
	};
	
    var calc = document.getElementById('calc');
    calc.addEventListener('click', function() {
        var url = '/api/add?a=' + document.getElementById('a').value + '&b=' + document.getElementById('b').value;
        //console.log(url);
        ajax_get(url, function(data) {
            document.getElementById('add').innerHTML = data['a'] + ' + ' + data['b'] + ' = ' + data['add'];
        });
	});
  })()