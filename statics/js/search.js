$('#search-form').submit(function(e){
    $.post('/search/', $(this).serialize(), function(data){

        window.location.href = document.location.origin +'/search/';
        $('.tweets').html(data);
    });
    e.preventDefault();
});