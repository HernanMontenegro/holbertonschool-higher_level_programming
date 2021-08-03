#!usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w === undefined || isNaN(parseInt(w)) || w === 0 || parseInt(w) < 0) { return; }
    if (h === undefined || isNaN(parseInt(h)) || h === 0 || parseInt(h) < 0) { return; }

    this.width = w;
    this.height = h;
  }
};
