from flask import render_template


def message(message):
    return render_template("error.html", message=message)