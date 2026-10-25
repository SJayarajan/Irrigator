from flask import render_template,redirect, url_for, flash
from Irrigator import app
from Irrigator.forms import SignInForm,SignUpForm
from werkzeug.security import generate_password_hash
from Irrigator.db import users

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')

@app.route("/about")
def about():
    return render_template("about.html", title="About", body="About content")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        users.insert({'username': form.username.data,
                      'password_hash': generate_password_hash(form.password.data)})
        flash("Account created. Please sign in.", "success")
        return redirect(url_for("login"))
    return render_template("signup.html", title="Sign up", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = SignInForm()
    if form.validate_on_submit():
        flash(f"Signed in as {form.username.data}", "success")  # temporary, no credential check yet
        return redirect(url_for("home"))
    return render_template("login.html", title="Login", form=form)