$(document).ready(function() {
    // Bind a click event to the <div> with id="toggle_header"
    $('#toggle_header').click(function() {
        // Check if the <header> element has class 'red'
        if ($('header').hasClass('red')) {
            // If it has class 'red', remove 'red' and add 'green'
            $('header').removeClass('red').addClass('green');
        } else {
            // If it doesn't have class 'red', remove 'green' and add 'red'
            $('header').removeClass('green').addClass('red');
        }
    });
});
