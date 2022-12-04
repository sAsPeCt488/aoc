
let fs = require('fs');
let inventory = fs.readFileSync('01_input.txt').toString().split("\r\n");

let elf = [];
let elves = [];

for (let snack of inventory) {
	if (snack == '') {
		elves.push(elf.reduce((a, b) => a + b));
		elf = [];
		continue;
	}
	elf.push(parseInt(snack));
}

const max_calories = Math.max(...elves);
console.log("Part 1:", max_calories);

elves.sort().reverse();
const sum_of_3_max = elves.slice(0, 3).reduce((a, b) => a + b);
console.log("Part 2: ", sum_of_3_max);