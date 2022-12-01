#!/usr/bin/node
$(document).ready(function () {
    function events() {
        $('header').text('New Header!!!');
    }

    $('#update_header').on('click', events);
});