$(document).ready(function() {
    // Fetch data from the API URL
    $.getJSON("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
        // Update the text of the <div> with id="hello" to display the translation of "hello"
        $('#hello').text(data.hello);
    });
});
