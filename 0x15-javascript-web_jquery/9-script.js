fetch('https://fourtonfish.com/hellosalut/?lang=fr')
  .then(resp => resp.json())
  .then(data => $('DIV#hello').text(data.hello));
