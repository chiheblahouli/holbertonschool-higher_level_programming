#!/usr/bin/node
/* value of argument */
const x = process.argv[2];
if (x === undefined) {
  console.log('No argument');
} else {
  console.log(x);
}
