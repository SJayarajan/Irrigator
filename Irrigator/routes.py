from flask import render_template,redirect, url_for, flash,session
from Irrigator import app
from Irrigator.forms import SignInForm,SignUpForm
from werkzeug.security import generate_password_hash,check_password_hash
from tinydb import Query
from Irrigator.db import users
User = Query()

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
        if users.contains(User.username == form.username.data):
            flash("Username already taken.", "danger")
            return render_template("signup.html", title="Sign up", form=form)

        users.insert({'username': form.username.data,
                      'password_hash': generate_password_hash(form.password.data)})
        flash("Account created. Please sign in.", "success")
        return redirect(url_for("login"))
    return render_template("signup.html", title="Sign up", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = SignInForm()
    if form.validate_on_submit():
        user = users.get(User.username == form.username.data)
        if user is None:
            flash("No account found. Please sign up.", "warning")
            return redirect(url_for("signup"))

        if check_password_hash(user["password_hash"], form.password.data):
            session.clear()
            session["user"] = user["username"]
            flash(f"Signed in as {user['username']}", "success")
            return redirect(url_for("home"))
        flash("Wrong password.", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("Logged out.", "info")
    return redirect(url_for("login"))