$(document).ready(function(){
    $('.add_friend').bind('click',add_friend);
})
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
