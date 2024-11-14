#!/usr/bin/node
// display charcters in movie with certain id
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

const getchars = new Promise((resolve, reject) => {
  request.get(url, (err, response, body) => {
    if (!err) {
      try {
        resolve(JSON.parse(body).characters);
      } catch (error) {
        reject(error);
      }
    }
    reject(err);
  });
});

getchars.then((data) => {
  const chararr = [];
  for (const ch of data) {
    chararr.push(
      new Promise((resolve, reject) => {
        request.get(ch, (err, response, body) => {
          if (err) reject(err);
          try {
            resolve(JSON.parse(body).name);
          } catch (error) {
            reject(error);
          }
        });
      })
    );
  }
  Promise.all(chararr).then((names) => {
    for (const n of names) {
      console.log(n);
    }
  });
});
