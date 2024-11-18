const response = fetch('https://swapi-api.hbtn.io/api/films/?format=json').then((response) =>
    response.json().then((data) => populateMovies(data['results']))
);

function populateMovies(obj) {
    const movie_list = document.querySelector('#list_movies');
    for (const movie of obj) {
        const movie_item = document.createElement('li');
        movie_item.id = 'list_movies';
        movie_item.textContent = movie.title;
        movie_list.appendChild(movie_item);
    }
}
