/**
 * Created by quynv on 21/01/2016.
 */

$(document).on('click', '.delete-activity', function(){
    var id = $(this).data('id');
    var csrf = $(this).data('csrf');
    var obj = $(this).parents('.list-group-item');
    $.ajax({
        url: '/activities/delete/',
        data: {id: id, csrfmiddlewaretoken: csrf},
        dataType: 'json',
        method: 'post',
        success: function(data){
            if(data.success == 1){
                Notify( data.message, null, null, "Success");
                obj.remove();
            } else {
                Notify( data.message, null, null, "Danger");
            }
        }
    });
});