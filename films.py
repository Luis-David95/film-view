from db import db
import users

def get_list():
    sql = "SELECT f.id, f.name, f.description, f.year, c.name FROM films AS f, countries AS c WHERE c.id=f.country_id AND visible=1"
    result = db.session.execute(sql)
    return result.fetchall()

def get_details(id):
    sql = "SELECT f.id, f.name, f.description, f.year, c.name FROM films AS f, countries AS c WHERE f.id=:id AND c.id=f.country_id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_name(id):
    sql = "SELECT name FROM films WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def send(name, description, year, country_id):
    sql = "INSERT INTO films (visible, name, description, year, country_id) VALUES (:visible, :name, :description, :year, :country_id)"
    visible = 1
    db.session.execute(sql, {"visible":visible, "name":name, "description":description, "year":year, "country_id":country_id})
    db.session.commit()
    return True