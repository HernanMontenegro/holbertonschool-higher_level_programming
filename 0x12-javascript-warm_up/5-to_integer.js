#!/usr/bin/node

const num = process.argv[2];
if (num !== undefined && !isNaN(parseInt(num, 10))) { console.log('My number: ' + parseInt(num, 10)); } else { console.log('Not a number'); }
