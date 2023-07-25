#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const characterId = 18;

request(url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
    return;
  }

  const movies = JSON.parse(body).results;
  let count = 0;

  for (const movie of movies) {
    const characters = movie.characters;

    if (characters.find(url => {
      const id = url.split('/').pop();
      return id === characterId.toString();
    })) {
      count++;
    }
  }

  console.log(count);
});
