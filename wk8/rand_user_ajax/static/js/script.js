/**
 * Created by michaelevan on 6/2/17.
 */


"use strict";

function addData(users)  {

  $.each(users.results, function(index, user) {   // $each(array, function)... works like enumerate

      let picture = user.picture.large;                                     // assign variable to picture
      let title = user.name.title;                                          // assign variable to title
      let first = user.name.first;                                          // assign variable to first name
      let last = user.name.last;                                            // assign variable to last name

      let email = user.email;                                               // assign variable to user email
      let username = user.login.username;                                   // assign variable to username
      let reg_date = user.registered;                                       // assign variable to user registration date
      let dob = user.dob;                                                   // assign variable to user date of birth

      let $picture = $('<img>').attr('src', `${picture}`);                  // capture jquery variable picture
      let $name = $('<div>').text(`Name:  ${title} ${first} ${last}`);      // capture jquery variable tite, first, last
      let $email = $('<div>').text(`Email:  ${email}`);                     // capture jquery variable email
      let $username = $('<div>').text(`Username:  ${username}`);            // capture jquery variable username
      let $reg_date = $('<div>').text(`Registration:  ${reg_date}`);        // capture jquery variable registration date
      let $dob = $('<div>').text(`Date of birth:  ${dob}`);                 // capture jquery variable date of birth

      // Name: Mr Aventino Lima
      // Email: aventino.lima@example.com
      // Username: heavybutterfly582
      // Registration date: 10/2/2002
      // Birth date: 6/5/1994

      let $pictureBox = $('<div>', {'class':'picturebox'});         // write using jquery variable class picturebox
      let $frameBox = $('<div>', {'class': 'framebox'});            // write using jquery variable class framebox
      let $textBox = $('<div>', {'class': 'textbox'}).append($name, $email, $username, $reg_date, $dob); // write using jquery variable class textbox
      let $newBox = $('<article>', {'class': 'item box'});          // write using jquery variable class item + box

      $pictureBox.append($picture);                                 // append jquery picture in pictureBox
      $frameBox.append($pictureBox, $textBox);                      // append jquery pictureBox, textBox in frameBox
      $newBox.append($frameBox);                                    // append frameBox in newBox
      $('#row2').append($newBox);                                   // append newBox in HTML, #row2 using id tag
  });
}


function fetcher() {                                // creates new 'item'
    let data;                                       // declare variable data;

    $.ajax({                                        // ajax syntax in jquery
    url:'https://api.randomuser.me/',               // from where data is taken
    method: 'GET',                                  // method.  can be: get, post, etc.
    data: {'results': 5},                           // data results show only 5

    success: function(rsp){                         // on success, do following
        console.log(rsp);                           // show results in console log only
        data = rsp;                                 // data variable assigned result of function in success
        addData(rsp)                                // rsp, result of data, is parameter passed to addData, above.
    },
    error: function(err){                           // function to address error
        console.log(err);                           // on error show err message in console.
    }
});


}

$('#sub_button').on('click', function(event){    // creates event on click of submit button
  // event handler for creating user boxes
  event.preventDefault();                        // prevents default behaviour to erase event
  fetcher();                                     // invoke fetcher function above to create new 'item'
});
