from flask import Flask, render_template
from os import getenv

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

@app.errorhandler(404)
def page_not_found(error):
   return render_template("error.html", message="404 - Page not found")

import routes