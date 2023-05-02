#!/usr/bin/node
// print number of movies where character 'Wedge Antilles' is present

const url = process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  if (!error) {
    body = JSON.parse(body);
    const movies = body.results;
    let nFilms = 0;
    for (const i in movies) {
      const charList = movies[i].characters;
      for (const actor in charList) {
        if (charList[actor].endsWith('/18/')) {
          nFilms++;
        }
      }
    }
    console.log(nFilms);
  }
});
