/* This script fetches the translation of "hello" from the provided URL and
   displays it in the HTML tag DIV#hello. */

$(document).ready(function () {
  // Make a GET request to fetch the translation
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Update the content of the <div> with the translation
    $('#hello').text(data.hello);
  });
});
