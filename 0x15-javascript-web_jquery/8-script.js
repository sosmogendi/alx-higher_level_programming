/* This script fetches and lists the title for all movies from the provided URL
   and displays them in the HTML tag UL#list_movies. */

$(document).ready(function () {
  // Wait for the document to be fully loaded before making the API request

  // Make a GET request to fetch the movie titles from the URL
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Iterate through each movie and append its title to the list
    data.results.forEach(function (movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  }
