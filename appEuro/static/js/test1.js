/* Test fonction a+ b*/
// https://flask.palletsprojects.com/en/1.1.x/patterns/jquery/
/*
addnumber.html
*/
$(function() {
    $('a#calculate').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });
  });