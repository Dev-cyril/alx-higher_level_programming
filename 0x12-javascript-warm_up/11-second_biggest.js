#!/usr/bin/node
process.argv.sort();
process.argv.reverse();
const arr = [];
for (const i in process.argv) {
  arr.push(process.argv[i] * 1);
}
arr.sort(function  (a, b) {
  return b - a;
});
console.log((arr.length > 3) ? arr[1] : 0);
