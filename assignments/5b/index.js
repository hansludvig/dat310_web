/**
 * Exercise #8: Card board
 */

$(document).ready(function() {

    /* assign randome possition for images */
    var arr = [0,1,2,3,4,5,6,7];
    

    /* dealing cards */
    $("#start").click(function(e) {

       // e.preventDefault();  // preventing the form from submission

        $("#cardboard").empty();

        var sizeCols = 4;
        var sizeRows = 4;

        var card;
        for (var row = 0; row < sizeRows; row++) {
            for (var col = 0; col < sizeCols; col++) {
                card = $("<div></div>").addClass("card");
                if (col == 0) {
                    card.addClass("clearleft");
                }
                $("#cardboard").append(card);
            }
        }

        var cardWidth = card.outerWidth(true);
        $("#cardboard").width(sizeCols * cardWidth);

        // alternatively, we can return false to prevent the form from submitting
        //return false;
    });

    /* clicking on a card */
    $("#cardboard").on("click", ".card", function () {
        $(this).fadeTo(1000, 0);
    });

});