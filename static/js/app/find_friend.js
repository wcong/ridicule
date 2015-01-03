function init(){
    $.getJSON('./find',function(data){
        if( data.find_list.length ==0 ){
            return;
        }
        for(var i=0;i<data.find_list.length;i++ ){
            data.find_list[i].name = data.user_map[data.find_list[i].id]
        }
        var html = Mustache.render($('#contentTemplate').html(),data)
        $('#main-section').html(html)
        $('.add_friend').bind('click',add_friend);
    })
}
function add_friend(){
    var user_id = $(this).attr('user_id');
    $.ajax({
        url:'./find',
        type:'POST',
        data:'user_id=' + user_id,
        success:function(data){
            location.reload()
        }
    })
}
