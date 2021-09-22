document.addEventListener("DOMContentLoaded", function(event) {
    $("INPUT#btn_translate").click(function() {
        let inputLang = $("INPUT#language_code").val();
        fetch(`https://fourtonfish.com/hellosalut/?lang=${inputLang}`)
            .then(resp => resp.json())
            .then(data => $("DIV#hello").text(data.hello));
    });
 });
