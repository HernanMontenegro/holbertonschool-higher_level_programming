#!/usr/bin/node

const req = require('request');
const fs = require('fs');
const av = process.argv;
const options = {
  url: av[2],
  method: 'GET'
};

req(options, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(av[3], body, function (err) {
      if (err) return console.log(err);
    });
  }
});
