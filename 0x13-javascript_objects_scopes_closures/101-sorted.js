#!/usr/bin/node

const dict = require('./101-data').dict;

const newObj = {};

for (const key in dict) {
  if (!Object.prototype.hasOwnProperty.call(newObj, dict[key])) {
    newObj[dict[key]] = [];
  }

  newObj[dict[key]].push(key);
}

console.log(newObj);
