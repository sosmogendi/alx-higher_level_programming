#!/usr/bin/node

/* Define the 'callMeMoby' function that takes two arguments:
 * x (number of times) and theFunction (the function to execute).
 */
function callMeMoby(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction(); /* Execute the provided function 'x' times.*/
  }
}

/* Export the 'callMeMoby' function so it can be accessed from outside. */
module.exports.callMeMoby = callMeMoby;
