from flask import Flask, url_for, redirect, request
app = Flask(__name__)

HTML_FRAME_TOP = "<!DOCTYPE html>\n<html>\n<head>\n<title>Exercise #1</title>\n</head>\n<body>"
HTML_FRAME_BOTTOM = "</body>\n</html>\n"


@app.route("/")
def index():
    return redirect(url_for("static", filename="form.html"))


@app.route("/sendform", methods=["POST"])
def sendform():

    html = HTML_FRAME_TOP
    html += "Name: " + request.form["firstname"] + "<br \>" + "Email: " + request.form["lastname"]
    html += HTML_FRAME_BOTTOM

    return html

if __name__ == "__main__":
    app.run()