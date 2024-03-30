from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///aatos"
db = SQLAlchemy(app)

def video_exists(id):
    sql = text("SELECT COUNT(*) FROM videos WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def check_and_select_by_source(audio, video):
    sql = text("SELECT COUNT(*) FROM videos WHERE audioaddress=:audio AND videoaddress=:video LIMIT 1")
    result = db.session.execute(sql, {"audio":audio, "video":video})
    if result.fetchone()[0] == "1":
        sql = text("SELECT id FROM videos WHERE audioaddress=:audio AND videoaddress=:video LIMIT 1")
        result = db.session.execute(sql, {"audio":audio, "video":video})
        return result.fetchone()[0]
    else:
        return "-1"

def select_thumbnails_new(n):
    sql = text("SELECT id, videoaddress, title FROM videos ORDER BY submissiontime LIMIT :n")
    result = db.session.execute(sql, {"n":n})
    return result.fetchall()

def select_video(id):
    sql = text("SELECT * FROM videos WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def select_videos_by_keywords(keywords):
    conditions = ""
    for word in keywords:
        conditions += "LOWER(title) LIKE '%"+word+"%' OR "
    conditions = conditions[:-4]
    sql = text("SELECT * FROM videos WHERE "+conditions)
    result = db.session.execute(sql)
    return result.fetchall()

def select_comments_new(video_id, n):
    sql = text("SELECT * FROM comments WHERE videoid=:videoid ORDER BY submissiontime LIMIT :n")
    result = db.session.execute(sql, {"videoid":video_id, "n":n})
    return result.fetchall()

def select_messages(n):
    sql = text("SELECT content FROM messages ORDER BY submissiontime LIMIT :n")
    result = db.session.execute(sql, {"n":n})
    return result.fetchall()

def insert_video(audio, video, title, desc, views, time):
    sql = text("""  INSERT INTO videos
                    (audioaddress, videoaddress, title, description, viewcount, submissiontime)
                    VALUES
                    (:audio, :video, :title, :desc, :views, :time)
                    RETURNING id""")
    result = db.session.execute(sql, {"audio":audio, "video":video, "title":title, "desc":desc, "views":views, "time":time})
    db.session.commit()
    return result.fetchone()[0]

def insert_comment(video_id, content, time):
    sql = text("""  INSERT INTO comments (videoid, content, submisiontime)
                    VALUES (:videoid, :content, :time) """)
    db.session.execute(sql, {"videoid":video_id, "content":content, "time":time})
    db.session.commit()

def insert_message(content, time):
    sql = text("""  INSERT INTO messages (content, submissiontime)
                    VALUES (:content, :time) """)
    db.session.execute(sql, {"content":content, "time":time})
    db.session.commit()
    