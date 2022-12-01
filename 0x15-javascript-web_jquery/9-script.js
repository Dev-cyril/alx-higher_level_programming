#!/usr/bin/node
$(document).ready(function () {
    function getData(data) {
        $('#hello').text(data.hello)
    }
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', getData)
});