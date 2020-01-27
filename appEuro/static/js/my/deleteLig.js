// save.js
$(function() {
    $('a#operation').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });
});


function addSubmit(ev) {
	ev.preventDefault();
	$.ajax({
		method: 'POST',
		url: $SCRIPT_ROOT + '/add',
		data: $(this).serialize()
	}).done(addShow);
}

function addShow(data) {
	$('#resultat').text(data.result);
}

$('#calc').on('submit', addSubmit);


//$( "#example tbody" ).on( "click", "tr", function(event) {
/* $( "#example tbody" ).on( "click", ".btn-danger", function(event) {
  console.log( $( this ).text() );
  console.log($(this).html());

  event.preventDefault();
  // recherche data
  var x=[]
  $(this).children("td").each(function(index){
	  console.log( index + ": " + $( this ).text() );
	  x.push( $( this ).text());
  })
  console.log(x);
  $.ajax({
		dataType: "json",
		method: 'POST',
		url: $SCRIPT_ROOT + '/delRow',
		data: { "id": x[0],
		        "name": x[1],
				"symbol": x[2]
			   }
	});
}); */
$(document).on("click", ".btn-danger", function(event){
	event.preventDefault();
	console.log( $( this ).text() );
	console.log($(this).html());
	// recherche data
    var x=[]
	$(this).parents("tr").find("td:not(:last-child)").each(function(index){
			//console.log( index + ": " + $( this ).text() );
			x.push( $( this ).text());
	});
	console.log(x);
	$.ajax({
		dataType: "json",
		method: 'POST',
		url: $SCRIPT_ROOT + '/delRow',
		data: { "id": x[0],
		        "name": x[1],
				"symbol": x[2]
			   }
	});
	$(this).parents("tr").remove();
	$(".btn-info.add-new").removeAttr("disabled");
});

