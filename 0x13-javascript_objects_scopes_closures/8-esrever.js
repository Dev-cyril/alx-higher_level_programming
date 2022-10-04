#!/usr/bin/node

exports.esrever = function (list) {
  let newArr =  list.map(list.pop, [... list]);
  return (newArr);
};
