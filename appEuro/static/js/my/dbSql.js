//dbSql.js
// https://code-maven.com/slides/python-programming/flask-and-ajax-plain-javascript


// add-new -> .btn-info.add-new
// add -> .btn-primary
// edit -> .btn-success
// delete -> .btn-function loadDoc() {
	
// Version complete	
/* $(document).ready(function(){
$('#demo, h1').html('Hello world. Ce texte est affiché parjQuery.');
}); */

// Version simplifiée	
/* $(function(){
	$('#demo, h1').html('Hello world. Ce texte est affiché parjQuery.');
}); */

/* function addSubmit(ev) {
	ev.preventDefault();
	$.ajax({
		method: 'POST',
		url: {{ url_for('add')|tojson }},
		data: $(this).serialize()
	}).done(addShow);
}

function addShow(data) {
	$('#premier').text(data.result);
}

$('#majPremier').on('click', addSubmit); */


$(function(){
	$('#majPremier').click(function(){
		$.ajax({
			type:'GET',
			url:'maj1.html?l=7',
			timeout:3000,
			success:function(data){
				alert(data);
			},
			error:function(){
				alert('La requête n\'a pas abouti');
			}
		});
	});
});
