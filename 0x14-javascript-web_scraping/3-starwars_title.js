#!/usr/bin/node
// prints title of a starwars movie where episode number
// is the number passed as argument

const episode = process.argv[2];
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + episode;
request(url, (error, response, body) => {
  if (!error) {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
