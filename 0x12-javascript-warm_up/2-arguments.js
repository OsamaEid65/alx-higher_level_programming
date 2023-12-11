#!/usr/bin/node

const command = process.argv.length - 2;

if (command === 0) {
  console.log("No argument");
} else if (command === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}

