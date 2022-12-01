#!/usr/bin/node
$(document).ready(function () {
    function events() {
        $('header').addClass('red')
    }

    $('#red_header').on('click', events)
})