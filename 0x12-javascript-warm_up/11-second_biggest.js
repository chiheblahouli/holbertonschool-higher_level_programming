#!/usr/bin/node
/* second biggest */
const a = process.argv;
if (a.length <= 3) {
  console.log(0);
} else {
  const array = a.slice(2);
  console.log(array.sort((a, b) => a - b).reverse()[1]);
}
