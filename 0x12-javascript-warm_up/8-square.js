#!/usr/bin/node
// prints a square using the character X
const arg = process.argv[2];
const size = parseInt(arg);
if ((size / size) === 1) {
  if (size > 0) {
    let x = '';
    for (let i = 0; i < size; i++) {
      x = x + 'X';
    }
    let i = 0;
    while (i < size) {
      console.log(x);
      i++;
    }
  }
} else {
  console.log('Missing size');
}
