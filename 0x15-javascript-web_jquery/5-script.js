#!/usr/bin/node
$(document).ready(function () {
    function events() {
        $('.my_list').append('<li>Item</li>');
    }

    $('#add_item').on('click', events);
});