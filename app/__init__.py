from os import getenv

from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")


@app.errorhandler(400)
def bad_request(error):
    return render_template("error.html", message="400 - Bad request")


@app.errorhandler(403)
def forbidden(error):
    return render_template("error.html", message="403 - Forbidden")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", message="404 - Page not found")


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("error.html", message="500 - Internal server error")


from app import routes