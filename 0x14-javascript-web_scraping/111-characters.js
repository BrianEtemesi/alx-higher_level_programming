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
    (async () => {
      try{
        for await (let i of actors) {
          const response = await request(i, (error, response, body) => {
            const actor = JSON.parse(response.body);
            console.log(actor.name);
		  })
		}
	  } catch (error) {
        console.log(error.response.body);
	  }
	})();
  }
});
