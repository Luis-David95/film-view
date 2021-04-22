from db import db
import users

def get_list():
    sql = "SELECT id, name, description, year FROM films"
    result = db.session.execute(sql)
    return result.fetchall()

def get_name(id):
    sql = "SELECT name FROM films WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def send(name, description, year):
    sql = "INSERT INTO films (name, description, year) VALUES (:name, :description, :year)"
    db.session.execute(sql, {"name":name, "description":description, "year":year})
    db.session.commit()
    return True