#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url + id, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (const i of characters) {
    request.get(i, function (error, response, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
