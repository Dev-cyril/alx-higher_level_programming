#!/usr/bin/node
$(document).ready(function (){
    function events() {
        $('header').toggleClass('red green');
    }

    $('#toggle_header').on('click', events);
});