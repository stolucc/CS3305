from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app.models import User

#This is a test again. and again and again
@app.route('/')
@app.route("/index")
def index():
    user = {"username": "User"}
    posts = [
        {
            "author": {"username": "Researcher1"},
            "body": "Activity: I employed x y z"
        },
        {
            "author": {"username": "Researcher2"},
            "body": "Activity: I went and did a talk"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegisterForm()
    if form.validate_on_submit():
        if not form.validate_email(form.email):
            flash("Please enter a valid email")
            return redirect(url_for("register"))
        if not form.validate_passwordmatch(form.password, form.confirmpass):
            flash("Passwords do not match")
            return redirect(url_for("register"))
        if not form.validate_username(form.username):
            flash("Username not valid")
            return redirect(url_for("register"))

        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Succesfully Registered")
        return redirect(url_for("index"))
    return render_template("register.html", title="Register", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

# how to start venv: "source venv/bin/activate"
