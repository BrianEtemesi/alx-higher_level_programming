#!/usr/bin/node
// prints number of argument already printed
let count = 0;
exports.logMe = function (item) {
  console.log(count.toString() + ': ' + item);
  count++;
};
