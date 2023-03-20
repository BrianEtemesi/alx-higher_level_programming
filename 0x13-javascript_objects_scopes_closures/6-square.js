#!/usr/bin/node
// class Square that inherits from `Square` of 5-square.js
// instance method `charPrint(c)` that prints square using character 'c'
const parentSquare = require('./5-square');
class Square extends parentSquare {
  charPrint (c) {
    if (c) {
      let dimention = '';
      for (let i = 0; i < this.width; i++) {
        dimention += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(dimention);
      }
    } else {
      super.print();
    }
  }
}
module.exports = Square;
