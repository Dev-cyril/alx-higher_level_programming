#!/usr/bin/node
const num = process.argv[2] * 1;
console.log((isNaN(num)) ? 'Not a number' : `My number: ${Math.floor(num)}`);
