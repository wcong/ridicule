$(document).ready(function(){
    $('#comment').bind('click',comment);
    $('#like').bind('click',like);
    $('#send_comment').bind('click',send_comment);
})
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
    var comment_list_box = $('#comment_list_box')
    if( comment_list_box.css('display') != 'none' ){
        comment_list_box.css('display','none');
    }else{
        comment_list_box.css('display','block')
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
                button.addClass('success')
                button.find('span').text(like_num +1)
            }else{
                button.removeClass('success')
                button.find('span').text(like_num -1)
            }
        }
    })
}