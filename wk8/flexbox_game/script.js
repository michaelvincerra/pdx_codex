/**
 * Created by michaelevan on 5/31/17.
 */
<!--create this file with the jquery methods-->


"use strict";


$(".item").hover(function (event) {                         // parameter  of jquery is a function with an event
    var hue = 'rgb('
        + (Math.floor(Math.random() * 256)) + ','
        + (Math.floor(Math.random() * 256)) + ','
        + (Math.floor(Math.random() * 256)) + ')';
    console.log(hue)

    $(this).css("background-color", hue);
    // $("#morpher").change(".item");
    let anima = $(this).text();
    $('#morpher').text(anima);

    }, function(event) {
    $("#morpher").text(`You selected: ${$(this).text()}` ); // In place of morpher, replace with selected box's text

    
    
    if(!$(this).hasClass('counted')) {
        let oldVal = Number($("#counter").text());
        let newVal = oldVal+1;
        $("#counter").text(newVal);
        $(this).addClass('counted');
    }
});


function addBox(item) {                                     // creates new 'item'
  let $newBox = $('<div>', {'class': 'item box'}).text(item);
  $('#container').append($newBox);                          // using id='list' reference, append $listItem element.
}

$('#sub_button').on('click', function(event){               // creates event on selecting submit button
  // event handler for handling ...
  event.preventDefault();
  // alert('Hello!');
  let output = $("#adder").val();                           // creates new text based on user input, val
  addBox(output);                                           // invoke addToList function above to create new 'item'
  $('#adder').val('');                                      // in the todo input box, clear and replace with nothing
});






