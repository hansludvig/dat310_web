
"""
A minimal web application in flask
@author: Krisztian Balog
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/info")
def info():
    return "Hello, info site!"

if __name__ == "__main__":
    app.run()