#!/usr/bin/node
// computes number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const dict = {};
    body = JSON.parse(body);
    console.log(body);
  }
});
