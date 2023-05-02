#!/usr/bin/node
// prints all characters of a Star Wars movie

const movieId = process.argv[2] + '/';
const request = require('request');

for (let i = 1; i <= 87; i++) {
  const url = 'https://swapi-api.alx-tools.com/api/people/' + i;
  request(url, (error, response, body) => {
    if (!error) {
      const actor = JSON.parse(body);
      const films = actor.films;
      for (const j in films) {
        if (films[j].endsWith(movieId)) {
          console.log(actor.name);
        }
      }
    }
  });
}
