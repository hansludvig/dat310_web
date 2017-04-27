/**
 * Assignment 9
 * @author: Hans Ludvug Kleivdal
 */

$(document).ready(function() {
    $('#userForm').formValidation({
            framework: 'bootstrap',
            icon: {
                valid: 'glyphicon glyphicon-ok',
                invalid: 'glyphicon glyphicon-remove',
                validating: 'glyphicon glyphicon-refresh'
            },
            fields: {
                name: {
                    validators: {
                        notEmpty: {
                            message: 'The product needs a name'
                        }
                    }
                },
                /**description: {
                    validators: {
                        notEmpty: {
                            message: 'Description is required'
                        }
                    }
                },*/
                normal_price: {
                    validators: {
                        notEmpty: {
                            message: 'The produt needs a price'
                        },
                        numeric: {
                            message: 'Input must be a number'
                        }
                    }
                },
                bonus_price: {
                    validators: {
                        numeric: {
                            message: 'Input must be a number'
                        }
                    }
                }
            }
        }).on('succses.form.fv', function(e){
            e.preventDefault() // no more inputs to the form

            var $form = $(e.target);
            var id = $form.find('[name="id"]').val();

            console.log($form);
            console.log(id);
        });

        $('.editButton').on('click', function() {
        // Get the record's ID via attribute
        var id = $(this).attr('data-id');

            $.get("/productinfo", {"product_id": id}, function(response){
                var res = JSON.parse(response);

                $('#userForm')
                    .find('[name="id"]').val(response.id).end()
                    .find('[name="name"]').val(response.name).end()
                    //.find('[name="description"]').val(response.email).end()
                    .find('[name="normal_price"]').val(response.normal_price).end()
                    .find('[name="bonus_price"]').val(response.bonus_price).end();
            
                // Show the dialog
                bootbox
                    .dialog({
                        title: 'Edit the user profile',
                        message: $('#userForm'),
                        show: false // We will show it manually later
                    })
                    .on('shown.bs.modal', function() {
                        $('#userForm')
                            .show()                             // Show the login form
                            .formValidation('resetForm'); // Reset form
                    })
                    .on('hide.bs.modal', function(e) {
                        // Bootbox will remove the modal (including the body which contains the login form)
                        // after hiding the modal
                        // Therefor, we need to backup the form
                        $('#userForm').hide().appendTo('body');
                    })
                    .modal('show');
            });
        });
    });
