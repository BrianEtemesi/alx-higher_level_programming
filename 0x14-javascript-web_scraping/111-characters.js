#!/usr/bin/node

// prints all characters of a star wars movie
// prints in the order of requests sent

const movieId = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

async function printCharacters() {
  try {
    const response = await request(url);
    const film = JSON.parse(response);
    const actors = film.characters;
    for await (const actorUrl of actors) {
      const actorResponse = await request(actorUrl);
      const actor = JSON.parse(actorResponse);
      console.log(actor.name);
    }
  } catch (error) {
    console.error(error);
  }
}

printCharacters();

