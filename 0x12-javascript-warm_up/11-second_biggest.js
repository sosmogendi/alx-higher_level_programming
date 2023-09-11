#!/usr/bin/node

function secondLargestNumber(args) {
  const integers = args.map(Number);

  if (integers.length < 2) {
    return 0;
  }

  let largestInt = -Infinity;
  let secondLargestInt = -Infinity;

  for (const num of integers) {
    if (num > largestInt) {
      secondLargestInt = largestInt;
      largestInt = num;
    } else if (num > secondLargestInt && num < largestInt) {
      secondLargestInt = num;
    }
  }

  return secondLargestInt;
}

const args = process.argv.slice(2);

console.log(secondLargestNumber(args));
