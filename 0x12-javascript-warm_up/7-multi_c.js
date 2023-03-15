#!/usr/bin/node
// Prints string x number of times. x = argument passed
const arg = process.argv[2];
const number = parseInt(arg);
function myFunc (num) {
  if ((num / num) === 1) {
    if (num > 0) {
      for (let i = 0; i < num; i++) {
        console.log('C is fun');
      }
    }
  } else {
    console.log('Missing number of occurrences');
  }
}

myFunc(number);
