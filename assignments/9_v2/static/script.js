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

    var data = {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
        {
            label: "My First dataset",
            fillColor: "rgba(220,220,220,0.2)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: [65, 59, 80, 81, 56, 55, 40]
        }
        ]
    };

    var myLineChart = new Chart(ctx).Line(data, option);


});
