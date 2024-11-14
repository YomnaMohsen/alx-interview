#!/usr/bin/node
// display charcters in movie with certain id
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (error, response, body) => {
  if (!error & response.statusCode === 200) {
    const data = JSON.parse(body);
    const charactersurl = data.characters;

    charactersurl.forEach(url => {
      request(url, (error, response, body) => {
        if (!error & response.statusCode === 200) {
          const charname = JSON.parse(body);
          console.log(charname.name);
        } else {
          console.log('error', error);
        }
      });
    });
  } else {
    console.log('error', error);
  }
});
