//deleteRow.js
// https://datatables.net/examples/ajax/objects.html
/*
$('#owned_stock_table').on('click', '.trash', function(events){
	var col1 = $(this).closest('tr').find('td').eq(0).html(); // or you could loop through the cells
	var txt = "Voulez vous effacer l'action " + col1 + '?'
	if (confirm(txt)) {
		// Save it!
		
		var col2 = $(this).closest('tr').find('td').eq(1).html();
		$(this).closest('tr').remove();
		$.ajax({
			type: "DELETE",
			data: {column1 : col1, column2 : col2}, // post values
			success:function(result){
				//window.location.href = $SCRIPT_ROOT + '/main';
			}
		});
	}
 });
 $(document).ready(function() {
    $('.table tr').on("dblclick",  function(e){
        var case_id = $(this).find("td:first").text();
        $.ajax({
            url: "{{ url_for('current_case') }}",
            data: {'case_id' : case_id},
            type: 'POST',
            success: function(response) {
                $("#result").html(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});