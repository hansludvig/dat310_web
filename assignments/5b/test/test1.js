 
 $(document).ready(function(){
  
    var timer_started = 0;
    var time_elapsed = 0;
    var memory_values = [];
    var memory_tile_ids = [];
    var tiles_filpped = 0;
    var tiles_flipped_total = 0;
    var p1 = true;
    var c1 = 0;
    var c2 = 0;
    var last_flip;
    var tile_img = [];

    for (var x = 0; x < 8; x++){
        tile_img.push(x);
        tile_img.push(x);
    }

    console.log(tile_img);

    function shuffle(a) {
        var j, x, i;
        for (i = a.length; i; i--) {
            j = Math.floor(Math.random() * i);
            x = a[i - 1];
            a[i - 1] = a[j];
            a[j] = x;
        }
    }

    $(".tableC").hide(); //shows stats for the game

    // Starts the game. Delete all elements from #cardboard and adds new ones
    $("#start").click(function(e) {

        timer_started = 0;
        time_elapsed = 0;
        memory_values = [];
        memory_tile_ids = [];
        tiles_filpped = 0;
        tiles_flipped_total = 0;
        p1 = true;
        c1 = 0;
        c2 = 0;
        last_flip = null;

        shuffle(tile_img);

        console.log(tile_img);

        $(".tableC").show();
        $("#cardboard").empty();
        //$("#runner").runner();
       
        var sizeCols = 4;
        var sizeRows = 4;
        var j = 0;
        var i = 0;

        var front, back, back2, card;
        
        for (var row = 0; row < sizeRows; row++) {
            for (var col = 0; col < sizeCols; col++) {
                card = $("<div id=" + i + "></div>").addClass("card").addClass("notMatch");
                back = $("<div></div>").addClass("back");
                back2 = $("<img src=\"../images/fruit_" + tile_img[i] + ".jpg\" alt=" + tile_img[i] + " />");
                back.prepend(back2);
                front = $("<div></div>").addClass("front");
                card.prepend(back).prepend(front);
                
                if (j == 7){
                    j = 0;
                }else{
                    j++;
                }
                i++;
                if (col == 0) {
                    card.addClass("clearleft");
                }
                $(card).flip({trigger: 'manual'});
                $("#cardboard").append(card);
            }
        }
        var cardWidth = card.outerWidth(true);
        $("#cardboard").width(sizeCols * cardWidth);
        $(".tableboard").width(sizeCols * cardWidth);
        $(".tableC").width((sizeCols * cardWidth) - 20);
        $(".winnerboard").width(sizeCols * cardWidth);
        $(".stats").width(((sizeCols * cardWidth) - 40 ) / 2);
        $("#c_total").html(tiles_flipped_total);
        $("#runner").runner("stop");
        $("#runner").runner({
            format: function (value) {
                time_elapsed = parseFloat(Math.round(value) / 1000).toFixed(2);
                return time_elapsed;
            }
        });

        $("#c_one").html(c1);
        $("#c_two").html(c2);
        
    });
    
    

   $("#cardboard").on("click", ".notMatch", ".card", function(){

        var tile = this;
        console.log(this);
        
        console.log(tiles_flipped_total);
        console.log($(tile).attr("id"));
        console.log($(tile).data("flip-model").isFlipped);

        if (!timer_started) {
            timer_started = 1;
            $('#runner').runner('start');
        }

        if ((memory_values.length < 2)){

            if (memory_values.length === 0){
                $(tile).flip(true); // Flip tile, imgae shows
                memory_values.push($(tile).children(".back").children("img").attr("alt"));
                memory_tile_ids.push(tile);
                tiles_flipped_total++;
                $("#c_total").html(tiles_flipped_total);

            } else if ((memory_values.length === 1) && ($(tile).data("flip-model").isFlipped === false)){ // If the tile is already fliped then nothing should happen

                $(tile).flip(true); // Flip tile, imgae shows
                memory_values.push($(tile).children(".back").children("img").attr("alt"));
                memory_tile_ids.push(tile);
                tiles_flipped_total++;
                $("#c_total").html(tiles_flipped_total);

                if ((memory_values[0] === memory_values[1]) && (memory_tile_ids[0] !== memory_tile_ids[1])){
                    $(tile).off(".flip"); // Remove flip from matching tiles
                    $(last_flip).off(".flip");
                    $(tile).removeClass("notMatch"); // Remove flip from matching tiles
                    $(last_flip).removeClass("notMatch");
                    
                    if (p1 === true){
                        c1++;
                        $("#c_one").html(c1);
                    }else{
                        c2++;
                        $("#c_two").html(c2);
                    }

                    tiles_filpped += 2;
                    memory_values = [];
                    memory_tile_ids = [];
                    last_flip = null;

                    if (tiles_filpped === 16){
                        $("#runner").runner("stop");
                        if (c1 > c2){
                            $(".winner").html("Player 1 won");
                        }else{
                            $(".winner").html("Player 2 won");
                        }
                        
                    }
                } else {
                    
                    function flipBack(){
                        var back1 = memory_tile_ids[0];
                        var back2 = memory_tile_ids[1];
                        $(back1).flip(false);
                        $(back2).flip(false);
                        
                        if (p1 === true){
                            p1 = false;
                        }else{
                            p1 = true;
                        }

                        memory_values = [];
                        memory_tile_ids = [];
                    }
                    setTimeout(flipBack, 700);
                }
            }
            
        }
        
        last_flip = this; // Previus flip        
    });
 });
   