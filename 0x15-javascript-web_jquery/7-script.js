/* This script fetches the character name from the provided URL and displays
   it in the HTML tag DIV#character. */

$(document).ready(function () {
  // Wait for the document to be fully loaded before making the API request

  // Make a GET request to fetch the character name from the URL
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Update the content of the <div> with the character name
    $('#character').text(data.name);
  });
});
