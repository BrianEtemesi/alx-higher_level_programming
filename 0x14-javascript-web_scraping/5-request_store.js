#!/usr/bin/node
// gets the content of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, (error, response, body) => {
  if (!error) {
    const content = body;
    fs.writeFile(fileName, content, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
