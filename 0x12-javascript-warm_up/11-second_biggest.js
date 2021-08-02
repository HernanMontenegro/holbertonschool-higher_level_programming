#!/usr/bin/node

const argv = process.argv;

if (argv[2] === undefined || argv.length === 3) {
  console.log('0');
} else {
  let bigger = parseInt(argv[2]);
  let secondBigger = parseInt(argv[2]);

  for (let i = 2; i < argv.length; i++) {
    const currNum = parseInt(argv[i]);
    if (bigger < currNum) {
      bigger = currNum;
    }
  }

  for (let i = 0; i < argv.length; i++) {
    const currNum = parseInt(argv[i]);
    if (secondBigger < currNum && currNum !== bigger) {
      secondBigger = currNum;
    }
  }

  console.log(secondBigger);
}
