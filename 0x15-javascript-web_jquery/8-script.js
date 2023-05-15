const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$(document).ready(function () {
  $.getJSON(url, function (data) {
    const movies = data.results;
    const listMovies = $('#list_movies');

    $.each(movies, function (index, movie) {
      const title = movie.title;
      const listItem = $('<li>').text(title);
      listMovies.append(listItem);
    });
  });
});
