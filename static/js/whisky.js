$('body').popover({
    selector: '[data-popover]',
    trigger: 'focus',
    html : true, 
    delay: { "show": 100, "hide": 100 },
    content: function() {
        return $(this).next("#popover-content").html();
    }
});

$(document).ready(function() {
    $('#show-edit-flavor').click(function() {
        $('.edit-flavor-div').slideToggle("fast", function() {
            if ($(this).is(":visible")) {
                $('#show-edit-flavor').text('Close');                
            } else {
                $('#show-edit-flavor').text('Edit your Flavor');                
            }        
        });
    });

    $('[data-toggle="popover"]').popover({
        html : true, 
        container : '#btn-share',
        content: function() {
          return $('#popoverExampleHiddenContent').html();
        }
    });

    $(document).click(function (event) {
        // hide share button popover
        if (!$(event.target).closest('#btn-share').length) {
            $('#btn-share').popover('hide')
        }
    });

    $("a.twitter").attr("href", "https://twitter.com/intent/tweet?text=" + window.location.href);
    $("a.facebook").attr("href", "https://www.facebook.com/sharer/sharer.php?u=" + window.location.href);
});

//slider
$(function() {
    $( "#flavor-bar-controller > .flavor-ctrl" ).each(function() {
        // read initial values from markup and remove that
        var value = parseInt($( this ).text(), 10);
        var ctrl_id = parseInt($(this).attr('id'), 10);

        $( this ).empty().slider({
            value: value,
            range: "min",
            min: 0,
            max: 10,
            orientation: "horizontal",
            slide: function( event, ui ) {
                var csrftoken = getCookie('csrftoken');
                $.ajax({
                headers: { "X-CSRFToken": csrftoken },
                url: window.location.href,
                type: "POST",
                data: {"flavor_edit": "flavor_edit", "ctrl_id": ctrl_id, "value": ui.value},
                success: function(response){
                        config_individual.data.datasets[0].data[ctrl_id] = ui.value;
                        config.data.datasets[0].data[ctrl_id] = response;
                        // redraw chart
                        myRadar.update();
                        generalRadar.update();
                },
                complete:function(){},
                error:function (xhr, textStatus, thrownError){}
                });
            }
        });
    });
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

function wishlistEditor(el, action){
    var csrftoken = getCookie('csrftoken');

    $.ajax({
        headers: { "X-CSRFToken": csrftoken },
        url: window.location.pathname,
        type: "POST",
        data: {"action": action},
        success:function(response){
            if(response){
                if(action == "bookmark"){
                    if(response == 1){
                        $(el).children('i').attr("class",'fas fa-bookmark');
                    }
                    else {
                        $(el).children('i').attr("class",'far fa-bookmark');
                    }
                }
            }
        },
        error:function (xhr, textStatus, thrownError){}
	});
}

function editComment(edit_cmt_id) {
    var c_id = edit_cmt_id.toString();
    var old_comment = "#cm-user-content-"+c_id;
    var edit_box = "#edit-box-"+c_id;
    var rating_edit = "#rating-edit-"+c_id
    
    $(old_comment).hide();
    $(edit_box).show();
    $(rating_edit).after("<input type=\"hidden\" id=\"myRating-edit\" name=\"myRating-edit\" value=\"\" />");
}

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

function cancelEdit(edit_cmt_id, rating_score) {
    var c_id = edit_cmt_id.toString();
    var old_comment = "#cm-user-content-"+c_id;
    var edit_box = "#edit-box-"+c_id;
    var rating_edit = "#rating-edit-"+c_id
    
    $("#myRating-edit").remove();
    $(rating_edit).starRating('setRating', rating_score)
    $(edit_box).hide();
    $(old_comment).show();
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