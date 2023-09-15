#!/usr/bin/node

class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0)
		{
			this.width = w;
			this.height = h;
		}
		else
		{
			/* Create an empty object if w or h is not a positive integer */
			return {};
		}
	}

	print() {
		/* Print the rectangle using the character 'X' */
		for (let j = 0; j < this.height; j++)
		{
			console.log('X'.repeat(this.width));
		}
	}
}

module.exports = Rectangle;
