function init(){
    $.getJSON('./',function(data){
        var html = Mustache.render($('#contentTemplate').html(),data.user)
        $('#main-section').html(html)
        if( data.user.is_nickname ==1 ){
            $('#is_nickname').attr('action',0).text('close nickname')
        }else{
            $('#is_nickname').attr('action',1).text('use nickname')
        }
        $('#is_nickname').bind('click',nickname);
    })
}
function nickname(){
    var nickname = $('#nickname').val().trim()
    var is_nickname = $(this).attr('action')
    if( is_nickname == 1 && nickname.length== 0){
        $('#main-alert-text').text('must pick a nick name')
        $('#main-alert').css('display','block');
        return
    }
    $.ajax({
        url:'./',
        type:'post',
        data:'nickname='+nickname+'&is_nickname=' + is_nickname,
        success:function(data){
            location.reload()
        }
    })
}