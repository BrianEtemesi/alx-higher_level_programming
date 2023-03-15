#!/usr/bin/node
// searches the 2nd biggest int in list of arguments
const len = process.argv.length;
if (len < 4) {
  console.log(1);
} else {
  let numList = [];
  for (let i = 2; i < len; i++) {
    numList.push(parseInt(process.argv[i]));
  }
  numList.sort();
  numList.reverse();
  console.log(numList[1]);
}
