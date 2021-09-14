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

function Ses (array) {
  const result = {};
  for (let i = 0; i < array.length; i++) {
    const item = array[i];
    if (!item.completed) {
      continue;
    }
    const usrId = String(item.userId);
    if (result[usrId] !== undefined) {
      result[usrId]++;
    } else {
      result[usrId] = 1;
    }
  }
  console.log(result);
}
