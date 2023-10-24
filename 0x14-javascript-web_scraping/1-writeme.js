#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath || !contentToWrite) {
  console.error('Usage: node 1-writeme.js <file_path> "<string_to_write>"');
  process.exit(1);
}

fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('The file has been written successfully.');
  }
});
