#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film of films) {
      if (film.characters.some((c) => c.endsWith('/18/'))) {
        count++;
      }
    }
    console.log(count);
  }
});
