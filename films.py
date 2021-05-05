from flask import abort
from db import db

def count():
    sql = "SELECT COUNT(*) FROM films WHERE visible=1"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def exists(id):
    sql = "SELECT COUNT(1) FROM films WHERE id=:id AND visible=1"
    result = db.session.execute(sql, {"id":id})
    if result.fetchone()[0] == 0:
        abort(404)

def visible(id):
    sql = "SELECT visible FROM films WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def get_visible():
    sql = "(SELECT f.id AS s_id, f.visible, f.name AS s_name, f.description, f.year, c.name, c.code, ROUND(AVG(r.grade),1) AS s_avg " \
          "FROM films AS f, countries AS c, reviews AS r " \
          "WHERE f.id=r.film_id AND c.id=f.country_id AND visible=1 " \
          "GROUP BY f.id, c.name, c.code) " \
          "UNION " \
          "(SELECT f.id, f. visible, f.name, f.description, f.year, c.name, c.code, 0.0 " \
          "FROM films AS f, countries AS c " \
          "WHERE c.id=f.country_id AND visible=1 AND NOT EXISTS (SELECT * FROM reviews AS r WHERE f.id = r.film_id)) " \
          "ORDER BY s_avg DESC"
    result = db.session.execute(sql)
    return result.fetchall()
    
def get_all():
    sql = "SELECT f.id, f.visible, f.name, f.description, f.year " \
          "FROM films AS f " \
          "ORDER BY f.name"
    result = db.session.execute(sql)
    return result.fetchall()

def get_details(id):
    sql = "SELECT f.id, f.name, f.description, f.year, c.name, l.name, g.name, d.name, s.name " \
          "FROM films AS f, countries AS c, languages AS l, genres AS g, directors AS d, screenwriters AS s " \
          "WHERE f.id=:id AND c.id=f.country_id AND l.id=f.language_id " \
          "AND g.id=f.genre_id AND d.id=f.director_id AND s.id=f.screenwriter_id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_name(id):
    sql = "SELECT name FROM films WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def send(name, description, year, country_id, language_id, genre_id, director_id, screenwriter_id):
    sql = "INSERT INTO films (visible, name, description, year, country_id, language_id, genre_id, director_id, screenwriter_id) " \
          "VALUES (:visible, :name, :description, :year, :country_id, :language_id, :genre_id, :director_id, :screenwriter_id)"
    visible = 1
    db.session.execute(sql, {"visible":visible, "name":name, "description":description, 
                             "year":year, "country_id":country_id, "language_id":language_id,
                             "genre_id":genre_id, "director_id":director_id, "screenwriter_id":screenwriter_id})
    db.session.commit()
    return True

def delete(id):
    sql = "UPDATE films SET visible=0 WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True

def restore(id):
    sql = "UPDATE films SET visible=1 WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True