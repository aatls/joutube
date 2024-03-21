from app import app
from flask import render_template, request, redirect
import db

@app.route("/")
def index():
    thumbnails = db.select_thumbnails_new(10)
    return render_template("index.html", videos=thumbnails)

@app.route("/video/<int:video_id>")
def video(video_id):
    return str(db.video_exists(video_id))
