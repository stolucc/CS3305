from flask import render_template, flash, redirect, url_for, request
from markupsafe import Markup

from app import app, db
from app.forms import LoginForm, RegisterForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime

from app.models import *

# Creates a URL route to each html page and connects them with their corresponding form from forms.py

svg = "/static/sfi-logo.svg"


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html", title="Home", img=svg)


@app.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)


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
    return render_template("register.html", title="Register", form=form, img=svg)


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
    return render_template("login.html", title="Sign In", form=form, img=svg)


@app.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts

    return render_template('profile.html', user=user, posts=posts, img=svg)

@app.route("/workbench")
@login_required
def workbench():
    education_info = current_user.education_info.all()
    education_length = len(education_info)
    return render_template("workbench.html", user=current_user, img=svg, education_info=education_info, edu_len = education_length)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/calls", methods=["GET", "POST"])
def calls():
	return render_template("calls.html", title="Calls for Proposals", img=svg)


# how to start venv: "source venv/bin/activate"


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
