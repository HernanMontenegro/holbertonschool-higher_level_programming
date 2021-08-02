#!/usr/bin/node

let size = process.argv[2];

if (size === undefined || isNaN(parseInt(size, 10))) {
    console.log('Missing size');
    return;
}

let str = ("X".repeat(size) + '\n').repeat(size);
str = str.slice(0, -1);

console.log(str);
