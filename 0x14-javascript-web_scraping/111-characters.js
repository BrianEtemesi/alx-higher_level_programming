#!/usr/bin/node

// prints all characters of a star wars movie
// prints in the order of requests sent

const movieId = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

(async () => {
  try{
    const response = await request(url, (error, response, body) => {
    const film = JSON.parse(response.body);  
    console.log(film);
	});
  } catch (error) {
    console.log(error.response.body);
  }
})();
