function start_backgroundscroll(){
   $(window).scroll(function () {
        if ($(window).scrollTop() > 650){
            $('.second_background').css('background-position', 'center -650px');
            $('.second_background').css('background-attachment', 'fixed');

            if ($(window).scrollTop() > $('.second_background').height()-$(window).height()-$('#sponsors').height()){
                offset = $('.second_background').height()-$(window).height()-$('#sponsors').height() - 650;
            }
        } else {
            $('.second_background').css('background-position', 'center 0px');
            $('.second_background').css('background-attachment', 'scroll');
        }
    });
}

var fb_url = 'https://graph.facebook.com/469934899704539';
var tw_url = 'https://api.twitter.com/1/users/show.json?screen_name=djangocon&callback=?';
var tw_tl_url = 'https://api.twitter.com/1/statuses/user_timeline.json?screen_name=djangocon&count=20&include_rts=1&callback=?';

function set_facebook() {
    $.getJSON(fb_url, function(data){
        $('.counter.facebook').html(data.likes);
    });
}

function set_twitter() {
    $.getJSON(tw_url, function(data){
        $('.counter.twitter').html(data.followers_count);
    });

    $.getJSON(tw_tl_url, function(data){
        var i, tweet;
        for(i=0; i < 3; i++) {
            tweet = '<a target="_blank" href="https://twitter.com/djangocon/status/' +
                    data[i].id_str + '"><div class="tweet">' +
                    data[i].text + '</div></a>';
            $('.tweets').append(tweet);
        }
    });
}

$(document).ready(function(){
    start_backgroundscroll();
    set_facebook();
    set_twitter();

    $('#scrollto-sponsors').click(function(){
        $(window).stop().scrollTo($('#sponsors'), 800);
    });
    $('#scrollto-speakers').click(function(){
        $(window).stop().scrollTo($('#speakers'), 800);
    });

    $('.vote_buttons .vote').click(function(){

        var button = $(this)

        $.getJSON('/vote/add_vote/'+button.attr('data-id')+'/'+button.attr('data-kind')+'/', function(data){
            if (data.result == 'success'){
                button.parent().parent().find('.baloon_counter').html(data.score);
                button.parent().find('.vote').css('display','none');
                button.parent().html(data.message);
            } else {
                button.parent().html(data.message);
            }
        });
    });

    $('.vote_buttons .cancel').click(function(){

        var button = $(this)

        $.getJSON('/vote/cancel_vote/'+button.attr('data-id')+'/', function(data){
            if (data.result == 'success'){
                button.parent().parent().find('.baloon_counter').html('???');
                button.parent().html(data.message);
            } else {
                button.parent().html(data.message);
            }
        });

    });

    $('#sponsors a').mouseover(function(){

        var src = $(this).find('img').attr('src').replace('off.','on.');
        $(this).find('img').attr('src', src);

    }).mouseout(function(){

        var src = $(this).find('img').attr('src').replace('on.','off.');
        $(this).find('img').attr('src', src);

    });

    $('nav a.button').click(function(){
        $('nav').find('a.button').each(function(){
            $(this).removeClass('active');
        });
        $(this).addClass('active');

        $('#agenda').find('.day').each(function(){
            $(this).css('display', 'none');
        });
        $('#'+$(this).attr('data-id')).css('display', '');
    });

});

