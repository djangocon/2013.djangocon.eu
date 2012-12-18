function start_backgroundscroll(){
   $(window).scroll(function () {
        if ($(window).scrollTop() > 650){
        	$('body').css('background-position', 'center -650px');
            $('body').css('background-attachment', 'fixed');
        } else {
            $('body').css('background-position', 'center 0px');
            $('body').css('background-attachment', 'scroll');
        }
    });
}
$(document).ready(function(){
    start_backgroundscroll();
});