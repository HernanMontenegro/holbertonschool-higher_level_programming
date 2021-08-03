#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

const str1 = fs.readFileSync(argv[2]).toString();
const str2 = fs.readFileSync(argv[3]).toString();

fs.writeFile(argv[4], str1 + str2, { overwrite: true }, function (err) {
  if (err) throw err;
});
