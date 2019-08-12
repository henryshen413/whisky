$('body').popover({
    selector: '[data-popover]',
    trigger: 'focus',
    html : true, 
    delay: { "show": 100, "hide": 100 },
    content: function() {
        return $(this).next("#popover-content").html();
    }
});


// ajax token
jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

function deleteComment(delete_cmt_id) {
    $.ajax({
    url: window.location.pathname,
    type: "POST",
    data: {"delete_cmt_id": delete_cmt_id},
    success:function(response){
        location.reload();  
    },
    complete:function(){},
    error:function (xhr, textStatus, thrownError){}
	});
}

function showReplyBox(rp_id) {
    var rp = rp_id.toString();
    var rp_class = "#reply-input-" + rp;
    $(rp_class).toggleClass('show');
}

function showReplies(rp_id) {
    var rp = rp_id.toString();
    var rp_class = "#reply-" + rp;
    $(rp_class).toggleClass('show');
}

$("#comment").keypress(function (e) {
    if(e.which == 13 && !e.shiftKey) {        
        $(this).closest("form").submit();
        e.preventDefault();
    }
});