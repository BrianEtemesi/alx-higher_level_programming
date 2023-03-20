#!/usr/bin/node
// class Rectangle with attributes; width and height
// instance method 'print' to print rectangle using 'X'
// instance method 'rotate'; exchanges width and height
// instance method 'double'; doubles width and height
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

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
