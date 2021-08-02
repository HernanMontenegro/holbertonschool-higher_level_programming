#!/usr/bin/node

const argv = process.argv;
let result = 0;

if (argv[2] !== undefined && argv.length !== 3) {
  const argvCpy = argv.slice(2, argv.length).map(function (item) {
    return parseInt(item, 10);
  });
  const indx = argvCpy.indexOf(Math.max.apply(null, argvCpy));

  argvCpy.splice(indx, 1);
  result = Math.max.apply(null, argvCpy);
}

console.log(result);
