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
			return {};
		}
	}
	print() {
		/* Print the rectangle using the character 'X'*/
		for (let i = 0; i < this.height; i++)
		{
			console.log('X'.repeat(this.width));
		}
	}
	rotate() {
		/* Exchange the width and height of the rectangle*/
		const tmp = this.width;
		this.width = this.height;
		this.height = tmp;
	}
	double() {
		/* Double the width and height of the rectangle*/
		this.width *= 2;
		this.height *= 2;
	}
}
module.exports = Rectangle;
