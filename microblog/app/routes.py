from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import *
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime
from flask_mail import Message

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

    form = EducatioForm()
    if form.validate_on_submit():
        current_user.degree = form.degree.data
        current_user.field_of_study = form.field_of_study.data
        current_user.institution = form.institution.data
        current_user.location = form.location.data
        current_user.year_awarded = form.year_awarded.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.degree.data = current_user.
        form.field_of_study.data = current_user.field_of_study
        form.institution.data = current_user.institution
        form.location.data = current_user.location
        form.year_awarded.data = current_user.year_awarded

    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =Employment()
    if form.validate_on_submit():
        current_user.institution = form.institution.data
        current_user.location = form.location.data
        current_user.years = form.years.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.institution.data = current_user.institution
        form.location.data = current_user.location
        form.years.data = current_user.years
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =ProfessionalSocietiesForm()
    if form.validate_on_submit():
        current_user.start_date = form.start_date.data
        current_user.end_date = form.end_date.data
        current_user.society = form.society.data
        current_user.membership = form.membership.data
        current_user.status = form.status.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.start_date.data = current_user.start_date
        form.end_date.data = current_user.end_date
        form.society.data = current_user.society
        form.membership.data = current_user.membership
        form.status.data = current_user.status
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =DistinctionsAwardsForm()
    if form.validate_on_submit():
        current_user.year = form.year.data
        current_user.awarding_body = form.awarding_body.data
        current_user.award_details = form.award_details.data
        current_user.member_name = form.member_name.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.year.data = current_user.year
        form.awarding_body.data = current_user.awarding_body
        form.award_details.data = current_user.award_details
        form.member_name.data = current_user.member_name
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =FundingForm()
    if form.validate_on_submit():
        current_user.start_date = form.start_date.data
        current_user.end_date = form.end_date.data
        current_user.funding_amount = form.funding_amount.data
        current_user.funding_body = form.funding_body.data
        current_user.fudning_programme = form.fudning_programme.data
        current_user.status = form.status.data
        current_user.primary_attribution = form.primary_attribution.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.start_date.data = current_user.start_date
        form.end_date.data = current_user.end_date
        form.funding_amount.data = current_user.funding_amount
        form.funding_body.data = current_user.funding_body
        form.fudning_programme.data = current_user.fudning_programme
        form.status.data = current_user.status
        form.primary_attribution.data = current_user.primary_attribution
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =TeamMembersForm()
    if form.validate_on_submit():
        current_user.start_date = form.start_date.data
        current_user.departure_date = form.departure_date.data
        current_user.name = form.name.data
        current_user.position_in_team = form.position_in_team.data
        current_user.primary_attribution = form.primary_attribution.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.start_date.data = current_user.start_date
        form.departure_date.data = current_user.departure_date
        form.name.data = current_user.name
        form.position_in_team.data = current_user.position_in_team
        form.primary_attribution.data = current_user.primary_attribution
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =ImpactsForm()
    if form.validate_on_submit():
        current_user.title  = form.title .data
        current_user.category = form.category.data
        current_user.primary_beneficiary  = form.primary_beneficiary .data
        current_user.primary_attribution = form.primary_attribution.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.title .data = current_user.title
        form.category.data = current_user.category
        form.primary_beneficiary .data = current_user.primary_beneficiary
        form.primary_attribution.data = current_user.primary_attribution
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =InovationForm()
    if form.validate_on_submit():
        current_user.year = form.year.data
        current_user.innovation_type = form.innovation_type.data
        current_user.title  = form.title .data
        current_user.primary_attribution  = form.primary_attribution .data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.year.data = current_user.year
        form.innovation_type.data = current_user.innovation_type
        form.title .data = current_user.title
        form.primary_attribution .data = current_user.primary_attribution
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =PublicationsForm()
    if form.validate_on_submit():
        current_user.year  = form.year .data
        current_user.publication_type  = form.publication_type .data
        current_user.title = form.title.data
        current_user.journal_name = form.journal_name.data
        current_user.status = form.status.data
        current_user.doi = form.doi.data
        current_user.primary_attribution = form.primary_attribution.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.year .data = current_user.year
        form.publication_type .data = current_user.publication_type
        form.title.data = current_user.title
        form.journal_name.data = current_user.journal_name
        form.status.data = current_user.status
        form.doi.data = current_user.doi
        form.primary_attribution.data = current_user.primary_attribution
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =PresentationsForm()
    if form.validate_on_submit():
        current_user.year = form.year.data
        current_user.title = form.title.data
        current_user.event_type = form.event_type.data
        current_user.organising_body = form.organising_body.data
        current_user.location = form.location.data
        current_user.primary_attribution = form.primary_attribution.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.year.data = current_user.year
        form.title.data = current_user.title
        form.event_type.data = current_user.event_type
        form.organising_body.data = current_user.organising_body
        form.location.data = current_user.location
        form.primary_attribution.data = current_user.primary_attribution
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =AcademicColabForm()
    if form.validate_on_submit():
        current_user.start_date = form.start_date.data
        current_user.end_date = form.end_date.data
        current_user.institution = form.institution.data
        current_user.department = form.department.data
        current_user.location = form.location.data
        current_user.collaborator = form.collaborator.data
        current_user.collaborator_goal = form.collaborator_goal.data
        current_user.interaction_freq = form.interaction_freq.data
        current_user.primary_attribution = form.primary_attribution.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.start_date.data = current_user.start_date
        form.end_date.data = current_user.end_date
        form.institution.data = current_user.institution
        form.department.data = current_user.department
        form.location.data = current_user.location
        form.collaborator.data = current_user.collaborator
        form.collaborator_goal.data = current_user.collaborator_goal
        form.interaction_freq.data = current_user.interaction_freq
        form.primary_attribution.data = current_user.primary_attribution
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =NonAcademicColabForm()
    if form.validate_on_submit():
        current_user.start_date = form.start_date.data
        current_user.end_date = form.end_date.data
        current_user.institution = form.institution.data
        current_user.department = form.department.data
        current_user.location = form.location.data
        current_user.collaborator = form.collaborator.data
        current_user.collaborator_goal = form.collaborator_goal.data
        current_user.interaction_freq = form.interaction_freq.data
        current_user.primary_attribution = form.primary_attribution.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.start_date.data = current_user.start_date
        form.end_date.data = current_user.end_date
        form.institution.data = current_user.institution
        form.department.data = current_user.department
        form.location.data = current_user.location
        form.collaborator.data = current_user.collaborator
        form.collaborator_goal.data = current_user.collaborator_goal
        form.interaction_freq.data = current_user.interaction_freq
        form.primary_attribution.data = current_user.primary_attribution
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =ConferencesForm()
    if form.validate_on_submit():
        current_user.start_date = form.start_date.data
        current_user.end_date = form.end_date.data
        current_user.title = form.title.data
        current_user.event_type = form.event_type.data
        current_user.role = form.role.data
        current_user.location = form.location.data
        current_user.primary_attribution = form.primary_attribution.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.start_date.data = current_user.start_date
        form.end_date.data = current_user.end_date
        form.title.data = current_user.title
        form.event_type.data = current_user.event_type
        form.role.data = current_user.role
        form.location.data = current_user.location
        form.primary_attribution.data = current_user.primary_attribution
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =CommunicationsForm()
    if form.validate_on_submit():
        current_user.year = form.year.data
        current_user.number_lectures = form.number_lectures.data
        current_user.number_visits = form.number_visits.data
        current_user.number_media = form.number_media.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.year.data = current_user.year
        form.number_lectures.data = current_user.number_lectures
        form.number_visits.data = current_user.number_visits
        form.number_media.data = current_user.number_media
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =FundingRatioForm()
    if form.validate_on_submit():
        current_user.year = form.year.data
        current_user.annual_spend = form.annual_spend.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.year.data = current_user.year
        form.annual_spend.data = current_user.annual_spend
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)

    form =PublicEngagementForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.start_date = form.start_date.data
        current_user.end_date = form.end_date.data
        current_user.activity_type = form.activity_type.data
        current_user.topic = form.topic.data
        current_user.target_area = form.target_area.data
        current_user.primary_attribution = form.primary_attribution.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))
    elif request.method == "GET":
        form.name.data = current_user.name
        form.start_date.data = current_user.start_date
        form.end_date.data = current_user.end_date
        form.activity_type.data = current_user.activity_type
        form.topic.data = current_user.topic
        form.target_area.data = current_user.target_area
        form.primary_attribution.data = current_user.primary_attribution
    return render_template("edit_profile.html", title="Edit Profile", form=form, img=svg)


