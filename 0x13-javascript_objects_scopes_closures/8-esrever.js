#!/usr/bin/node
// returns the reversed version of a list
exports.esrever = function (list) {
  const copyList = [...list];
  const length = list.length;
  let j = length - 1;
  for (let i = 0; i < length; i++) {
    list[i] = copyList[j];
    j--;
  }
  return list;
};
