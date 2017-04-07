"""
Assignment #8: AJAX
"""

from flask import Flask, request, g
import json

app = Flask(__name__)


class Albums():
    """Class representing a collection of albums."""

    def __init__(self, albums_file, tracks_file):
        self.__albums = []
        self.__tracks = {}
        self.__load_albums(albums_file)
        self.__load_tracks(tracks_file)

    def __load_albums(self, albums_file):
        """Loads a list of albums from a file."""
        with open(albums_file, "r") as h:
            for line in h:
                album_id, artist, album_name, album_img = line.strip().split("\t")
                self.__albums.append({
                    "id": album_id,
                    "artist": artist,
                    "album_name": album_name,
                    "img": album_img
                })
        h.close()
        #print(self.__albums)

    def __load_tracks(self, tracks_file):
        """Loads a list of tracks from a file."""
        with open(tracks_file, "r") as h:
            for line in h:
                album_id, track_name, track_time = line.strip().split("\t")

                if album_id in self.__tracks:
                    self.__tracks[album_id][track_name] = track_time
                else:
                    self.__tracks[album_id] = {track_name: track_time}
        h.close()
        #print(self.__tracks)

    def get_albums(self):
        """Returns a list of all albums, with album_id, artist and title."""
        return self.__albums

    def get_album(self, album_id):
        """Returns all details of an album."""
        track = []
        img = None

        for i in self.__albums:
            for t_id, info in self.__tracks.items():
                if i["id"] == t_id and t_id == album_id:
                    img = i["img"]

                    for a, b in info.items():
                        track.append({
                            "name": a,
                            "length": b
                        })
        return {"album_id": album_id, "img": img, "track": track}


# the Albums class is instantiated and stored in a config variable
# it's not the cleanest thing ever, but makes sure that the we load the text files only once
app.config["albums"] = Albums("data/albums.txt", "data/tracks.txt")


@app.route("/albums")
def albums():
    """Returns a list of albums (with album_id, author, and title) in JSON."""
    albums = app.config["albums"]
    # TODO complete (return albums.get_albums() in JSON format)
    return json.dumps(albums.get_albums())


@app.route("/albuminfo")
def albuminfo():
    albums = app.config["albums"]
    album_id = request.args.get("album_list", None)
    if album_id:
        # TODO complete (return albums.get_album(album_id) in JSON format)
        return json.dumps(albums.get_album(album_id))
    return ""


@app.route("/sample")
def sample():
    return app.send_static_file("index_static.html")


@app.route("/")
def index():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run()
