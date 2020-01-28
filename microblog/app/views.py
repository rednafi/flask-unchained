from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Redowan"}
    posts = [
        {"author": {"username": "Xfiles"}, "body": "I want to believe!"},
        {"author": {"username": "Maverick"}, "body": "One of life's mystery sir!"},
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
