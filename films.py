from db import db

def exists(id):
    sql = "SELECT COUNT(1) FROM films WHERE id=:id AND visible=1"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def get_list():
    sql = "SELECT f.id, f.visible, f.name, f.description, f.year, c.name " \
          "FROM films AS f, countries AS c " \
          "WHERE c.id=f.country_id " \
          "ORDER BY f.name"
    result = db.session.execute(sql)
    return result.fetchall()

def get_details(id):
    sql = "SELECT f.id, f.name, f.description, f.year, c.name, l.name, g.name " \
          "FROM films AS f, countries AS c, languages AS l, genres AS g " \
          "WHERE f.id=:id AND c.id=f.country_id AND l.id=f.language_id AND g.id=f.genre_id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchall()

def get_name(id):
    sql = "SELECT name FROM films WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def send(name, description, year, country_id, language_id, genre_id):
    sql = "INSERT INTO films (visible, name, description, year, country_id, language_id, genre_id) " \
          "VALUES (:visible, :name, :description, :year, :country_id, :language_id, :genre_id)"
    visible = 1
    db.session.execute(sql, {"visible":visible, "name":name, "description":description, 
                             "year":year, "country_id":country_id, "language_id":language_id, "genre_id":genre_id})
    db.session.commit()
    return True

def delete(id):
    sql = "UPDATE films SET visible=0 WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True