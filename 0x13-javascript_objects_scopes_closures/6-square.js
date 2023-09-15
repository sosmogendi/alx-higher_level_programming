#!/usr/bin/node

const ParentSquare = require('./5-square');

class Square extends ParentSquare {
	charPrint(c) {
		if (c === undefined)
		{
			c = 'X';
		}
			/* Print the square using the character 'c'*/
		for (let i = 0; i < this.height; i++)
		{
			console.log(c.repeat(this.width));
		}
	}
}

module.exports = Square;
