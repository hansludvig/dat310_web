/**
 * Exercise #8: Card board
 */

$(document).ready(function() {

    /* assign randome possition for images */
    var arr = [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7];
    var imagArr = [];
    
    for (var i = 0; i < arr.length; i++){
        var img = 'images/fruit_' + i + '.jpg';
        imagArr.push(img);
    }

    /* dealing cards */
    $("#start").click(function(e) {

       // e.preventDefault();  // preventing the form from submission

        $("#cardboard").empty();

        var sizeCols = 4;
        var sizeRows = 4;
        var j = 0;

        var front;
        var back;
        var back2;
        var card;
        for (var row = 0; row < sizeRows; row++) {
            for (var col = 0; col < sizeCols; col++) {
                card = $("<div></div>").addClass("flip");
                back = $("<div></div>").addClass("back");
                back2 = $("<img src=\"images/fruit_" + j + ".jpg\" alt=" + j + "\" />");
                back.prepend(back2);
                front = $("<div></div>").addClass("front");
                card.prepend(front).prepend(back);
                
                if (j == 7){
                    j = 0;
                }else{
                    j++;
                }
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

    /* clicking on a card 
    $("#cardboard").on("click", ".flip", function () {
        $(this).flip();
    });*/

    $(function(){
        $(".flip").flip({
            axis: 'y',
            trigger: 'click'
        });
    });

});