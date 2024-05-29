$(document).ready(function() {
    // Fetch data from the API URL
    $.getJSON("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data) {
        // Extract the character name from the fetched data
        var characterName = data.name;
        // Update the text of the <div> with id="character" to display the character name
        $('#character').text(characterName);
    });
});
