/* This script updates the text color of the <header> element to red (#FF0000)
   when the user clicks on the <div> with the ID 'red_header'. */

$(document).ready(function () {
  // Wait for the document to be fully loaded before manipulating elements
  
  // Select the <div> with the ID 'red_header' and add a click event handler
  $("#red_header").click(function () {
    // Change the text color of the <header> element to red
    $("header").css("color", "#FF0000");
  });
});
