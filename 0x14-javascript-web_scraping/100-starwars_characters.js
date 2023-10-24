#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 100-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    function getCharacterName(url) {
      request(url, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    }

    const promises = characters.map((characterUrl) => {
      return new Promise((resolve) => {
        getCharacterName(characterUrl);
        resolve();
      });
    });

    Promise.all(promises);
  } else {
    console.error(`Status code: ${response.statusCode}`);
  }
});
