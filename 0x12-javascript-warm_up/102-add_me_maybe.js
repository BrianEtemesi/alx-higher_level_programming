#!/usr/bin/node
// increments and calls a function
exports.addMeMaybe = function (number, theFunction) {
  const nb = number + 1;
  theFunction(nb);
};
