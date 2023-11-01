/* This script updates the text of the <header> element to 'New Header!!!' when
   the user clicks on the <div> with the ID 'update_header'. */

$(document).ready(function () {
  // Wait for the document to be fully loaded before manipulating elements

  // Select the <div> with the ID 'update_header' and add a click event handler
  $("#update_header").click(function () {
    // Update the text of the <header> element to 'New Header!!!'
    $("header").text("New Header!!!");
  });
});
