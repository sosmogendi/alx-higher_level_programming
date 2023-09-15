#!/usr/bin/node

/* 'addMeMaybe' function that takes two arguments: number and theFunction. */
function addMeMaybe(number, theFunction) {
	/* Increment the 'number' by 1. */
	const result = number + 1;

	/* Call the provided 'theFunction' with the incremented 'number'. */
	theFunction(result);
}

/** Export the 'addMeMaybe' function so it can be accessed from outside. */
module.exports.addMeMaybe = addMeMaybe;

