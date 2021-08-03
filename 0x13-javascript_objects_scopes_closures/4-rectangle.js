#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (isNaN(parseInt(w)) || w === 0 || parseInt(w) < 0) { return; }
    if (isNaN(parseInt(h)) || h === 0 || parseInt(h) < 0) { return; }

    this.width = w;
    this.height = h;
  }

  print () {
    console.log(('X'.repeat(this.width) + '\n').repeat(this.height).slice(0, -1));
  }

  rotate () {
    const auxH = this.height;

    this.height = this.width;
    this.width = auxH;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
