$(document).ready(function() {
    // Fetch data from the API URL
    $.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
        // Loop through each movie in the fetched data
        $.each(data.results, function(index, movie) {
            // Create a new <li> element with the movie title
            var listItem = $('<li>').text(movie.title);
            // Append the new <li> element to the <ul> with id="list_movies"
            $('#list_movies').append(listItem);
        });
    });
});
