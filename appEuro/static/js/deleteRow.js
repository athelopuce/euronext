//deleteRow.js
(function() {
	var ajax_get = function(url, callback) {
        xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                console.log('responseText:' + xhr.responseText);
                try {
					// reponse du serveur
                    //var data = JSON.parse(xhr.responseText);
					//document.getElementById("myTable").deleteRow(id);
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
	
	var id = document.getElementById(id).value;
	var delete = document.getElementById('#delete');
    delete.addEventListener('click', function() {
        var url = '/foo?id=' + id;
        //console.log(url);
        ajax_get(url, function(data) {
            //document.getElementById('add').innerHTML = data['a'] + ' + ' + data['b'] + ' = ' + data['add'];
        });
	});
	
})()