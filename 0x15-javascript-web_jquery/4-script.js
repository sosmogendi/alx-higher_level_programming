/* This script toggles the class of the <header> element between 'red' and 'green'
   when the user clicks on the <div> with the ID 'toggle_header'. */

$(document).ready(function () {
  // Wait for the document to be fully loaded before manipulating elements

  // Select the <div> with the ID 'toggle_header' and add a click event handler
  $("#toggle_header").click(function () {
    // Toggle the class of the <header> element between 'red' and 'green'
    $("header").toggleClass("red green");
  });
});
