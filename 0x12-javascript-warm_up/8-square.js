#!/usr/bin/node

let size = process.argv[2];

if (size === undefined || isNaN(parseInt(size, 10))) {
    console.log('Missing size');
    return;
}

for (let i = 0; i < size; i++) {
    console.log(("X".repeat(size)));
}
