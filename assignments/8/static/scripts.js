/**
 * Assignment 8 
 */
$(document).ready(function(){
    $.get("/albums", function (data){
        var ul;
        var a;
        
        $.each(JSON.parse(data), function(index, element) {
            //console.log(element.artist);
            ul = $("<li></li>").addClass(element.id);
            a = $("<a>" + element.artist + " - " + element.album_name +"</a>").attr('id', 'list');
            ul.prepend(a);
            $("#albums_list").prepend(ul);
        });
        
    });

    $("#list").click(function(){
        console.log("kjorer click");
        var clicked = $(this).attr('class');
        console.log(clicked);
        /** 
        $.get("/albuminfo", {"album_id": clicked}, function(data){

            var result = JOSN.parse(data);
            console.log(result);

            var image = $("#album_cover").prepend("<img src='/static/images/" + result.img + "' />");
            $("#album_info").prepend(image);

            var table = $("<table></table>");
            var table_head = $("<tr><th>No.</th><th>Title</th><th>Length</th></tr>");

            var table_cels;
            $.each(result.track, function(index, element) {
                table_tr = $("<tr></tr>");
                table_td1 = $(index + ".");
                table_td2 = $(element.name);
                table_td3 = $(element.length);
                $(table_tr).prepend(table_td3).prepend(table_td2).prepend(table_td1);
                $(table_head).append(table_tr);
            });

            var table_bottom = $("<tr><td colspan='2'><strong>Total length:</strong></td><td class='song_length'><strong>54:08</strong></td></tr>");
            $(table_head).append(table_bottom);
            $("#album_songs").prepend($(table).prepend(table_head));
        }); 
        */
    });
 
});
/** Load the list of albums */
function listAlbums(){
    // TODO make an AJAX request to /albums
    // then populate the "albums_list" list with the results
}
    


/** Show details of a given album */
function showAlbum(album_id) {
    // TODO make an AJAX request to /albuminfo with the selected album_id as parameter (i.e., /albuminfo?album_id=xxx),
    // then show the album cover in the "album_cover" div and display the tracks in a table inside the "album_songs" div

}
