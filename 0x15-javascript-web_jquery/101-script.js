$(document).ready(function () {
    $('#add_item').click(function () {
        const newItem = $('<li>Item</li>');
        
        $('.my_list').append(newItem);
    });

    $('#remove_item').click(function () {
        const lastItem = $('.my_list li:last-child');
        
        lastItem.remove();
    });

    $('#clear_list').click(function () {
        $('.my_list').empty();
    });
});