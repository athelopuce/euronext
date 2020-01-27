//newActions.js
// https://www.tutorialrepublic.com/codelab.php?topic=bootstrap&file=table-with-add-and-delete-row-feature


// add-new -> .btn-info.add-new
// add -> .btn-primary
// edit -> .btn-success
// delete -> .btn-danger

$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip();
	$(".btn-primary").hide()
	var actions = $("table td:last-child").html();
	// Append table with add row form on add new button click
    $(".btn-info.add-new").click(function(){
		$(this).attr("disabled", "disabled");
		var index = $("table tbody tr:last-child").index();
        var row = '<tr>' +
            '<td><input type="text" class="form-control" name="name" id="name"></td>' +
            '<td><input type="text" class="form-control" name="department" id="department"></td>' +
            '<td><input type="text" class="form-control" name="phone" id="phone"></td>' +
			'<td>' + actions + '</td>' +
        '</tr>';
    	$("table").append(row);		
		$("table tbody tr").eq(index + 1).find(".btn-primary, .btn-success").toggle();
        $('[data-toggle="tooltip"]').tooltip();
    });
	// Add row on add button click
	$(document).on("click", ".btn-primary", function(){
		var empty = false;
		var input = $(this).parents("tr").find('input[type="text"]');
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
    });
	// Edit row on edit button click
	$(document).on("click", ".btn-success", function(){		
        $(this).parents("tr").find("td:not(:last-child)").each(function(){
			$(this).html('<input type="text" class="form-control" value="' + $(this).text() + '">');
		});		
		//$(this).parents("tr").find(".btn-primary, .btn-success").toggle();
		$(this).parents("tr").find(".btn-success").hide();
		$(this).parents("tr").find(".btn-primary").show();
		$(".btn-info.add-new").attr("disabled", "disabled");
    });
	// Delete row on delete button click
	$(document).on("click", ".btn-danger", function(){
        $(this).parents("tr").remove();
		$(".btn-info.add-new").removeAttr("disabled");
    });
});
