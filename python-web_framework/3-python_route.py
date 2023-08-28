"""
a new script that starts a Flask web application
/hbnb: display “HBNB”
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def string(text):
    txt = text.replace("_", " ")
    return "C %s" % txt


@app.route("/python/(<text>)", strict_slashes=False)
def string1(text):
    if text == "":
        return "Python is cool"
    else:
        txt = text.replace("_", " ")
        return "Python %s" % txt

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
