from flask import Flask
from art import text2art

from .screen import GREEN, NC
from .compare import Compare

print(GREEN + text2art("Hello, world!") + NC)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<message>")
def message(message):
    compare = Compare("Hello, world!", message)
    diff = f"{compare.diff():.1f}%"

    page = "<p>Hello, World!</p>"
    page += f"<p>Message: {message}</p>"
    page += f"<p>Diff: {diff}</p>"
    return page
