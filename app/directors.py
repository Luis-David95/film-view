from app.db import db

def count():
    sql = "SELECT COUNT(*) FROM directors"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def get_list():
    sql = "SELECT id, name FROM directors ORDER BY name"
    result = db.session.execute(sql)
    return result.fetchall()

def send(name, description, country_id):
    sql = "INSERT INTO directors (name, description, country_id) " \
          "VALUES (:name, :description, :country_id)"
    db.session.execute(sql, {"name":name, "description":description,
                             "country_id":country_id})
    db.session.commit()
    return True