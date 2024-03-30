from app import app
from flask import render_template, request, redirect
import db, helpers

@app.route("/")
def index():
    thumbnails = db.select_thumbnails_new(100)
    return render_template("index.html", videos=thumbnails)

@app.route("/", methods=["POST"])
def search():
    search_term = request.form["search"]
    results = helpers.search_by_title(search_term)
    return render_template("index.html", videos=results)

@app.route("/video/<int:video_id>")
def video(video_id):
    if not db.video_exists(video_id): return "This video does not exist :/"
    video = db.select_video(video_id)
    comments = db.select_comments_new(video_id, 100)
    return render_template("video.html", video=video, comments=comments)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/create", methods=["POST"])
def create_populated():
    # todo: check if source is valid

    visual = request.form["visual"]
    audio = request.form["audio"]
    title = request.form["title"]
    desc = request.form["desc"]
    button = request.form["button"]

    visual_address = helpers.trim_link(visual)
    audio_address = helpers.trim_link(audio)
    identical = db.check_and_select_by_source(audio_address, visual_address)

    message = ""
    accept_input = True

    if identical != "-1":
        accept_input = False
        message += "Identical video already exists at [site]/video/"+identical+"\n"

    if visual_address == audio_address and visual_address != "":
        accept_input = False
        message += "Visual and audio must be from different sources >:(\n"

    if len(title) < 3 or len(title) > 100:
        accept_input = False
        message += "Title length must be 3 - 100 characters >:(\n"

    if len(desc) > 1000:
        accept_input = False
        message += "Description length must be under 1000 characters >:(\n"

    if button == "edit":
        accept_input = False

    if accept_input and button == "create":
        id = str(db.insert_video(audio_address, visual_address, title, desc, 0, "NOW()"))
        if not db.video_exists(id):
            accept_input = False
            message += "Video creation failed for some reason... OOPS xD... Try again"
        else:
            return redirect("/video/"+id)

    return render_template("create.html",
                            confirmed=accept_input,
                            message=message,
                            visual=visual,
                            visual_address=visual_address,
                            audio=audio,
                            audio_address=audio_address,
                            title=title,
                            desc=desc)