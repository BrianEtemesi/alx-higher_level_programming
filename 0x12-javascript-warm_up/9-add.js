#!/usr/bin/node
// prints the addition of two integers passed as arguments
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);
function add (a, b) {
  console.log(a + b);
}
add(num1, num2);
