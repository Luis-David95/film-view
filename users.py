import secrets
from db import db
from flask import abort, session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
    sql = "SELECT password, id, username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
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

def register(username, password, country_id):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password, admin, banned, country_id, registered) " \
              "VALUES (:username, :password, 0, 0, :country_id, NOW())"
        db.session.execute(sql, {"username":username, "password":hash_value, "country_id":country_id})
        db.session.commit()
    except:
        return False
    return login(username, password)

def count():
    sql = "SELECT COUNT(*) FROM users"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def count_admins():
    sql = "SELECT COUNT(*) FROM users WHERE admin=1"
    result = db.session.execute(sql)
    return result.fetchone()[0]

def get_user_id():
    return session.get("user_id", 0)

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