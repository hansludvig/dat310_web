/**
 * Assignment 9
 * @author: Hans Ludvug Kleivdal
 */

$(document).ready(function() {

    $("#product_table").DataTable();

    $("#normal_price").on("input", function(e) {
        console.log($(this))
        if ($(this).length > 0){
            $("#bonus_price").attr("disabled", false);
            $("#bonus_price").attr("max", $(this).val());
        }
        else{
            $("#bonus_price").attr("disabled", true);
        }
    });

});
