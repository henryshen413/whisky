// extend jQuery to check if the selector returns nothing
$.fn.exists = function () {
    return this.length !== 0;
}

// Hide Header on on scroll down
var didScroll;
var lastScrollTop = 0;

$(window).scroll(function(event){
    didScroll = true;
});

setInterval(function() {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 250);

function hasScrolled() {
    var delta = 3;
    var navbarHeight = 135;
    var st = $(this).scrollTop();
    
    // Make sure they scroll more than delta
    if(Math.abs(lastScrollTop - st) <= delta)
        return;
    
    // If they scrolled down and are past the navbar, add class .nav-up.
    // This is necessary so you never see what is "behind" the navbar.
    if (window.innerWidth >= 768){
        if (st > lastScrollTop && st > navbarHeight){
            // Scroll Down
            $('.navbar').css('top', '-80px');
            $('.notifications').css('top', '70px');
        } else {
            // Scroll Up
            if(st + $(window).height() < $(document).height()) {
                $('.navbar').css('top', '0px');
                $('.notifications').css('top', '150px');
            }
        }
    }
    
    lastScrollTop = st;
}

function testAnim(x) {
    $('.nav-block').children().removeClass().addClass(x + ' animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
      $(this).removeClass();
    });
  };

$('.pagination li a.active').each(function(){
    $(this).css('background', '#337AB7');
    $(this).css('color', '#fff');
});

if($('.pagination li:first').find('a span').text() == '<<')
    $('.pagination li:first').find('a span').text('First');

if($('.pagination li:nth-child(2)').find('a span').text() == '<')
    $('.pagination li:nth-child(2)').find('a span').text('Prev');

if($('.pagination li:last').find('a span').text() == '>>')
    $('.pagination li:last').find('a span').text('Last');

if($('.pagination li:nth-last-child(2)').find('a span').text() == '>')
    $('.pagination li:nth-last-child(2)').find('a span').text('Next');

//window.setTimeout(function() {
//    $(".alert-message").fadeTo(500, 0).slideUp(500, function(){
//        $(this).remove();
//    });
//}, 5000);

$(document).ready(function(){
    if($(window).scrollTop() > 150){
        $('#gotop').fadeIn();
    }
    $('.owl-carousel').owlCarousel({
        autoplay:true,
        autoplayTimeout:3000,
        autoplayHoverPause:true,
        loop:true,
        margin:10,
        nav:true,
        items: 1,
        navText : ['<i class="fa fa-angle-left" aria-hidden="true"></i>','<i class="fa fa-angle-right" aria-hidden="true"></i>']
    })// end carousel

    $('.tabs').tabslet();
    $('.tabs').on("_before", function(e) {
        e.preventDefault();
        testAnim("fadeInLeft")
    });

    $('#myModal').modal('hide');
    $('#myModal').on('hidden', function(){
        $('#myModal1').modal('show');
    });

    setTimeout(function(){
        $('.notifications').fadeOut(2000, function(){});
    }, 3000);

    $('.navbar-toggler').on('click', function(){
        $('.animated-icon').toggleClass('open');
    });

    // click user menu btn to float in the menu
    $('.user-menu-btn').on('click', function(){
        $('.user-mobile-menu').toggleClass('open');
    });

    // click  outside user menu to float out user menu
    $('.user-page-info, footer').on('click', function(){
        if($('.user-mobile-menu').width())
            $('.user-mobile-menu').removeClass('open');
    });

    // load more tiles
    $('.more-btn').click(function(){
        var more_btn = $(this);
        more_btn.addClass('disabled');
        var letters = /^[A-Za-z\-\_]+$/;
        var tile_length = 0;
        var target = $(this).attr('data-target');
        if(target.match(letters)){
            tile_length = $("."+target+" .tile").length;
            target_div = $("div."+target);
        }  
        else{
            tile_length = $(".tile").length;
            target_div = $("div.tiles")
        }
            
        $.ajax({
            method: "GET",
            url: "/api/post/more/",
            data: {target: target, num: tile_length},
            dataType: "json",
            success: function(result){
                var result_length = (result.length <=9)? result.length:9
                for(var i = 0; i < result_length; i++){
                    target_div.append(
                        $('<div/>', {'class': 'tile'}).append(
                            $('<a/>', {'href': '/blog/'+result[i]['slug']}).append(
                                $('<div/>', {'class': 'tile-img', 'style': 'background-image: url("'+result[i]['featured_image']+'")'})
                            )
                            .append($('<h4/>', {'class': 'tile-title', text: result[i]['title']}))
                            .append($('<p/>', {'class': 'tile-desc', text: result[i]['content']}))
                            .append(
                                $('<div/>', {'class': 'tile-detail'}).append(
                                    $('<span/>', {text: result[i]['username']})
                                )
                                .append(
                                    $('<span/>', {'class': 'tile-date', text: result[i]['date']})
                                )
                            )
                        ).hide().fadeIn()
                    );
                }
                more_btn.removeClass('disabled');
                if(result.length != 10)
                    more_btn.fadeOut();
            },
            error: function(xhr, ajaxOptions, thrownError){ 
                console.log(xhr.status); 
                console.log(thrownError);
            }
        });
    });

    $('.author-tile-wrap').mouseenter(function(){
        if(window.innerWidth >= 768)
            $(this).find('.author-articles').delay(300).fadeIn();
    }).mouseleave(function(){
        $(this).find('.author-articles').clearQueue().css('display', 'none');
    });
});

$(function(){
    $('#gotop_btn').click(function(){
        jQuery('html,body').animate({
            scrollTop:0
        },600);
    });
    $(window).scroll(function() {
        if( $(this).scrollTop() > 150){
          $('#gotop').fadeIn();
        }
        else{
          $('#gotop').fadeOut();
        }
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function editFollow(el, author) {
    var csrftoken = getCookie('csrftoken');
    console.log(window.location.href)
    $.ajax({
    headers: { "X-CSRFToken": csrftoken },
    url: window.location.href,
    type: "POST",
    data: {"follow": "follow", "author": author},
    success:function(response){
        if (response==2){
            var ori_count = parseInt($(".follower").text().split(" ")[0])
            add_one = ori_count + 1 
            
            $(el).text("UnFollow") 
            $(".follower").text(add_one + " Follower") 
        }
        
        else if (response==3){
            var ori_count = parseInt($(".follower").text().split(" ")[0])
            minus_one = ori_count - 1 

            $(el).text("Follow") 
            $(".follower").text(minus_one + " Follower") 
        }
    },
    complete:function(){},
    error:function (xhr, textStatus, thrownError){}
	});
}

function notify(type, msg){
    element = $('.notifications .alert').first();
    if(!element.exists()){
        $('.notifications').html('<div class="alert alert-dismissible role="alert"><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
        element = $('.notifications .alert').first();
    }
    switch(type){
        case 'success':
            element.removeClass('alert-error').addClass('alert-success');
            break;
        case 'error':
        default:
            element.removeClass('alert-success').addClass('alert-error');
            break;
    }
    element.text(msg);
    $('.notifications').fadeIn();
    setTimeout(function(){
        $('.notifications').fadeOut(2000, function(){});
    }, 3000);
}
