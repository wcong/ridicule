$(document).ready(function(){
    $('#comment').bind('click',comment);
    $('#like').bind('click',like)
})
function comment(){

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