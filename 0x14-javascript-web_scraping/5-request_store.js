#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: node 5-request_store.js <URL> <FilePath>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFileSync(filePath, body, 'utf-8');
  } else {
    console.error(`Failed to retrieve content from ${url}`);
  }
});
