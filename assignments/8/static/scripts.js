/**
 * Assignment 8 
 */
$(document).ready(function(){

    // load list of albums
    $.get("/albums", function (data){
        var ul = 0;
        var a = 0;
        
        //decode JSOM 
        $.each(JSON.parse(data), function(index, element) {

            // list albums
            ul = $("<li></li>").attr('id', 'list');
            a = $("<a>" + element.artist + " - " + element.album_name +"</a>").addClass(element.id).attr('id', 'link');
            ul.prepend(a);
            $("#albums_list").append(ul);
        });
        
    });

    // load clicked album
    $("#albums_list").on("click", "#list", "#link", function(){
        
        var clicked = $(this).children().attr("class");
        $("#album_cover").empty();
        $("#album_songs").empty();
        
        var table = 0; 
        var total_time_sec = 0;

        $.get("/albuminfo", {"album_id": clicked}, function(data){

            var result = JSON.parse(data);

            var image = $("#album_cover").prepend("<img src='/static/images/" + result.img + "' />");
            $("#album_info").prepend(image);

            table = $("<table></table>");
            var table_head = $("<tr><th>No.</th><th>Title</th><th>Length</th></tr>");
            $(table).append(table_head);

            $.each(result.track, function(index, element) {
                table_tr = $("<tr></tr>");
                table_td1 = $("<td>" + (index + 1) + ".</td>").addClass("song_no");
                table_td2 = $("<td>" + element.name + "</td>").addClass("song_title");
                table_td3 = $("<td>" + element.length + "</td>").addClass("song_length");
                
                // track time
                var hms = element.length;   
                var a = hms.split(':'); 
                total_time_sec += (+a[0]) * 60 + (+a[1]); // album time in sec

                $(table_tr).prepend(table_td3).prepend(table_td2).prepend(table_td1);
                $(table).append(table_tr);
            });

            var table_bottom = $("<tr><td colspan='2'><strong>Total length:</strong></td><td class='song_length'><strong>" + total_time(total_time_sec) + "</strong></td></tr>");
            $(table).append(table_bottom);

            $("#album_songs").append($(table)); // add table 
        }); 
        
    });
 
});

// convert sec to hh:mm:ss
function total_time(sec){
    var sec_num = parseInt(sec, 10);
    var hours   = Math.floor(sec_num / 3600);
    var minutes = Math.floor((sec_num - (hours * 3600)) / 60);
    var seconds = sec_num - (hours * 3600) - (minutes * 60);

    if (hours   < 10) {hours   = "0"+hours;}
    if (minutes < 10) {minutes = "0"+minutes;}
    if (seconds < 10) {seconds = "0"+seconds;}

    if (hours == "00"){
        return minutes + ":" + seconds;
    }else{
        return hours + ":" + minutes + ":" + seconds;
    } 
}
