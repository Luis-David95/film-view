from app import app
from flask import redirect, render_template, request, url_for
import countries, directors, films, genres, languages, reviews, screenwriters, users

@app.route("/")
def index():
    film_list = films.get_visible()
    return render_template("index.html", films=film_list)

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Wrong username or password")

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
        if users.register(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Registration failed")

@app.route("/statistics")
def statistics():
    user_count = users.count()
    film_count = films.count()
    review_count = reviews.count()
    return render_template("statistics.html", users=user_count, films=film_count, reviews=review_count)

@app.route("/countries", methods=["get","post"])
def country():
    if request.method == "GET":
        users.require_status(1)
        count = countries.count()
        return render_template("countries.html", count=count)
    if request.method == "POST":
        if countries.create_list():
            return redirect("/countries")
        else:
            return render_template("error.html", message="Creating country list failed, perhaps it already exists?")

@app.route("/new_film", methods=["get","post"])
def new_film():
    if request.method == "GET":
        users.require_status(1)
        country_list = countries.get_list()
        language_list = languages.get_list()
        genre_list = genres.get_list()
        director_list = directors.get_list()
        screenwriter_list = screenwriters.get_list()
        return render_template("new_film.html", countries=country_list, languages=language_list, genres=genre_list, 
                                                directors=director_list, screenwriters=screenwriter_list)
    if request.method == "POST":
        name = request.form["name"]
        if len(name) == 0:
            return render_template("error.html", message="Name cannot be empty")
        if len(name) > 50:
            return render_template("error.html", message="Name is too long")
        description = request.form["description"]
        if len(description) == 0:
            return render_template("error.html", message="Description cannot be empty")
        if len(description) > 500:
            return render_template("error.html", message="Description is too long")
        year = int(request.form["year"])
        if year < 1888 or year > 2021:
            return render_template("error.html", message="Please enter a correct year")
        country_id = int(request.form["country_id"])
        language_id = int(request.form["language_id"])
        if language_id == 0:
            new_language = request.form["new_language"]
            languages.send(new_language)
            language_id = languages.count()
        genre_id = int(request.form["genre_id"])
        if genre_id == 0:
            new_genre = request.form["new_genre"]
            genres.send(new_genre)
            genre_id = genres.count()
        director_id = int(request.form["director_id"])
        screenwriter_id = int(request.form["screenwriter_id"])
        if films.send(name, description, year, country_id, language_id, genre_id, director_id, screenwriter_id):
            return redirect("/")
        else:
            return render_template("error.html", message="Sending failed")

@app.route("/new_director", methods=["get","post"])
def new_director():
    if request.method == "GET":
        users.require_status(1)
        country_list = countries.get_list()
        return render_template("new_director.html", countries=country_list)
    if request.method == "POST":
        name = request.form["name"]
        if len(name) == 0:
            return render_template("error.html", message="Name cannot be empty")
        if len(name) > 50:
            return render_template("error.html", message="Name is too long")
        description = request.form["description"]
        if len(description) == 0:
            return render_template("error.html", message="Description cannot be empty")
        if len(description) > 500:
            return render_template("error.html", message="Description is too long")
        country_id = int(request.form["country_id"])
        if directors.send(name, description, country_id):
            return redirect("/new_film")
        else:
            return render_template("error.html", message="Sending failed")

@app.route("/new_screenwriter", methods=["get","post"])
def new_screenwriter():
    if request.method == "GET":
        users.require_status(1)
        country_list = countries.get_list()
        return render_template("new_screenwriter.html", countries=country_list)
    if request.method == "POST":
        name = request.form["name"]
        if len(name) == 0:
            return render_template("error.html", message="Name cannot be empty")
        if len(name) > 50:
            return render_template("error.html", message="Name is too long")
        description = request.form["description"]
        if len(description) == 0:
            return render_template("error.html", message="Description cannot be empty")
        if len(description) > 500:
            return render_template("error.html", message="Description is too long")
        country_id = int(request.form["country_id"])
        if screenwriters.send(name, description, country_id):
            return redirect("/new_film")
        else:
            return render_template("error.html", message="Sending failed")

@app.route("/films/")
def manage():
    users.require_status(1)
    films_list = films.get_all()
    return render_template("films.html", films=films_list)

@app.route("/delete/<int:id>", methods=["get","post"])
def delete(id):
    if request.method == "GET":
        films.exists(id)
        users.require_status(1)
        name = films.get_name(id)
        return render_template("delete.html", name=name, id=id)
    if request.method == "POST":
        if films.delete(id):
            return redirect("/")
        else:
            return render_template("error.html", message="Deleting film failed")

@app.route("/restore/<int:id>", methods=["get","post"])
def restore(id):
    if request.method == "GET":
        if films.visible(id) == 0:
            users.require_status(1)
            name = films.get_name(id)
            return render_template("restore.html", name=name, id=id)
    if request.method == "POST":
        if films.restore(id):
            return redirect("/")
        else:
            return render_template("error.html", message="Restoring film failed")

@app.route("/film/<int:id>")
def film(id):
    films.exists(id)
    review_list = reviews.get_list(id)
    film_list = films.get_details(id)
    grade_details = reviews.get_grade_details(id)
    return render_template("film.html", id=id, reviews=review_list, details=film_list, grade_details=grade_details)

@app.route("/film/<int:id>/new_review", methods=["get","post"])
def new_review(id):
    if request.method == "GET":
        users.require_status(0)
        films.exists(id)
        name = films.get_name(id)
        return render_template("new_review.html", name=name, id=id)
    if request.method == "POST":
        user_id = users.get_user_id()
        film_id = id
        content = request.form["content"]
        if len(content) < 10:
            return render_template("error.html", message="Review content too short or doesn't exist")
        grade = int(request.form["grade"])
        if reviews.send(user_id, film_id, content, grade):
            return redirect(url_for("film", id=id))
        else:
            return render_template("error.html", message="Sending failed")