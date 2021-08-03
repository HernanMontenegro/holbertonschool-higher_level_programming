#!/usr/bin/node

const dict = require('./101-data').dict;

const new_obj = new Object();

for (const key in dict) {
  if (!new_obj.hasOwnProperty(dict[key])) {
    new_obj[dict[key]] = [];
  }

  new_obj[dict[key]].push(key);
}

console.log(new_obj);
