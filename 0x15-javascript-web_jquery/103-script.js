/* This script fetches and prints the translation of "Hello" based on the
   language code entered by the user when the button is clicked or Enter is pressed. */

$(document).ready(function () {
  // Wait for the document to be fully loaded before handling events

  // Function to fetch and display the translation
  function fetchAndDisplayTranslation() {
    // Get the language code entered by the user
    const languageCode = $('#language_code').val();

    // Make a GET request to fetch the translation
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      // Display the translation in the HTML tag DIV#hello
      $('#hello').text(data.hello);
    });
  }

  // Add a click event handler to the Translate button
  $('#btn_translate').click(fetchAndDisplayTranslation);

  // Add a keypress event handler to the language code input field
  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      // Check if Enter key is pressed (keyCode 13)
      fetchAndDisplayTranslation();
    }
  });
});
