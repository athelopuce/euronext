/* autocomplete */
// https://www.bogotobogo.com/python/Flask/Python_Flask_with_AJAX_JQuery.php

$(document).ready(function() {
	var listactions=[];

	function loadActions(){
		$.getJSON('/listAction', function(data, status, xhr){
			for (var i = 0; i < data.length; i++ ) {
				listactions.push(data[i].name);
			}
		});
	};

	loadActions();

	$('#action').autocomplete({
		source: listactions
	});
	
});
