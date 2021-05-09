import secrets
from db import db
from flask import abort, session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT password, id, username, banned FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    banned = user[3]
    if user == None:
        return False
    if banned == 1:
        return False
    else:
        if check_password_hash(user[0], password):
            session["user_id"] = user[1]
            session["username"] = user[2]
            session["csrf_token"] = secrets.token_hex(16)
            if is_admin(username):
                session["is_admin"] = True
            else:
                session["is_admin"] = False
            sql = "UPDATE users SET last_login = NOW() WHERE username=:username"
            db.session.execute(sql, {"username":username})
            db.session.commit()
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["username"]
    del session["is_admin"]
    del session["csrf_token"]

def register(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, admin, banned, registered) " \
              "VALUES (:username, :password, 0, 0, NOW())"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)

def get_list():
    sql = "SELECT u.id, u.username, u.admin, u.banned, TO_CHAR(u.registered, 'D Month YYYY'), " \
          "TO_CHAR(u.last_login, 'D Month YYYY - HH24:MI'), c.name, c.code " \
          "FROM users AS u, countries AS c " \
          "WHERE c.id = u.country_id"
    result = db.session.execute(sql)
    return result.fetchall()

def exists(id):
    sql = "SELECT COUNT(1) FROM users WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    if result.fetchone()[0] == 0:
        abort(404)

def promote(id):
    sql = "UPDATE users SET admin=1 WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True

def ban(id):
    sql = "UPDATE users SET banned=1 WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True

def unban(id):
    sql = "UPDATE users SET banned=0 WHERE id=:id"
    db.session.execute(sql, {"id":id})
    db.session.commit()
    return True

def count():
    sql = "SELECT COUNT(*) FROM users"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def count_admins():
    sql = "SELECT COUNT(*) FROM users WHERE admin=1"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def count_banned():
    sql = "SELECT COUNT(*) FROM users WHERE banned=1"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def oldest_user():
    sql = "SELECT username FROM users GROUP BY username, registered ORDER BY registered ASC LIMIT 1"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def newest_user():
    sql = "SELECT username FROM users GROUP BY username, registered ORDER BY registered DESC LIMIT 1"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def last_to_login():
    sql = "SELECT username FROM users GROUP BY username, last_login ORDER BY last_login DESC LIMIT 1"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def get_user_id():
    return session.get("user_id", 0)

def get_name(id):
    sql = "SELECT username FROM users WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]

def is_admin(username):
    sql = "SELECT admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    admin = result.fetchone()
    if not admin or admin[0] == 0:
        return False
    else:
        return True

def require_status(level):
    if level == 0:
        id = get_user_id()
        if id == 0:
            abort(403)
    elif level == 1:
        if not is_admin(session.get("username")):
            abort(403)
    else:
        abort(500)