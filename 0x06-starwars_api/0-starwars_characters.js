#!/usr/bin/node

const request = require('request')
let movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`

request(url, (error, response, body) => {
	if (!error && response.statusCode == 200) {
		const film = JSON.parse(body);

		// Get list of character URLs
		const characterUrls = film.characters;

		// Recursive function to fetch each character

		function fetchCharacter(i) {
			if ( i < characterUrls.length) {
				request(characterUrls[i], (error, response, body) => {
					if (!error && response.statusCode == 200) {
						const character = JSON.parse(body);
						console.log(character.name);

						fetchCharacter(i + 1);
					}
				});
			}
		}

		// start fetching characters
		fetchCharacter(0);
	}

});


