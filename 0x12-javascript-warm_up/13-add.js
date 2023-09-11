#!/usr/bin/node

/* Define the 'add' function that takes two integers and returns their sum. */
function add(a, b) {
  return a + b;
}

/* Export the 'add' function so it can be accessed from outside. */
module.exports.add = add;
