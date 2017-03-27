from flask import Flask, request, render_template
app = Flask(__name__)

HTML_FRAME_TOP = "<!DOCTYPE html>\n<html>\n<head>\n<title>Exercise #1</title>\n</head>\n<body>"
HTML_FRAME_BOTTOM = "</body>\n</html>\n"


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/sendform", methods=["POST"])
def sendform():

   return render_template("reg.html", fname=request.form["firstname"], lname=request.form["lastname"])

if __name__ == "__main__":
    app.run()