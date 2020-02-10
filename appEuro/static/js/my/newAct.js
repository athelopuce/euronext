/* javascript page newAct
* add-new -> .btn-info.add-new
* add -> .btn-primary
* edit -> .btn-success
* delete -> .btn-danger */

// Ajout ligne (row) à la fin du tableau on button click ".btn-info.add-newr"
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
	$(".btn-primary").hide(); // au démarrage
	var actions = $("#newActTab td:last-child").html(); // ajout des 3 buttons edit, add et del
	// Append table with add row form on add new button click
    $(".btn-info.add-new").click(function(){
		$(this).attr("disabled", "disabled");
		var index = $("#newActTab tbody tr:last-child").index();
		console.log('index add-new av inc:', index);
		if (index == -1) { index = 0;} 
		index++;
		console.log('index add-new:', index);
        var row = '<tr>' +
			'<td class="d-none">' + index +'</td>' +
            '<td><input type="text" class="form-control" name="name" id="name"></td>' +
            '<td><input type="text" class="form-control" name="symbol" id="symbol"></td>' +
			'<td>' + actions + '</td>' +
			'</tr>';
    	$("#newActTab").append(row);		
		$("#newActTab tbody tr").eq(index).find(".btn.btn-primary, .btn.btn-success").toggle();
        $('[data-toggle="tooltip"]').tooltip();
	});
});

// Delete row on delete button click ".btn-danger"
$(document).on("click", ".btn-danger", function(event){
	event.preventDefault();
	console.log( $( this ).text() );
	console.log($(this).html());
	// stock data in var x
    var x=[]
	$(this).parents("tr").find("td:not(:last-child)").each(function(index){
			//console.log( index + ": " + $( this ).text() );
			x.push( $( this ).text());
	});
	console.log('del:', x);
	$.ajax({
		dataType: "json",
		method: 'POST',
		url: $SCRIPT_ROOT + '/delRow',
		data: { "id": x[0],
		        "name": x[1],
				"symbol": x[2],
				"table":"newAct"
			   }
	});
	$(this).parents("tr").remove();
	$(".btn-info.add-new").removeAttr("disabled");
});

// Edit row on edit button click ".btn-success"
$(document).on("click", ".btn-success", function(){		
	$(this).parents("tr").find("td:not(:last-child)").each(function(){
		$(this).html('<input type="text" class="form-control" value="' + $(this).text() + '">');
	});		
	//$(this).parents("tr").find(".btn-primary, .btn-success").toggle();
	$(this).parents("tr").find(".btn-success").hide();
	$(this).parents("tr").find(".btn-primary").show();
	$(".btn-info.add-new").attr("disabled", "disabled");
});

// Add contenus on add button click ".btn-primary"
$(document).on("click", ".btn-primary", function(){
	var empty = false;
	var input = $(this).parents("tr").find('input[type="text"]');
	// si contenu vide
	input.each(function(){
		if(!$(this).val()){
			$(this).addClass("error");
			empty = true;
		} else{
			$(this).removeClass("error");
		}
	});
	$(this).parents("tr").find(".error").first().focus();
	if(!empty){
		input.each(function(){
			$(this).parent("td").html($(this).val());
		});			
		//$(this).parents("tr").find(".btn-success").hide()
		$(this).parents("tr").find(".btn-success").show();
		$(this).parents("tr").find(".btn-primary").hide();
		$(".btn-info.add-new").removeAttr("disabled");
	}
	// envoi data au serveur
	var x=[]
	$(this).parents("tr").find("td:not(:last-child)").each(function(index){
			//console.log( index + ": " + $( this ).text() );
			x.push( $( this ).text());
	});
	console.log('data:', x);
	
	/* Mémorise index de la ligne modifiée */
	var index = $(this).parents("tr").find("td").first();
	console.log('ligne add:', index);
	
	$.ajax({
		method: 'POST',
		url: $SCRIPT_ROOT + '/editRow',
		data: { "id": x[0],
		        "name": x[1],
				"symbol": x[2],
				"table":"newAct"
			   },
		dataType: "json",
		success: function(resp) {
			//console.log('response idAct: ' + resp.idAct); // la reponse de json
			console.log('index retour add:', index.eq(0))
			index.eq(0).text(resp.idAct);
			$('.success').show();
			$('.success').delay(3000).fadeOut();
		}
	});
});
