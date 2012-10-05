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
    set_facebook();
    set_twitter();
});
