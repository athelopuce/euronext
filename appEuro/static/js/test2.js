/* Test fonction a+ b*/
// https://code-maven.com/slides/python-programming/flask-and-ajax-plain-javascript
/*
sdg.html --> addnumber
*/
$(function() {
	var ajax_get = function(url, callback) {
        xmlhttp = new XMLHttpRequest();
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                console.log('responseText:' + xmlhttp.responseText);
                try {
                    var data = JSON.parse(xmlhttp.responseText);
                } catch(err) {
                    console.log(err.message + " in " + xmlhttp.responseText);
                    return;
                }
                callback(data);
            }
        };
 
        xmlhttp.open("GET", url, true);
        xmlhttp.send();
	
	
    var calc = document.getElementById('calc');
    calc.addEventListener('click', function() {
        var url = '/addition/add?a=' + document.getElementById('a').value + '&b=' + document.getElementById('b').value;
        //console.log(url);
        ajax_get(url, function(data) {
            document.getElementById('add').innerHTML = data['a'] + ' + ' + data['b'] + ' = ' + data['add'];
        });
  });