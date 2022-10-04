#!/usr/bin/node

const arr = require('./100-data').list;
let newArr = [];
console.log(arr);
newArr.map((x, index) => x *index);
console.log(newArr);
