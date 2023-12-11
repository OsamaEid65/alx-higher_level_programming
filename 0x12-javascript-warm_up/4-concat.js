#!/usr/bin/node

const args = process.argv.slice(2);
const arg1 = args[0];
const arg2 = args[1];

if (args.length === 0) {
  console.log('undefined is undefined');
} else if (args.length === 1) {
  console.log(arg1 + ' is undefined');
} else {
  console.log(arg1 + ' is ' + arg2);
}

