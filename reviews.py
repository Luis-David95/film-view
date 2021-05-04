from db import db
import users

def count():
    sql = "SELECT COUNT(*) FROM reviews"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def get_list(film_id):
    sql = "SELECT u.username, r.content, r.grade, TO_CHAR(r.submitted, 'DD Month YYYY - HH24:MI'), c.name, c.code " \
          "FROM reviews AS r, users AS u, countries AS c " \
          "WHERE r.film_id=:film_id AND u.id=r.user_id AND c.id=u.country_id"
    result = db.session.execute(sql, {"film_id":film_id})
    return result.fetchall()

def get_grade_details(film_id):
    sql = "SELECT ROUND(AVG(r.grade),1), COUNT(DISTINCT r.id) " \
          "FROM reviews AS r, films AS f " \
          "WHERE r.film_id=:film_id"
    result = db.session.execute(sql, {"film_id":film_id})
    return result.fetchall()

def send(user_id, film_id, content, grade):
    sql = "INSERT INTO reviews (user_id, film_id, content, grade, submitted) " \
          "VALUES (:user_id, :film_id, :content, :grade, NOW())"
    db.session.execute(sql, {"user_id":user_id, "film_id":film_id, "content":content, "grade":grade})
    db.session.commit()
    return True