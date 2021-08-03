#!/usr/bin/node

const Square_ = require('./5-square');

module.exports = class Square extends Square_ {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }

    console.log((c.repeat(this.width) + '\n').repeat(this.height).slice(0, -1));
  }
};
