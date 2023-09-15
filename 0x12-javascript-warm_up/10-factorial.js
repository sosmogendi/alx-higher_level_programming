#!/usr/bin/node

function factorial(n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }
  if (n === 0) {
    return 1; // Factorial of 0 is 1
  }
  return n * factorial(n - 1);
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
