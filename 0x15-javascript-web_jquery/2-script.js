#!/usr/bin/node
$(document).ready(function () {
    function events(){
        $('header').css('color', '#FF0000')
    }

    $('#red_header').on('click', events)
})