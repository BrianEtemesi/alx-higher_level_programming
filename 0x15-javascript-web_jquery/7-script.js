const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$(document).ready(function () {
  $.getJSON(url, function (data) {
    const characterName = data.name;
    $('#character').text(characterName);
  });
});
