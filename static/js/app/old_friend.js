function init(){
    $.getJSON('./old',function(data){
        if( data.friend_list.length ==0 ){
            return;
        }
        for(var i=0;i<data.friend_list.length;i++ ){
            data.friend_list[i].name = data.user_map[data.friend_list[i].related_user_id]
            now_status = data.friend_list[i].is_open
            if(now_status == 1){
                action = 'close'
                color= 'success'
            }else{
                action = 'open'
                color='alert'
            }
            data.friend_list[i].action=action
            data.friend_list[i].color=color
            data.friend_list[i].action_status = 1- now_status
        }
        var html = Mustache.render($('#contentTemplate').html(),data)
        $('#main-section').html(html)
        $('.read_open').bind('click',change_read_open);
    })
}
function change_read_open(){
    var is_open = $(this).attr('action_status');
    var id = $(this).attr('friend_id')
    $.ajax({
        url:'./old',
        type:'POST',
        data:'is_open=' + is_open+'&id=' + id,
        success:function(data){
            location.reload()
        }
    })
}
