$(document).ready(function() {
    // Function to make a call to HelloSalut API and display the translation
    function sayHello(languageCode) {
        // Make a call to HelloSalut API with the provided language code
        $.ajax({
            url: "https://hellosalut.stefanbohacek.dev/",
            data: { lang: languageCode },
            success: function(response) {
                // Display the translation for "Hello" in the HTML tag DIV#hello
                $('#hello').text(response);
            },
            error: function(xhr, status, error) {
                // Handle error if translation cannot be fetched
                $('#hello').text("Translation not available");
            }
        });
    }

    // Call sayHello function when the button is clicked
    $('#btn_say_hello').click(function() {
        // Get the language code provided by the user
        var languageCode = $('#language_code').val();

        // Call sayHello function with the provided language code
        sayHello(languageCode);
    });
});
