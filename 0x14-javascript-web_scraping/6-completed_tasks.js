#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, { json: true }, (err, response, body) => {
  if (err) {
    console.log('error:', err);
    return;
  }

  const tasksCompleted = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
