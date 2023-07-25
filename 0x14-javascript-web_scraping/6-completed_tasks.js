#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {

  if (error) {
    console.error('error:', error);
    return;
  }

  const todos = JSON.parse(body);

  const completedTasks = {};

  for(let todo of todos) {
    if (todo.completed) {
      const userId = todo.userId.toString();
      if (!completedTasks[userId]) {
        completedTasks[userId] = 0;
      }
      completedTasks[userId]++; 
    }
  }

  console.log(completedTasks);

});