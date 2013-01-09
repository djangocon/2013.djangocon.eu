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

    $('.vote_buttons .vote').click(function(){

        var button = $(this)

        $.getJSON('/vote/add_vote/'+button.attr('data-id')+'/'+button.attr('data-kind')+'/', function(data){
            if (data.result == 'success'){
                var baloon = button.parent().parent().find('.baloon_counter');
                var score = parseInt(baloon.text())+parseInt(button.attr('data-kind'));
                baloon.html(score);
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
                var baloon = button.parent().parent().find('.baloon_counter');
                var score = parseInt(baloon.text())-parseInt(button.attr('data-kind'));
                baloon.html(score);
                button.parent().html(data.message);

            } else {
                button.parent().html(data.message);
            }
        });

    })

});

