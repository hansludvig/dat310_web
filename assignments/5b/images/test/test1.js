 
 $(document).ready(function(){
    var arr = [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7];
    var imagArr = [];
    
    for (var i = 0; i < arr.length; i++){
        var img = 'images/fruit_' + i + '.jpg';
        imagArr.push(img);
    }

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
                back = $("<div></div>").addClass("front");
                back2 = $("<img src=\"../fruit_" + j + ".jpg\" alt=" + j + "\" />");
                back.prepend(back2);
                front = $("<div></div>").addClass("back");
                card.prepend(front).prepend(back);
                
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
 });
   