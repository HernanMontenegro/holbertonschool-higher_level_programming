#!/usr/bin/node

const req = require('request');
const av = process.argv;
const options = {
  url: av[2],
  method: 'GET'
};

req(options, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    Ses(JSON.parse(body));
  }
});

function Ses (ret_json) {
  let films = 0;
  const results = ret_json.results;

  for (key in results) {
    for (let i = 0; i < results[key].characters.length; i++) {
      const item = results[key].characters[i];
      if (item == 'https://swapi-api.hbtn.io/api/people/18/') {
        films++;
      }
    }
  }

  console.log(films);
}
