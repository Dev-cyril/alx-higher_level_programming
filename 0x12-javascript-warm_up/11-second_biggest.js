#!/usr/bin/node
process.argv.sort();
process.argv.reverse();
const arr = [];
for (const i in process.argv) {
  arr.push(parseInt(process.argv[i]));
}
console.log((arr.length > 3) ? arr[1] : 0);
