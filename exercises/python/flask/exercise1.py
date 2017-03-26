from flask import Flask, url_for
app = Flask(__name__)

HTML_FRAME_TOP = "<!DOCTYPE html>\n<html>\n<head>\n<title>Exercise #1</title>\n</head>\n<body>"
HTML_FRAME_BOTTOM = "</body>\n</html>\n"
postcodes = {
        "0001": "Oslo",
        "4026": "Stavanger",
        "4041": "Hafrsfjord",
        "9019": "Tromsø",
        "7491": "Trondheim"
    }

@app.route("/")
def index():
    html = HTML_FRAME_TOP
    url = url_for("postcode", code="0001")
    html += "<p>Postcode lookup service. Example usage: <a href='{url}'>{url}</a>".format(url=url)
    html += HTML_FRAME_BOTTOM
    return html


@app.route("/postcode/<code>")
def postcode(code):

    if code in postcodes:
        return "Post code {} is {}".format(code, postcodes[code])
    else:
        return "Unknown post code ({})".format(code)

if __name__ == "__main__":
    app.run()