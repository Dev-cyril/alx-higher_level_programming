#!/usr/bin/node
$(document).ready(function () {
    function events() {
        $('.my_list').append('<li>Item</li>');
    }
    function events1() {
        $('.my_list li:last-child').remove();
    }
    function events2() {
        $('.my_list').empty();
    }

    $('#add_item').on('click', events);
    $('#remove_item').on('click', events1);
    $('#clear_list').on('click', events2);
});