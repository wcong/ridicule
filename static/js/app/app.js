$(document).ready(function(){
    $(document).foundation();
    get_notice()
});
function get_notice(){
    $.getJSON('/reminder/',function(data){
        var all_reminder = data.friend_num + data.like_num + data.comment_num
        $('#all_reminder').html(all_reminder)
        var html = Mustache.render($('#reminderTemplate').html(),data)
        $('#reminder_list').html(html)
    })
}