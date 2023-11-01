#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: node 4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const filmsData = JSON.parse(body).results;
    const characterId = '18';
    const moviesWithWedge = filmsData.filter(movie =>
      movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );
    console.log(moviesWithWedge.length);
  } else {
    console.error(`Status code: ${response.statusCode}`);
  }
});
