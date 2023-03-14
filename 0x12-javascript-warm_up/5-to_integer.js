#!/usr/bin/node
// prints number if first argument can be converted to an integer
const arg = process.argv[2];
const num = parseInt(arg);
if ((num / num) === 1) {
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
