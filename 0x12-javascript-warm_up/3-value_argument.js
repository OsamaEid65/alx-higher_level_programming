#!/usr/bin/node

const command = process.argv.slice(2);

if (command.length === 0) {
  console.log('No argument');
} else {
  for (let i = 0; i < command.length; i++) {
    console.log(command[i]);
  }
}

