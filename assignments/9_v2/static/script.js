/**
 * Assignment 9
 * @author: Hans Ludvug Kleivdal
 */

$(document).ready(function() {
    $('#userForm').validator().on('submit', function(e){
        if (e.isDefaultPrevented()){
            alert('form is not valid') // this should not happen
            console.log('form is not valid')
        }else{
            var $form = $(e.target);
            var id = $form.find('[name="id"]').val();

            console.log($form);
            console.log(id);
        }
        
    });
    $("#product_table").DataTable();
});
