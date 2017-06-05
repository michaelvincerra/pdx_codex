/**
 * Created by michaelevan on 5/31/17.
 */
<!--create this file with the jquery methods-->


"use strict";


$(".item").hover(function (event) {               // parameter  of jquery is a function with an event
    var hue = 'rgb('
        + (Math.floor(Math.random() * 256)) + ','
        + (Math.floor(Math.random() * 256)) + ','
        + (Math.floor(Math.random() * 256)) + ')';
    console.log(hue)
    $(this).css("background-color", hue);
    // $("#morpher").change(".item");
    var anima = $(this).text();
    $('#morpher').text(anima);

    }, function(event) {
    $("#morpher").text('PEACE!');

    if(!$(this).hasClass('counted')) {
        var oldVal = Number($("#counter").text());
        var newVal = oldVal+1;
        $("#counter").text(newVal);
        $(this).addClass('counted');
    }




});



    // $("#morpher").text(".item");






// $('#sub_button').on('click', function(event){               // creates event on selecting submit button
//   // event handler for handling todo item
//   event.preventDefault();                                   // prevent default behavior of form to reset on refresh
//   var output = $('#todo').val();                            // ????
//   addToList(output);                                        // invoke addToList function above to create new 'item'
//   $('#todo').val('');                                       // in the todo input box, clear and replace with nothing
// });
//
//





