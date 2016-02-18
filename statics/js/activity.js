/**
 * Created by quynv on 21/01/2016.
 */

$(document).on('click', '.delete-activity', function(){
<<<<<<< HEAD
=======
    var action = confirm('Are you sure?');
    if(action == false) return;
>>>>>>> 7eea6bfb863db11f68d57ee5c64c1fff14722986
    var id = $(this).data('id');
    var csrf = $(this).data('csrf');
    var obj = $(this).parents('.list-group-item');
    $.ajax({
<<<<<<< HEAD
        url: '/activities/delete/',
=======
        url: '/activities/',
>>>>>>> 7eea6bfb863db11f68d57ee5c64c1fff14722986
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
<<<<<<< HEAD
=======
    return 1;
>>>>>>> 7eea6bfb863db11f68d57ee5c64c1fff14722986
});