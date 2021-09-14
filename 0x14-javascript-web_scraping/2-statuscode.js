#!/usr/bin/node

const req = require('request');
const av = process.argv;

const options = {
  url: av[2],
  method: 'GET'
};

req(options, function (err, res, body) {
  console.log(`code: ${res.statusCode}`);
  if (err) {
    console.log(err);
  }
});
