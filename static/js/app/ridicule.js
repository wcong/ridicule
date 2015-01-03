function init(){
    $.getJSON(location.url,function(data){
        if( data.is_liked ){
            add_like();
        }else{
            remove_like();
        }
        var render_data = new Object();
        render_data.ridicule=data.ridicule.content
        render_data.id=data.ridicule.id
        render_data.creator = data.user_map[data.ridicule.user_id]
        render_data.comment_num = data.comment_list.length
        render_data.like_num = data.like_list.length
        render_data.comment_list = data.comment_list
        for(var i=0;i<render_data.comment_list.length;i++){
            render_data.comment_list[i].name = data.user_map[render_data.comment_list[i].user_id]
        }
        var html = Mustache.render($('#contentTemplate').html(),render_data)
        $('#main-section').html(html)
        $('.comment_li').css('display','none')
        $('#comment').bind('click',comment).attr('comment_list','none');
        $('#like').bind('click',like);
        $('#send_comment').bind('click',send_comment);

    })
}
function send_comment(){
    var button = $(this);
    var comment = button.parent().parent().find('#comment_content').val();
    var ridicule_id = button.attr('ridicule_id')
    $.ajax({
        url:'./comment',
        type:'post',
        data:'id=' + ridicule_id + '&comment=' + comment,
        success:function(data){
            location.reload()
        }
    })

}
function comment(){
    var comment_list_box = $(this)
    if( comment_list_box.attr('comment_list') != 'none' ){
        comment_list_box.attr('comment_list','none');
        $('.comment_li').css('display','none');
    }else{
        comment_list_box.attr('comment_list','block');
        $('.comment_li').css('display','block');
    }
}
function like(){
    var button = $(this)
    var id = button.parent().attr('ridicule_id')
    button.attr('disabled',true)
    $.ajax({
        url:'./like',
        type:'post',
        data:'id='+id,
        success:function(data){
            var msg = eval('(' + data+ ')')
            var like_num = button.find('span').text()
            like_num = parseInt(like_num)
            if(msg.now == true){
                add_like()
                button.find('span').text(like_num +1)
            }else{
                remove_like()
                button.find('span').text(like_num -1)
            }
        }
    })
}

function add_like(){
    like_button = $('#like')
    if(like_button.hasClass('success')){
        return;
    }else{
        like_button.addClass('success')
    }
}
function remove_like(){
    like_button = $('#like')
    if(like_button.hasClass('success')){
        like_button.removeClass('success')
    }else{
        return;
    }
}