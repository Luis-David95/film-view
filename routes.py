from app import app
from flask import abort, redirect, render_template, request, session, url_for
import countries, directors, error, films, genres, languages, reviews, screenwriters, statistics, users

@app.route("/")
def index():
    film_list = films.get_visible(0)
    return render_template("index.html", films=film_list)

@app.route("/sort")
def sort():
    sort_by = int(request.args["sort-by"])
    film_list = films.get_visible(sort_by)
    return render_template("index.html", films=film_list)

@app.route("/search")
def search():
    query = request.args["query"]
    film_list = films.get_search_results(query)
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
            return error.message("Logging in failed")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        country_list = countries.get_list()
        return render_template("register.html", countries=country_list)
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username, password):
            return redirect("/")
        else:
            return error.message("Registration failed")

@app.route("/statistics")
def stats():
    user_count = users.count()
    admin_count = users.count_admins()
    banned_count = users.count_banned()
    most_active = reviews.get_most_active_user()
    oldest_user = users.oldest_user()
    newest_user = users.newest_user()
    last_to_login = users.last_to_login()
    film_count = films.count()
    review_count = reviews.count()
    highest = reviews.get_highest_rated()
    lowest = reviews.get_lowest_rated()
    average = reviews.get_average_grade()
    country_count = countries.count()
    language_count = languages.count()
    genre_count = genres.count()
    director_count = directors.count()
    screenwriter_count = screenwriters.count()
    return render_template("statistics.html", users=user_count, admins=admin_count, banned=banned_count, most_active=most_active,
                                              oldest=oldest_user, newest=newest_user, last_to_login=last_to_login, films=film_count,
                                              reviews=review_count, highest=highest, lowest=lowest, average=average, countries=country_count,
                                              languages=language_count, genres=genre_count, directors=director_count, screenwriters=screenwriter_count)

@app.route("/countries", methods=["get","post"])
def country():
    if request.method == "GET":
        users.require_status(1)
        count = countries.count()
        country_list = countries.get_details()
        return render_template("countries.html", count=count, countries=country_list)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        if countries.create_list():
            return redirect("/countries")
        else:
            return error.message("Creating country list failed, perhaps it already exists?")

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
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        name = request.form["name"]
        if len(name) == 0:
            return error.message("Name cannot be empty")
        if len(name) > 50:
            return error.message("Name is too long")
        description = request.form["description"]
        if len(description) == 0:
            return error.message("Description cannot be empty")
        if len(description) > 500:
            return error.message("Description is too long")
        try:
            year = int(request.form["year"])
        except ValueError:
            return error.message("Year cannot be empty")
        if year < 1888 or year > 2021:
            return error.message("Please enter a correct year")
        try:
            country_id = int(request.form["country_id"])
        except:
            return error.message("Please select a country from the list")
        try:
            language_id = int(request.form["language_id"])
        except:
            return error.message("Please select a language from the list or add new one")
        if language_id == 0:
            new_language = request.form["new_language"]
            if len(new_language) == 0:
                return error.message("Language cannot be empty")
            if len(new_language) < 3:
                return error.message("Language name is too short")
            languages.send(new_language)
            language_id = languages.count()
        try:
            genre_id = int(request.form["genre_id"])
        except:
            return error.message("Please select a genre from the list or add new one")
        if genre_id == 0:
            new_genre = request.form["new_genre"]
            genres.send(new_genre)
            genre_id = genres.count()
        try:
            director_id = int(request.form["director_id"])
        except:
            return error.message("Please select a director from the list or add new one")
        try:
            screenwriter_id = int(request.form["screenwriter_id"])
        except:
            return error.message("Please select a screenwriter from the list or add new one")
        if films.send(name, description, year, country_id, language_id, genre_id, director_id, screenwriter_id):
            return redirect("/")
        else:
            return error.message("Sending failed")

