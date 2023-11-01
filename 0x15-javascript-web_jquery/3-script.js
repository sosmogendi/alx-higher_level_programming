/* This script adds the class 'red' to the <header> element when the user clicks
   on the <div> with the ID 'red_header'. */

$(document).ready(function () {
  // Wait for the document to be fully loaded before manipulating elements
  
  // Select the <div> with the ID 'red_header' and add a click event handler
  $("#red_header").click(function () {
    // Add the 'red' class to the <header> element
    $("header").addClass("red");
  });
});
