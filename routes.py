from app import app
from flask import render_template, request, redirect, url_for
import users, films, reviews

@app.route("/")
def index():
    list = films.get_list()
    return render_template("index.html", films=list)

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Wrong username or password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Registration failed")

@app.route("/new_film", methods=["get","post"])
def new_film():
    if request.method == "GET":
        return render_template("new_film.html")
    if request.method == "POST":
        name = request.form["name"]
        if (len(name) == 0):
            return render_template("error.html",message="Name cannot be empty")
        description = request.form["description"]
        if (len(description) == 0):
            return render_template("error.html",message="Description cannot be empty")
        if films.send(name, description):
            return redirect("/")
        else:
            return render_template("error.html",message="Sending failed")

@app.route("/film/<int:id>")
def review(id):
    name = films.get_name(id)
    review_list = reviews.get_list(id)
    return render_template("film.html", name=name, id=id, reviews=review_list)