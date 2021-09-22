fetch("https://swapi-api.hbtn.io/api/films/?format=json")
    .then(resp => resp.json())
    .then(function(data) {
        for (let i = 0; i < data.results.length; i++) {
            const item = data.results[i];
            $("UL#list_movies").append(`<li>${item.title}</li>`);
        }
    })
