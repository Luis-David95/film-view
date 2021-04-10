from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password):
    sql = "SELECT password, id, username FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            session["username"] = user[2]
            if is_admin(username):
                session["is_admin"] = True
            else:
                session["is_admin"] = False         
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["username"]
    del session["is_admin"]

def register(username,password):
    hash_value = generate_password_hash(password)
    admin = 0
    try:
        sql = "INSERT INTO users (username,password,admin) VALUES (:username,:password,:admin)"
        db.session.execute(sql, {"username":username,"password":hash_value,"admin":admin})
        db.session.commit()
    except:
        return False
    return login(username,password)

def get_user_id():
    return session.get("user_id",0)

def is_admin(username):
    sql = "SELECT admin FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    admin = result.fetchone()
    if admin[0] == 1:
        return True
    else:
        return False