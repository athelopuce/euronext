/* autocomplete et liste des valeurs entrée */
A REVOIR
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
	
	
	$('form').on('submit', function(e){
		$.ajax({
			data: {
				action:$('#action').val()
			},
			type: 'POST',
			url : '/process'
		})
		.done(function(data1){
			if (data.error){
				$('#result').text(data.error).show();
			}
			else {
				$('#result').html(data.country).show()
			}
		})

		e.preventDefault();
	});
});
