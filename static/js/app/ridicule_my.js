function init(){
    $.getJSON('./my',function(data){
        if(data.list.length == 0){
            return;
        }
        var html = Mustache.render($('#contentTemplate').html(),data)
        $('#main-section').html(html)
    })
}