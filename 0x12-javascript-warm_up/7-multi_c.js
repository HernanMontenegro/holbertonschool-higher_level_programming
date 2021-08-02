#!/usr/bin/node

let x = process.argv[2];

if (x === undefined || isNaN(parseInt(x, 10))) {
    console.log('Missing number of occurrences');
    return;
}

for (let iter = 0; iter < x; iter++) {
    console.log('C is fun');
}
