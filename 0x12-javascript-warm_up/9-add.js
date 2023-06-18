#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add (arg1, arg2) {
  return (arg1 + arg2);
}

console.log(add(parseInt(arg1), parseInt(arg2)));