@app.route("/register", methods=["GET", "POST"])
@login_required
def register():
    msg = Message("Thank you for registering",
    sender="jacobmckeon23@gmail.com",
    recipients=["115336756@umail.ucc.ie"])
    if current_user.is_authenticated or not current_user.is_admin():
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

        user = User(username=form.username.data, email=form.email.data, access=1)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        mail.send(msg)
        flash("Succesfully Registered")
        return redirect(url_for("index"))
    return render_template("register.html", title="Register", form=form, img=svg)


@app.route("/makecall", methods=["GET", "POST"])
@login_required
def makecall():
    user = User.query.filter_by(username=current_user.username).first_or_404()

    if not user.is_admin():
        flash("No Permission for this area")
        return redirect(url_for("index"))

    form = CallsForProposalForm()

    return render_template("makecall.html", form=form, img=svg, title="Make Call Proposal")


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
    return render_template('profile.html', user=user, img=svg)


@app.route("/workbench")
@login_required
def workbench():
    education_info = current_user.education_info.all()
    education_length = len(education_info)
    form = CallsForProposalFilter()
    return render_template("workbench.html", user=current_user, img=svg, education_info=education_info, form=form,
                           edu_len=education_length)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/calls", methods=["GET", "POST"])
def calls():
	form = CallsForProposalFilter()
	return render_template("calls.html", title="Calls for Proposals", form=form, img=svg)

@app.route("/admin")
def admin():
    return render_template("admin.html", title="Admin", img=svg)


# how to start venv: "source venv/bin/activate"


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
