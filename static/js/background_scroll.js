function start_backgroundscroll(){
    $(window).scroll(function () {
        if ($(window).scrollTop() > 57){
            $('body').css('background-position', 'center '+($(window).scrollTop()-57).toString()+"px")

        }
    });
}

$(document).ready(function(){
    start_backgroundscroll();
});