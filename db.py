from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from app import app
from os import getenv

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

def select_userid(username):
    sql = text("SELECT id FROM users WHERE LOWER(username)=LOWER(:username)")
    result = db.session.execute(sql, {"username":username})
    result = result.fetchone()
    return result[0] if result else None

def select_password_by_username(username):
    sql = text("SELECT password FROM users WHERE LOWER(username)=LOWER(:username)")
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()[0]

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
    sql = text("SELECT * FROM videos ORDER BY submissiontime DESC LIMIT :n")
    result = db.session.execute(sql, {"n":n})
    return result.fetchall()

def select_video(id):
    sql = text("SELECT v.*, u.username FROM videos v, users u WHERE v.id=:id AND v.userid=u.id")
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
    sql = text("SELECT c.*, u.username FROM comments c, users u WHERE c.videoid=:videoid AND c.userid=u.id ORDER BY c.submissiontime DESC LIMIT :n")
    result = db.session.execute(sql, {"videoid":video_id, "n":n})
    return result.fetchall()

def select_messages(n):
    sql = text("SELECT * FROM messages ORDER BY submissiontime LIMIT :n")
    result = db.session.execute(sql, {"n":n})
    return result.fetchall()

def insert_video(audio, video, title, desc, views, time, userid):
    sql = text("""  INSERT INTO videos
                    (audioaddress, videoaddress, title, description, viewcount, submissiontime, userid)
                    VALUES
                    (:audio, :video, :title, :desc, :views, :time, :userid)
                    RETURNING id""")
    result = db.session.execute(sql, {"audio":audio, "video":video, "title":title, "desc":desc, "views":views, "time":time, "userid":userid})
    db.session.commit()
    return result.fetchone()[0]

def increment_viewcount(video_id):
    sql = text("""  UPDATE videos
                    SET viewcount=viewcount+1
                    WHERE id=:videoid""")
    db.session.execute(sql, {"videoid":video_id})
    db.session.commit()

def insert_user(username, password):
    sql = text("""  INSERT INTO users (username, password)
                    VALUES (:username, :password)""")
    db.session.execute(sql, {"username":username, "password":password})
    db.session.commit()

def insert_comment(video_id, userid, content, time):
    sql = text("""  INSERT INTO comments (videoid, userid, content, submissiontime)
                    VALUES (:videoid, :userid, :content, :time) """)
    db.session.execute(sql, {"videoid":video_id, "userid":userid, "content":content, "time":time})
    db.session.commit()

def insert_message(userid, content, time):
    sql = text("""  INSERT INTO messages (userid, content, submissiontime)
                    VALUES (:userid, :content, :time) """)
    db.session.execute(sql, {"userid":userid, "content":content, "time":time})
    db.session.commit()
    