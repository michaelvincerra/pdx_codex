/**
 * Created by michaelevan on 5/31/17.
 */
<!--create this file with the jquery methods-->


"use strict";


// $('#section');
//
//
// $('#button');
//
//
// function addToList(item) {
//     $('#reminder').append(item);
//
// }
//
// $('#input:eq(1)').on('click',
//     function(event) {
//
//     var $input = $('#reminder').val();
//     eventpreventDefault();
//     addToList($input);
//
//     });

$('#input').css('border', '2px green');


function incrementCounter() {
  // increments the counter by 1
  var $counter= $("#counter").text();
  var intify = Number($counter);
  var counted = String(intify+1);
  $('#counter').html(counted);
}


function addToList(item) {                                  // creates new 'item'
  var $listItem = $('<li class="myclass">').text(item);     // $listItem = newly created using $('') and
  $listItem.on('click', function(event) {                   // event handler uses .on selector method
    // event handler for clicking on list items
    $(this).css('text-decoration', 'line-through');         // applies line-through using 'this' nearest, to 'item' created.
    incrementCounter();                                     // invokes incrementCounter on click action
  });

  $('#list').append($listItem);                             // using id='list' reference, append $listItem element.
}


$('#sub_button').on('click', function(event){               // creates event on selecting submit button
  // event handler for handling todo item
  event.preventDefault();                                   // prevent default behavior of form to reset on refresh
  var output = $('#todo').val();                            // ????
  addToList(output);                                        // invoke addToList function above to create new 'item'
  $('#todo').val('');                                       // in the todo input box, clear and replace with nothing
});


$('#sub_button').on('click', function (event) {
    // change button color on click
    event.preventDefault();
    $(this).css("color", "yellow");
}, function () {
    $(this).css("color", "blue");
});







// $('#input:eq()').on('click',
//     function(event){
//         alert('Yes!')
//
//     });
