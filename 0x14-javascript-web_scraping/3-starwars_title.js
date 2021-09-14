#!/usr/bin/node

const req = require('request');
const av = process.argv;

const options = {
  url: `https://swapi-api.hbtn.io/api/films/${av[2]}`,
  method: 'GET'
};

req(options, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  else {
    console.log(JSON.parse(body).title)
  }
});
