$(document).ready(function() {
    // Bind a click event to the <div> with id="red_header"
    $('#red_header').click(function() {
        // Update the text color of the <header> element to red
        $('header').css('color', '#FF0000');
    });
});
