$(document).ready(function(){
    $(".button-on").click(function() {
        $.ajax({
            url: 'http://192.168.1.38:3000/assistant',
            type: 'POST',
            data: {"user": "alexandre", "command":"allume "+$(this).attr('google')},
        });
    });
    
    $('.button-off').on('click', function() {
        $.ajax({
            url: 'http://192.168.1.38:3000/assistant',
            type: 'POST',
            data: {"user": "alexandre", "command":"éteint "+$(this).attr('google')},
        });
    });
});
