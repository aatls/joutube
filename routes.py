from app import app
from flask import render_template, request, redirect
import db

@app.route("/")
def index():
    thumbnails = db.select_thumbnails_new(100)
    return render_template("index.html", videos=thumbnails)

@app.route("/video/<int:video_id>")
def video(video_id):
    if not db.video_exists(video_id): return "This video does not exist :/"
    video = db.select_video(video_id)
    comments = db.select_comments_new(video_id, 100)
    return render_template("video.html", video=video, comments=comments)
