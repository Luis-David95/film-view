from db import db
import users

def get_list():
    sql = "SELECT id, name, description FROM films"
    result = db.session.execute(sql)
    return result.fetchall()

def get_name(id):
    sql = "SELECT name FROM films WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def send(name, description):
    sql = "INSERT INTO films (name, description) VALUES (:name, :description)"
    db.session.execute(sql, {"name":name, "description":description})
    db.session.commit()
    return True