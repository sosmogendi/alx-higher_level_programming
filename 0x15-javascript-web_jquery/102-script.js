/* This script fetches and prints how to say "Hello" depending on the language
   entered in the INPUT#language_code. */

$(document).ready(function () {
  // Wait for the document to be fully loaded before handling events

  // Add click event handler for the Translate button
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val(); // Get the language code from the input

    // Make a GET request to fetch the translation
    $.get(`https://www.fourtonfish.com/hellosalut/?lang=${langCode}`, function (data) {
      // Update the content of the <div> with the translation
      $('#hello').text(data.hello);
    });
  });
});
