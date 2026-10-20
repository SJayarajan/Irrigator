from flask import render_template
from Irrigator import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')

@app.route("/about")
def about():
    return render_template("about.html", title="About", body="About content")

@app.route("/signup")
def signup():
    return render_template("sign_up.html", title="Sign up", body="")

@app.route("/login")
def login():
    return render_template("login.html", title="Sign up", body="")