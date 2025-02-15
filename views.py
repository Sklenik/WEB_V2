from flask import Blueprint, render_template

views = Blueprint("views",__name__)

@views.route("/")
def home():
    return render_template("home.html", lang='cz')

@views.route("/en")
def about():
    return render_template("home_en.html", lang='en')