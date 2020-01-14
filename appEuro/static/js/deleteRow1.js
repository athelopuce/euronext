//deleteRow.js
$("#delete_student").click(function(){
    $.ajax({
		url: '/_delete_student',
        data: {
            id: $(elm).attr('data-id')
        },
        type: 'POST',
		data: {id:localStorage.getItem('deleteId')},
		dataType: "text",
		success: function(data){
				 alert("Deleted Student ID "+ student_id.toString());
			   }
    });
});