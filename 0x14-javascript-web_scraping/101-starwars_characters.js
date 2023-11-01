#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 101-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    function getCharacterName(index) {
      if (index < characters.length) {
        request(characters[index], (charError, charResponse, charBody) => {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
            getCharacterName(index + 1);
          }
        });
      }
    }

    getCharacterName(0); // Start with the first character
  } else {
    console.error(`Status code: ${response.statusCode}`);
  }
});
