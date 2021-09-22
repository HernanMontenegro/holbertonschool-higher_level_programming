fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(resp => resp.json())
  .then(data => $('DIV#character').text(data.name));
