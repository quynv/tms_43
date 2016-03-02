/**
 * Created by quynv on 13/01/2016.
 */

$(document).on('click','#new-report', function(){
    var user_id = $(this).data('user');
    $.ajax({
        url: '/reports/'+user_id+'/user/',
        data: $('#post_report_form').serialize(),
        method: 'post',
        dataType: 'json',
        success: function(data){
            if(data.success == 1){
                window.location.reload();
            }else{
                $.each(data.errors, function(key, error){
                    field = key;
                    $.each(error, function(key, type){
                        Notify( field.toUpperCase() + ' FIELD: ' + type, null, null, "Danger");
                    });
                });
            }
        }
    })
});


$(document).on('click', '.delete-report', function(){
    var action = confirm('Are you sure?');
    if(action == false) return;
    var id = $(this).data('id');
    var csrf = $(this).data('csrf');
    var  obj = $(this).parents('.report-content');
    $.ajax({
        url: '/reports/delete/',
        data: {id: id, csrfmiddlewaretoken: csrf},
        method: 'post',
        dataType: 'json',
        success: function(data){
            if(data.success == 1){
               Notify( data.message, null, null, "Success");
                obj.remove();
            } else {
                Notify( data.message, null, null, "Danger");
            }
        }
    })
})
