#!/usr/bin/node
process.argv.sort();
process.argv.reverse();
console.log((process.argv.length > 3) ? process.argv[1] : 0);
