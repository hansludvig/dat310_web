 
 $(document).ready(function(){
  
    $(".tableClass").hide();
    $("#start").click(function(e) {
        
        $(".tableClass").show();
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
                card = $("<div></div>").addClass("card");
                back = $("<div></div>").addClass("back");
                back2 = $("<img src=\"../images/fruit_" + j + ".jpg\" alt=" + j + " />");
                back.prepend(back2);
                front = $("<div></div>").addClass("front");
                card.prepend(back).prepend(front);
                
                if (j == 7){
                    j = 0;
                }else{
                    j++;
                }
                if (col == 0) {
                    card.addClass("clearleft");
                }
                $(card).flip();
                $("#cardboard").append(card);
            }
        }
        var cardWidth = card.outerWidth(true);
        $("#cardboard").width(sizeCols * cardWidth);

    });
    var player1 = 0;
        var player2 = 0;
        var tile_id = [];
        var last_flip = 0;
        var flip_counter = 0;
    
    
   $("#cardboard").on("click", ".card", function(){
        


        var val = this;
        
        $(val).flip();
        flip_counter ++;
        var atr = $(val).children(".back").children("img").attr("alt");
        tile_id.push(atr);
        console.log(tile_id);
        console.log(atr);
        console.log(this);

        var myClass = $(this).attr("class");
        console.log(myClass);

        if (tile_id[0] == tile_id[1]){
            this.off(".flip");
            last_flip.off(".flip");
        }else if (flip_counter == 2){
            this.off(".flip");
            last_flip.off(".flip");
        }
        last_flip = this;
    });

    /*$(function(){
        $(".card").flip();
    });*/
 });
   