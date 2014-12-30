$(document).ready(function(){
    $(document).foundation();
    get_notice()
});
function get_notice(){
    $.getJSON('/reminder/',function(data){
        var all_reminder = data.friend_num + data.like_num + data.comment_num
        like_list = new Array();
        for(i in data.like_map){
            like = new Object();
            like['id'] = data.ridicule_map[i].id
            like['text'] = data.ridicule_map[i].content.trim().slice(0,5)
            like['num'] = data.like_map[i]
            like_list.push(like)
        }
        comment_list = new Array();
        for( i in data.comment_map){
            comment = new Object();
            comment['id'] = data.ridicule_map[i].id
            comment['text'] = data.ridicule_map[i].content.trim().slice(0,5)
            comment['num'] = data.comment_map[i]
            comment_list.push(comment)
        }
        data['like_list'] = like_list
        data['comment_list'] = comment_list
        $('#all_reminder').html(all_reminder)
        var html = Mustache.render($('#reminderTemplate').html(),data)
        $('#reminder_list').html(html)
    })
}