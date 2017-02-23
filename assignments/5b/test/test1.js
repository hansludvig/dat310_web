 
 $(document).ready(function(){
  

    $("#start").click(function(e) {


        var sizeCols = 4;
        var sizeRows = 4;
        var j = 0;

        var front;
        var back;
        var back2;
        var card;
        for (var row = 0; row < sizeRows; row++) {
            for (var col = 0; col < sizeCols; col++) {
                card = $("<div></div>").addClass("card");
                back = $("<div></div>").addClass("back");
                back2 = $("<img src=\"../images/fruit_" + j + ".jpg\" alt=" + j + "\" />");
                back.prepend(back2);
                front = $("<div></div>").addClass("front");
                card.prepend(back).prepend(front);
                
                if (j == 7){
                    j = 0;
                }else{
                    j++;
                }
                
                $("body").append(card);
            }
        }
      

    });
 
   $("#cardboard").on("click", ".card", function(){
        $(this).flip();
    });

    /*$(function(){
        $(".card").flip();
    });*/
 });
   