#!/usr/bin/node
// prints all characters of a star wars movie
// prints in a particular order

const movieId = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(url, (error, response, body) => {
  if (!error) {
    film = JSON.parse(body);
    actors = film.characters;
	for (let i = 0; i < actors.length; i++) {
      request(actors[i], (error, response, body) => {
        if (!error) {
          actor = JSON.parse(body);
          console.log(actor.name);
		}
	  });
	}
  }
});
