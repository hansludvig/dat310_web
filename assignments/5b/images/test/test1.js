
$(document).ready(function (){

    var front = $("<div></div>").addClass("front");
    var back = $("<div></div>").addClass("back");
    $("#card").prepend(front).prepend(back);

});

$("#card").flip({
    axis: x,
    trigger: 'click'
});