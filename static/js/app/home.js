function init(){
    $.getJSON('./',function(data){
        if(data.ridicule_list.length == 0){
            return;
        }
        for( var i=0;i< data.ridicule_list.length;i++ ){
            data.ridicule_list[i].name=data.user_map[data.ridicule_list[i].user_id]
        }
        var html = Mustache.render($('#contentTemplate').html(),data)
        $('#main-section').html(html)
    })
}