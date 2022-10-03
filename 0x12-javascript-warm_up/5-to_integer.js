#!/usr/bin/node
<<<<<<< HEAD
let num = process.argv[2]*1
console.log((num !== NaN) ? `My number: ${Math.floor(num)}` : 'Not a number');
=======
const num = process.argv[2] * 1;
console.log((isNaN(num)) ? 'Not a number' : `My number: ${Math.floor(num)}`);
>>>>>>> e5f3e63493759d68ffa5cdacf226753a8ae5ecf1
