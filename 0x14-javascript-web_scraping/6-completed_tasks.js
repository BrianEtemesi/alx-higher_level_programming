#!/usr/bin/node
// computes number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const dict = {};
    body = JSON.parse(body);
    for (let i = 1; i <= 10; i++) {
      let nCompleted = 0;
      for (const j in body) {
        if (body[j].userId === i && body[j].completed === true) {
          nCompleted++;
        }
      }
      dict[i.toString()] = nCompleted;
    }
    console.log(dict);
  }
});
