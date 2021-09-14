#!/usr/bin/node

const av = process.argv;
const req = require('request');

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    req(url, function (error, res, body) {
      if (!error && res.statusCode == 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

async function main () {
  const url = `https://swapi-api.hbtn.io/api/films/${av[2]}`;
  const res = await doRequest(url);
  const arr = JSON.parse(res);

  for (let j = 0; j < arr.characters.length; j++) {
    const chrUrl = arr.characters[j];
    const charData = await doRequest(chrUrl);
    const name = JSON.parse(charData).name;
    console.log(name);
  }
}

main();
