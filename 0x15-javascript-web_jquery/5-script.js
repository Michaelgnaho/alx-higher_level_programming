$(document).ready(function() {
    // Bind a click event to the <div> with id="add_item"
    $('#add_item').click(function() {
        // Create a new <li> element with text "Item"
        var newItem = $('<li>').text('Item');
        // Append the new <li> element to the <ul> with class "my_list"
        $('ul.my_list').append(newItem);
    });
});
