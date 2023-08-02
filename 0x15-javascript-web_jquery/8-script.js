$(document).ready(function () {
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

    $.get(url, function(data) {
        const movies = data.results;
        
        const ulList = $('#list_movies');
        
        $.each(movies, function(index, movie) {
            const liElement = $('<li>').text(movie.title);
            ulList.append(liElement);
        });
    });
});