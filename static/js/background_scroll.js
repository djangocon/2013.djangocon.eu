function start_backgroundscroll(){
    $(window).scroll(function () {
        if ($(window).scrollTop() > 650){
            $('body').css('background-position', 'center '+($(window).scrollTop()-650).toString()+"px")

        }
    });
}

$(document).ready(function(){
    start_backgroundscroll();
});