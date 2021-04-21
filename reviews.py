from db import db
import users

def get_list(film_id):
    sql = "SELECT u.username, r.content, r.grade FROM reviews AS r, users AS u WHERE r.film_id=:film_id AND u.id=r.user_id"
    result = db.session.execute(sql, {"film_id":film_id})
    return result.fetchall()

def send(grade, content, film_id, user_id):
    sql = "INSERT INTO reviews (grade, content, film_id, user_id) VALUES (:grade, :content, :film_id, :user_id)"
    db.session.execute(sql, {"grade":grade, "content":content, "film_id":film_id, "user_id":user_id})
    db.session.commit()
    return True