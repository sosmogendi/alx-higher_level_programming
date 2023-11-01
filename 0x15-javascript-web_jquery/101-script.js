/* This script adds, removes, and clears LI elements from a list when the user
   clicks on the respective DIV elements. */

$(document).ready(function () {
  // Wait for the document to be fully loaded before handling events

  // Add a new <li> element to the list UL.my_list
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });

  // Remove the last <li> element from the list UL.my_list
  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  // Clear all <li> elements from the list UL.my_list
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
