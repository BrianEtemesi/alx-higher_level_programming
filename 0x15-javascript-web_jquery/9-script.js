const $ = window.$;
let response = null;
$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    async: false,
    success: function (data) {
      response = data.hello;
    },
    error: () => {
      response = 'Error';
    }
  });
  if (response) {
    $('#hello').text(response);
  }
});
