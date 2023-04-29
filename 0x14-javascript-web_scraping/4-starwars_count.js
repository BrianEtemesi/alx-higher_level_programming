#!/usr/bin/node
// print number of movies where character 'Wedge Antilles' is present

const url = process.argv[2];
const request = require('request');

let occurence = 0;
let sum = 0;
for (let i = 1; i < 8; i++) {
  const movieUrl = url + '/' + i;
  request(movieUrl, (error, response, body) => {
    if (!error) {
      body = JSON.parse(body);
      const actorList = body.characters;
      const id = 18;
      const charApi = 'https://swapi-api.alx-tools.com/api/people/' + id + '/';
      for (const actor in actorList) {
        if (actorList[actor] === charApi) {
          occurence++;
        }
      }
    }
	sum = sum + i;
    if (sum == 28) {
      console.log(occurence);
	}
  });
}
