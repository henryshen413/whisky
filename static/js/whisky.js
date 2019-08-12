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

$(document).ready(function () {
    function editComment(edit_cmt_txt) {
        // Insert input after span
        $('<input id="tmp_input">').insertAfter($(".comment-content-31"));
        $(".comment-content-31").hide(); // Hide span
        $(".comment-content-31").next().focus();
        $("#tmp_input").val(edit_cmt_txt);
        $("#tmp_input").blur(function() {
            // Set input value as span content
            // when focus of input is lost.
            // Also delete the input.
            var value = $(".comment-content-31").val();
            $(".comment-content-31").prev().show();
            $(".comment-content-31").prev().html(value);
            $(".comment-content-31").remove();        
        });
    }
});

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