@app.route("/new_director", methods=["get","post"])
def new_director():
    if request.method == "GET":
        users.require_status(1)
        country_list = countries.get_list()
        return render_template("new_director.html", countries=country_list)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        name = request.form["name"]
        if len(name) == 0:
            return error.message("Name cannot be empty")
        if len(name) > 50:
            return error.message("Name is too long")
        description = request.form["description"]
        if len(description) == 0:
            return error.message("Description cannot be empty")
        if len(description) > 500:
            return error.message("Description is too long")
        try:
            country_id = int(request.form["country_id"])
        except:
            return error.message("Please select a country from the list")
        if directors.send(name, description, country_id):
            return redirect("/new_film")
        else:
            return error.message("Sending failed")

@app.route("/new_screenwriter", methods=["get","post"])
def new_screenwriter():
    if request.method == "GET":
        users.require_status(1)
        country_list = countries.get_list()
        return render_template("new_screenwriter.html", countries=country_list)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        name = request.form["name"]
        if len(name) == 0:
            return error.message("Name cannot be empty")
        if len(name) > 50:
            return error.message("Name is too long")
        description = request.form["description"]
        if len(description) == 0:
            return error.message("Description cannot be empty")
        if len(description) > 500:
            return error.message("Description is too long")
        try:
            country_id = int(request.form["country_id"])
        except:
            return error.message("Please select a country from the list")
        if screenwriters.send(name, description, country_id):
            return redirect("/new_film")
        else:
            return error.message("Sending failed")

@app.route("/films/")
def manage_films():
    users.require_status(1)
    film_list = films.get_all()
    return render_template("films.html", films=film_list)

@app.route("/delete/<int:id>", methods=["get","post"])
def delete(id):
    if request.method == "GET":
        films.exists(id)
        users.require_status(1)
        name = films.get_name(id)
        return render_template("delete.html", name=name, id=id)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        if films.delete(id):
            return redirect("/")
        else:
            return error.message("Deleting film failed")

@app.route("/restore/<int:id>", methods=["get","post"])
def restore(id):
    if request.method == "GET":
        if films.visible(id) == 0:
            users.require_status(1)
            name = films.get_name(id)
            return render_template("restore.html", name=name, id=id)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        if films.restore(id):
            return redirect("/")
        else:
            return error.message("Restoring film failed")

@app.route("/users/")
def manage_users():
    users.require_status(1)
    user_list = users.get_list()
    return render_template("users.html", users=user_list)

@app.route("/promote/<int:id>", methods=["get","post"])
def promote(id):
    if request.method == "GET":
        users.exists(id)
        users.require_status(1)
        name = users.get_name(id)
        return render_template("promote.html", name=name, id=id)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        if users.promote(id):
            return redirect("/users")
        else:
            return error.message("Promoting user failed")

@app.route("/ban/<int:id>", methods=["get","post"])
def ban(id):
    if request.method == "GET":
        users.exists(id)
        users.require_status(1)
        name = users.get_name(id)
        return render_template("ban.html", name=name, id=id)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        if users.ban(id):
            return redirect("/users")
        else:
            return error.message("Banning user failed")

@app.route("/unban/<int:id>", methods=["get","post"])
def unban(id):
    if request.method == "GET":
        users.exists(id)
        users.require_status(1)
        name = users.get_name(id)
        return render_template("unban.html", name=name, id=id)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        if users.unban(id):
            return redirect("/users")
        else:
            return error.message("Banning user failed")

@app.route("/film/<int:id>")
def film(id):
    films.exists(id)
    name = films.get_name(id)
    review_list = reviews.get_list(id)
    film_list = films.get_details(id)
    grade_details = reviews.get_grade_details(id)
    return render_template("film.html", id=id, name=name, reviews=review_list,
                                        details=film_list, grade_details=grade_details)

@app.route("/film/<int:id>/new_review", methods=["get","post"])
def new_review(id):
    if request.method == "GET":
        users.require_status(0)
        films.exists(id)
        name = films.get_name(id)
        return render_template("new_review.html", name=name, id=id)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        user_id = users.get_user_id()
        film_id = id
        content = request.form["content"]
        if len(content) < 10:
            return error.message("Review content too short or doesn't exist")
        elif len(content) > 1000:
            return error.message("Review content too long")
        grade = int(request.form["grade"])
        if reviews.send(user_id, film_id, content, grade):
            return redirect(url_for("film", id=id))
        else:
            return error.message("Sending failed")