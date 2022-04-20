from flask import Flask

from .compare import Compare

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
