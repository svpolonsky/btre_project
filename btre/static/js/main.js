const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Stas' additions

$(document).ready( function() {

    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery local!");
    });
});


$(document).ready( function() {

    $(function() {
        $('tr.parent td span.btn')
          .on("click", function(){
          var idOfParent = $(this).parents('tr').attr('id');
          $('tr.child-'+idOfParent).toggle('fast');
        });
        $('tr[class^=child-]').hide().children('td');
      });
    });