#!/usr/bin/node
// converts a number from base 10 to one passed as argument
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
