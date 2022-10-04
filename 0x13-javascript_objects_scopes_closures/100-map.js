#!/usr/bin/node

const arr = require('./100-data').list;
let newArr = [];
console.log(arr);
for (let i in arr) {
  newArr.map(arr[i] * i)
}
console.log(newArr);
