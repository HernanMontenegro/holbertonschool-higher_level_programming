#!/usr/bin/node

let num = parseInt(process.argv[2]);

console.log(factorial(num));

function factorial(num)
{
    let parsed = parseInt(num);
    if (isNaN(parsed) || parsed == 0) {
        return 1;
    }

    return parsed * factorial(parsed - 1);
}

