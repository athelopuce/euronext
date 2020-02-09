/* javascript page newAct
* add-new -> .btn-info.add-new
* add -> .btn-primary
* edit -> .btn-success
* delete -> .btn-danger */

// Ajout ligne (row) à la fin du tableau on button click ".btn-info.add-newr"
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
	$(".btn-primary").hide(); // au démarrage
	var actions = $("#newOrd td:last-child").html(); // ajout des buttons edit et del
	// Append table with add row form on add new button click
    $(".btn-info.add-new").click(function(){
		$(this).attr("disabled", "disabled");
		var index = $("#newOrd tbody tr:last-child").index();
        var row = '<tr>' +
			'<td class="d-none">' + index + 1 + '</td>' +
			'<td><input type="text" class="form-control" name="sens"></td>' +
			'<td><input type="text" class="form-control" name="date"></td>' +
			'<td><input type="text" class="form-control" name="PriceAchat"></td>' +
            '<td><input type="text" class="form-control" name="quantity"></td>' +
            '<td><input type="text" class="form-control" name="idAct"></td>' +
			'<td>' + actions + '</td>' +
			'</tr>';
    	$("#newOrd").append(row);		
		$("#newOrd tbody tr").eq(index + 1).find(".btn-primary, .btn-success").toggle();
        $('[data-toggle="tooltip"]').tooltip();
	});
});

// Delete row on delete button click ".btn-danger"
$(document).on("click", ".btn-danger", function(event){
	event.preventDefault();
	// console.log( $( this ).text() );
	// console.log($(this).html());
	// stock data in var x
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
		        "sens": x[1],
				"date": x[2],
				"PriceAchat": x[3],
				"quantity":x[4],
				"idAct":x[5],
				"table":"newOrd"
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
	//console.log(x);
	
	/* Mémorise index de la ligne modifiée */
	var index = $(this).parents("tr").find("td").first();
	//console.log(index);
	
	$.ajax({
		method: 'POST',
		url: $SCRIPT_ROOT + '/editRow',
		data: { "id": x[0],
		        "sens": x[1],
				"date": x[2],
				"PriceAchat": x[3],
				"quantity":x[4],
				"idAct":x[5],
				"table":"newOrd"
			   },
		dataType: "json",
		success: function(resp) {
			//console.log('response idAct: ' + resp.idAct); // la reponse de json
			//console.log( index.eq(0))
			index.eq(0).text(resp.idOrd);
			$('.success').show();
			$('.success').delay(3000).fadeOut();
		}
	});
});
