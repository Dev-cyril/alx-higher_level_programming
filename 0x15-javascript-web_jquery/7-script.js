#!/usr/bin/node
$(document).ready(function () {
    function getData(data){
        $('#character').text(data.name);
    }
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', getData)
});