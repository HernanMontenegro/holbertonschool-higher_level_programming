#!/usr/bin/node

const req = require('request');
const reqp = require('request-promise');
const av = process.argv;
const options = {
  url: `https://swapi-api.hbtn.io/api/films/${av[2]}`,
  method: 'GET'
};

req(options, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    Ses(JSON.parse(body));
  }
});

async function Ses (obj) {
  for (let i = 0; i < obj.characters.length; i++) {
    const element = obj.characters[i];
    const options = {
      url: element,
      method: 'GET'
    };
    const prom = reqp(options);
    const body = await prom;

    console.log(JSON.parse(body).name);
  }
}
