#!/usr/bin/node
// class Rectangle with width and height attributes
// instance method to print rectangle using 'X'
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let size = '';
    for (let i = 0; i < this.width; i++) {
      size = size + 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(size);
    }
  }
}
module.exports = Rectangle;
