#!/usr/bin/node
// print number of movies where character 'Wedge Antilles' is present

const url = process.argv[2];
const request = require('request');

let i = 1;
//let occurence = 0;
let actorList;
while (i < 8) {
  const movieUrl = url + '/' + i.toString();
  request(movieUrl, (error, response, body) => {
    if (!error) {
      body = JSON.parse(body);
      actorList = body.characters;
    }
  console.log(typeof actorList);
  });
  i++;
}


/*   
 *   const id = 18;
      const charApi = 'https://swapi-api.alx-tools.com/api/people/' + id + '/';
      console.log(charApi);
      for (const actor in actorList) {
		if (actorList[actor] == charApi) {
          occurence = occurence + 1;
        }
      }
    }
  i++;
  console.log(occurence);
}
console.log(i);
*/
