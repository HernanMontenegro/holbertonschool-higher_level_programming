#!/usr/bin/node

const num = parseInt(process.argv[2]);

console.log(factorial(num));

function factorial (num) {
  const parsed = parseInt(num);
  if (isNaN(parsed) || parsed === 0) {
    return 1;
  }

  return parsed * factorial(parsed - 1);
}
