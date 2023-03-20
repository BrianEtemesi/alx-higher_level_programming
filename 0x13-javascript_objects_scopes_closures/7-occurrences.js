#!/usr/bin/node
// defines a functin that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  const length = list.length;
  let occ = 0;
  for (let i = 0; i < length; i++) {
    if (list[i] === searchElement) {
      occ++;
    }
  }
  return occ;
};
