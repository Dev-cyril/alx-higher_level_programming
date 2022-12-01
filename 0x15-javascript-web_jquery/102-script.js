#!/usr/bin/node
$(document).ready(function () {
    $('btn_translate').click(function (){
        function getData(data) {
            $('#hello').text(data.hello)
        }
        $.get('https://www.fourtonfish.com/hellosalut/hello/' + $('#language_code').val(), getData)
    })
});