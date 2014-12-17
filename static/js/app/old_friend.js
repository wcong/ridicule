$(document).ready(function(){
    $('.read_open').bind('change',change_read_open);
})
function change_read_open(){
    var is_open = $(this).val();
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
