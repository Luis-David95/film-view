from app.db import db
from app import users

def count():
    sql = "SELECT COUNT(*) " \
          "FROM reviews AS r, films AS f, users AS u " \
          "WHERE f.id=r.film_id AND u.id=r.user_id AND f.visible=1 AND u.banned=0"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def get_list(film_id):
    sql = "SELECT u.username, r.content, r.grade, TO_CHAR(r.submitted, 'DD Month YYYY - HH24:MI'), c.name, c.code " \
          "FROM reviews AS r, users AS u, countries AS c " \
          "WHERE r.film_id=:film_id AND u.id=r.user_id AND c.id=u.country_id AND u.banned=0"
    result = db.session.execute(sql, {"film_id":film_id})
    return result.fetchall()

def get_grade_details(film_id):
    sql = "SELECT ROUND(AVG(r.grade),1), COUNT(DISTINCT r.id) " \
          "FROM reviews AS r, films AS f, users AS u " \
          "WHERE r.film_id=:film_id AND r.user_id=u.id AND u.banned=0"
    result = db.session.execute(sql, {"film_id":film_id})
    return result.fetchall()

def get_highest_rated():
    sql = "SELECT f.name, AVG(r.grade) AS average " \
          "FROM films AS f, reviews AS r, users AS u " \
          "WHERE f.id=r.film_id AND visible=1 AND r.user_id=u.id AND u.banned=0 " \
          "GROUP BY f.id " \
          "ORDER BY average DESC"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def get_lowest_rated():
    sql = "SELECT f.name, AVG(r.grade) AS average " \
          "FROM films AS f, reviews AS r, users AS u " \
          "WHERE f.id=r.film_id AND visible=1 AND r.user_id=u.id AND u.banned=0 " \
          "GROUP BY f.id " \
          "ORDER BY average ASC"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def get_average_grade():
    sql = "SELECT ROUND(AVG(r.grade),1) " \
          "FROM films AS f, reviews AS r, users AS u " \
          "WHERE f.id=r.film_id AND visible=1 AND r.user_id=u.id AND u.banned=0"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def get_most_active_user():
    sql = "SELECT u.username " \
          "FROM users AS u, reviews AS r " \
          "WHERE r.user_id=u.id AND u.banned=0 " \
          "GROUP BY u.username " \
          "ORDER BY COUNT(r.grade) DESC LIMIT 1"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def send(user_id, film_id, content, grade):
    sql = "INSERT INTO reviews (user_id, film_id, content, grade, submitted) " \
          "VALUES (:user_id, :film_id, :content, :grade, NOW())"
    db.session.execute(sql, {"user_id":user_id, "film_id":film_id, "content":content, "grade":grade})
    db.session.commit()
    return True