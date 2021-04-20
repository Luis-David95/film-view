from db import db
import users

def get_list(film_id):
    sql = "SELECT id, content, grade FROM reviews WHERE film_id=:film_id"
    result = db.session.execute(sql, {"film_id":film_id})
    return result.fetchall()