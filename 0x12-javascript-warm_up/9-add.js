#!/usr/bin/node
function add (a, b) {
  a *= 1;
  b *= 1;
  console.log(a + b);
}
add(process.argv[2], process.argv[3]);
