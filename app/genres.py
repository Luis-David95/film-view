from app.db import db

def count():
    sql = "SELECT COUNT(*) FROM genres"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def get_list():
    sql = "SELECT id, name FROM genres ORDER BY name"
    result = db.session.execute(sql)
    return result.fetchall()

def send(name):
    sql = "INSERT INTO genres (name) VALUES (:name)"
    db.session.execute(sql, {"name":name})
    db.session.commit()
    return True