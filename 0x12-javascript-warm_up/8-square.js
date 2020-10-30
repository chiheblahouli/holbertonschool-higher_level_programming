#!/usr/bin/node
/* printing */
let y = process.argv[2];
if (isNaN(y)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < y; i++) {
    console.log('Y'.repeat(y));
  }
}
