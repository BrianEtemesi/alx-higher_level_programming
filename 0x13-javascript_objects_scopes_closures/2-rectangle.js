#!/usr/bin/node
// class Rectangle with width and height attributes
// if width or height <= 0, create empty object
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 ) {
      this.width = w;
      this.height = h;
	}
  }
}
module.exports = Rectangle;
