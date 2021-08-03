#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { c = 'X'; }

    console.log((c.repeat(this.width) + '\n').repeat(this.height).slice(0, -1));
  }
};
