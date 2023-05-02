#!/usr/bin/node
// computes number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const dict = {};
    body = JSON.parse(body);
    if (body.length > 0) {
      let users = 0;
      for (const k in body) {
        if (body[k].userId > users) {
          users = body[k].userId;
        }
      }
      for (let i = 1; i <= users; i++) {
        let nCompleted = 0;
        for (const j in body) {
          if (body[j].userId === i && body[j].completed === true) {
            nCompleted++;
          }
        }
		if (nCompleted) {
          dict[i.toString()] = nCompleted;
		}
      }
    }
    console.log(dict);
  }
});
