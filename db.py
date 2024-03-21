from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///aatos"
db = SQLAlchemy(app)

def video_exists(id):
    sql = text("SELECT COUNT(*) FROM videos WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def select_thumbnails_new(n):
    sql = text("SELECT id, videoaddress, title FROM videos ORDER BY submissiontime LIMIT :n")
    result = db.session.execute(sql, {"n":n})
    return result.fetchall()