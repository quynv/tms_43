/**
 * Created by quynv on 18/02/2016.
 */
$(document).on('click', '.delete-course', function(){
    var action = confirm('Are you sure?');
    if(action == false) return;
    var id = $(this).data('id');
    var csrf = $(this).data('csrf');
    var  obj = $(this).parents('tr');
    $.ajax({
        url: '/admin/courses/delete/',
        data: {id: id, csrfmiddlewaretoken: csrf},
        method: 'post',
        dataType: 'json',
        success: function(data){
            if(data.success == 1){
                alert(data.message);
                obj.remove();
            } else {
                alert(data.message);
            }
        }
    })
});

$(document).on('click', '.delete-subject', function(){
    var action = confirm('Are you sure?');
    if(action == false) return;
    var id = $(this).data('id');
    var csrf = $(this).data('csrf');
    var  obj = $(this).parents('tr');
    $.ajax({
        url: '/admin/subjects/delete/',
        data: {id: id, csrfmiddlewaretoken: csrf},
        method: 'post',
        dataType: 'json',
        success: function(data){
            if(data.success == 1){
                alert(data.message);
                obj.remove();
            } else {
                alert(data.message);
            }
        }
    })
});

$(document).on('click', '.delete-user', function(){
    var action = confirm('Are you sure?');
    if(action == false) return;
    var id = $(this).data('id');
    var csrf = $(this).data('csrf');
    var  obj = $(this).parents('tr');
    $.ajax({
        url: '/admin/users/delete/',
        data: {id: id, csrfmiddlewaretoken: csrf},
        method: 'post',
        dataType: 'json',
        success: function(data){
            if(data.success == 1){
                alert(data.message);
                obj.remove();
            } else {
                alert(data.message);
            }
        }
    })
});