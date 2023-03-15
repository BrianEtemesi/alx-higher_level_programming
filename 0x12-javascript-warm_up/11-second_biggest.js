#!/usr/bin/node
// searches the 2nd biggest int in list of arguments
const len = process.argv.length;
if (len < 4) {
  console.log(0);
} else {
  const numList = [];
  for (let i = 2; i < len; i++) {
    numList.push(parseInt(process.argv[i]));
  }
  numList.sort(function (a, b) { return a - b; });
  numList.reverse();
  console.log(numList[1]);
}
