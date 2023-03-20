#!/usr/bin/node
// class Square that inherits from 'Rectangle'
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super();
    if (size > 0) {
	  this.width = size;
      this.height = size;
    }
  }
}
module.exports = Square;
