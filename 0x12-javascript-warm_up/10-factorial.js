#!/usr/bin/node
// computes and prints a factorial
const num = parseInt(process.argv[2]);
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(num));
