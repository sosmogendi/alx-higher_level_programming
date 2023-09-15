#!/usr/bin/node
const { dict } = require('./101-data');

const userByOccurrence = {};

for (const userId in dict)
{
	const occurrence = dict[userId];
	if (!userByOccurrence[occurrence])
	{
		userByOccurrence[occurrence] = [];
	}
	userByOccurrence[occurrence].push(userId);
}

console.log(userByOccurrence);
