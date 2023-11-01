/* This script adds a <li> element to the list UL.my_list when the user clicks
   on the <div> with the ID 'add_item'. The new element must be <li>Item</li>. */

$(document).ready(function () {
  // Wait for the document to be fully loaded before manipulating elements

  // Select the <div> with the ID 'add_item' and add a click event handler
  $("#add_item").click(function () {
    // Create a new <li> element with the text "Item"
    const newListItem = $("<li>Item</li>");
    
    // Add the new <li> element to the list UL.my_list
    $("ul.my_list").append(newListItem);
  });
});
