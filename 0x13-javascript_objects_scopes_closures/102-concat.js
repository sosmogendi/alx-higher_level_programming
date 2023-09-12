#!/usr/bin/node
const fs = require('fs');

const FileA = process.argv[2];
const FileB = process.argv[3];
const FileC = process.argv[4];

if (!FileA || !FileB || !FileC) {
  console.error('Usage: ./102-concat.js <FileA> <FileB> <FileC>');
  process.exit(1);
}

fs.readFile(FileA, 'utf8', (err, data1) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }

  fs.readFile(FileB, 'utf8', (err, data2) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }

    const concatenatedData = data1 + data2;

    fs.writeFile(FileC, concatenatedData, (err) => {
      if (err) {
        console.error(err);
        process.exit(1);
      }

      console.log(`Concatenated files: ${FileA} + ${FileB} -> ${FileC}`);
    });
  });
});
