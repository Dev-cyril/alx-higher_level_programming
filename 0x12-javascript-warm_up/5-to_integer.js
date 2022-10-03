#!/usr/bin/node
let num = process.argv[2]*1
console.log((num !== NaN) ? `My number: ${Math.floor(num)}` : 'Not a number');
