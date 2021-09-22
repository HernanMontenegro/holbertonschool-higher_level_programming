document.addEventListener('DOMContentLoaded', function (event) {
  $('INPUT#btn_translate').click(function () {
    const inputLang = $('INPUT#language_code').val();
    fetch(`https://fourtonfish.com/hellosalut/?lang=${inputLang}`)
      .then(resp => resp.json())
      .then(data => $('DIV#hello').text(data.hello));
  });
  $('INPUT#btn_translate').keypress(function (e) {
    if (e.keyCode === 13) {
      $('INPUT#btn_translate').click();
    }
  });
  $('INPUT#language_code').keypress(function (e) {
    if (e.keyCode === 13) {
      $('INPUT#btn_translate').click();
    }
  });
});
