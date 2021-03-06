from flask import render_template, flash, redirect, url_for, request, send_from_directory
from app import app, db, mail
from app.forms import *
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from flask_mail import Message

from app.models import *

# Creates a URL route to each html page and connects them with their corresponding form from forms.py

svg = "/static/sfi-logo.svg"
UPLOAD_FOLDER = '/home/jack/PycharmProjects/CS3305/microblog/app/uploads'
ALLOWED_EXTENSIONS = set(['pdf'])


@app.route('/')
@app.route("/index")
def index():
    return render_template("index.html", title="Home", img=svg)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/upload_file", methods=["GET", "POST"])
@login_required
def upload_file():
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("uploaded_file", filename=filename))
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    """


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route("/edit_profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    if current_user.access == 2 or current_user.access == 3 or current_user.access == 4:
        flash("This area is for researcher profile edits only")
        return redirect(url_for("index"))
    edu_form = EducationForm()
    emp_form = EmploymentForm()
    prof_form = ProfessionalStudiesForm()
    dist_form = DistinctionsAndAwardsForm()
    fund_form = FundingDiversificationForm()
    team_form = TeamMembersForm()
    impact_form = ImpactsForm()
    inov_form = InovationForm()
    public_form = PublicationsForm()
    pres_form = PresentationsForm()
    non_ac_form = NonAcademicColabForm()
    ac_form = AcademicColabForm()
    conf_form = ConferencesForm()
    commun_form = CommunicationsForm()
    fund_ratio_form = FundingRatioForm()
    public_eng_form = PublicEngagementForm()

    if edu_form.validate_on_submit():
        user_edu_info = EducationInfo.query.filter_by(user_id=current_user.id).first()
        if user_edu_info is None:
            user_edu_info = EducationInfo(user_id=current_user.id)
        user_edu_info.degree = edu_form.degree.data
        user_edu_info.field_of_study = edu_form.field_of_study.data
        user_edu_info.institution = edu_form.institution.data
        user_edu_info.location = edu_form.location.data
        user_edu_info.year_of_degree = edu_form.year_awarded.data
        db.session.add(user_edu_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif emp_form.validate_on_submit():
        emp_info = Employment.query.filter_by(user_id=current_user.id).first()
        if emp_info is None:
            emp_info = Employment(user_id=current_user.id)
        emp_info.institution = emp_form.institution.data
        emp_info.location = emp_form.location.data
        emp_info.years = emp_form.years.data
        db.session.add(emp_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for("edit_profile"))

    elif prof_form.validate_on_submit():
        user_prof_info = ProfessionalStudies.query.filter_by(user_id=current_user.id).first()
        if user_prof_info is None:
            user_prof_info = ProfessionalStudies(user_id=current_user.id)
        user_prof_info.start_date = prof_form.start_date.data
        user_prof_info.end_date = prof_form.end_date.data
        user_prof_info.society_name = prof_form.society.data
        user_prof_info.member_type = prof_form.membership.data
        user_prof_info.status = prof_form.status.data
        db.session.add(user_prof_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif dist_form.validate_on_submit():
        user_dist_info = DistinctionsAndAwards.query.filter_by(user_id=current_user.id).first()
        if user_dist_info is None:
            user_dist_info = DistinctionsAndAwards(user_id=current_user.id)
        user_dist_info.year = dist_form.year.data
        user_dist_info.awarding_body = dist_form.awarding_body.data
        user_dist_info.award_details = dist_form.award_details.data
        user_dist_info.member_name = dist_form.member_name.data
        db.session.add(user_dist_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif fund_form.validate_on_submit():
        user_fund_info = FundingDiversification.query.filter_by(user_id=current_user.id).first()
        if user_fund_info is None:
            user_fund_info = FundingDiversification(user_id=current_user.id)
        user_fund_info.start_date = fund_form.start_date.data
        user_fund_info.end_date = fund_form.end_date.data
        user_fund_info.funding_amt = fund_form.funding_amount.data
        user_fund_info.funding_body = fund_form.funding_body.data
        user_fund_info.funding_program = fund_form.funding_program.data
        db.session.add(user_fund_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif team_form.validate_on_submit():
        user_team_info = TeamMembers.query.filter_by(user_id=current_user.id).first()
        if user_team_info is None:
            user_team_info = TeamMembers(user_id=current_user.id)
        user_team_info.name = team_form.name.data
        user_team_info.position_in_team = team_form.position_in_team.data
        user_team_info.start_date = team_form.start_date.data
        user_team_info.end_date = team_form.departure_date.data
        user_team_info.other_users = team_form.other_users.data
        db.session.add(user_team_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif impact_form.validate_on_submit():
        user_impact_info = Impacts.query.filter_by(user_id=current_user.id).first()
        if user_impact_info is None:
            user_impact_info = Impacts(user_id=current_user.id)
        user_impact_info.title = impact_form.title.data
        user_impact_info.category = impact_form.category.data
        user_impact_info.primary_beneficiary = impact_form.primary_beneficiary.data
        user_impact_info.primary_attribution = impact_form.primary_attribution.data
        db.session.add(user_impact_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif inov_form.validate_on_submit():
        user_innovations_info = Innovation.query.filter_by(user_id=current_user.id).first()
        if user_innovations_info is None:
            user_innovations_info = Innovation(user_id=current_user.id)
        user_innovations_info.year = inov_form.year.data
        user_innovations_info.innovation_type = inov_form.innovation_type.data
        user_innovations_info.title = inov_form.title.data
        user_innovations_info.primary_attribution = inov_form.primary_attribution.data
        db.session.add(user_innovations_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif public_form.validate_on_submit():
        publications_info = Publication.query.filter_by(user_id=current_user.id).first()
        if publications_info is None:
            publications_info = Publication(user_id=current_user.id)
        publications_info.year = public_form.year.data
        publications_info.publication_type = public_form.publication_type.data
        publications_info.title = public_form.title.data
        publications_info.journal_name = public_form.journal_name.data
        publications_info.status = public_form.status.data
        publications_info.doi = public_form.doi.data
        publications_info.primary_attribution = public_form.primary_attribution.data
        db.session.add(publications_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif pres_form.validate_on_submit():
        pres_info = Presentation.query.filter_by(user_id=current_user.id).first()
        if pres_info is None:
            pres_info = Presentation(user_id=current_user.id)
        pres_info.year = pres_form.year.data
        pres_info.title = pres_form.title.data
        pres_info.event_type = pres_form.event_type.data
        pres_info.organising_body = pres_form.organising_body.data
        pres_info.location = pres_form.location.data
        pres_info.primary_attribution = pres_form.primary_attribution.data
        db.session.add(pres_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif ac_form.validate_on_submit():
        ac_info = AcademicCollabs.query.filter_by(user_id=current_user.id).first()
        if ac_info is None:
            ac_info = AcademicCollabs(user_id=current_user.id)
        ac_info.start_date = ac_form.start_date.data
        ac_info.end_date = ac_form.end_date.data
        ac_info.institution = ac_form.institution.data
        ac_info.department = ac_form.department.data
        ac_info.location = ac_form.location.data
        ac_info.collaborator = ac_form.collaborator.data
        ac_info.collaborator_goal = ac_form.collaborator_goal.data
        ac_info.interaction_freq = ac_form.interaction_freq.data
        ac_info.primary_attribution = ac_form.primary_attribution.data
        db.session.add(ac_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif non_ac_form.validate_on_submit():
        non_ac_info = NonAcademicCollabs.query.filter_by(user_id=current_user.id).first()
        if non_ac_info is None:
            non_ac_info = NonAcademicCollabs(user_id=current_user.id)
        non_ac_info.start_date = non_ac_form.start_date.data
        non_ac_info.end_date = non_ac_form.end_date.data
        non_ac_info.institution = non_ac_form.institution.data
        non_ac_info.department = non_ac_form.department.data
        non_ac_info.location = non_ac_form.location.data
        non_ac_info.collaborator = non_ac_form.collaborator.data
        non_ac_info.collaborator_goal = non_ac_form.collaborator_goal.data
        non_ac_info.interaction_freq = non_ac_form.interaction_freq.data
        non_ac_info.primary_attribution = non_ac_form.primary_attribution.data
        db.session.add(non_ac_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif conf_form.validate_on_submit():
        conf_info = Conference.query.filter_by(user_id=current_user.id).first()
        if conf_info is None:
            conf_info = Conference(user_id=current_user.id)
        conf_info.start_date = conf_form.start_date.data
        conf_info.end_date = conf_form.end_date.data
        conf_info.title = conf_form.title.data
        conf_info.event_type = conf_form.event_type.data
        conf_info.role = conf_form.role.data
        conf_info.location = conf_form.location.data
        conf_info.primary_attribution = conf_form.primary_attribution.data
        db.session.add(conf_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif commun_form.validate_on_submit():
        commun_info = Communications.query.filter_by(user_id=current_user.id).first()
        if commun_info is None:
            commun_info = Communications(user_id=current_user.id)
        commun_info.year = commun_form.year.data
        commun_info.number_lectures = commun_form.number_lectures.data
        commun_info.number_visits = commun_form.number_visits.data
        commun_info.number_media = commun_form.number_media.data
        db.session.add(commun_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif fund_ratio_form.validate_on_submit():
        fund_ratio_info = FundingRatio.query.filter_by(user_id=current_user.id).first()
        if fund_ratio_info is None:
            fund_ratio_info = FundingRatio(user_id=current_user.id)
        fund_ratio_info.year = fund_ratio_form.year.data
        fund_ratio_info.annual_spend = fund_ratio_form.annual_spend.data
        db.session.add(fund_ratio_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    elif public_eng_form.validate_on_submit():
        public_eng_info = PublicEngagement.query.filter_by(user_id=current_user.id).first()
        if public_eng_info is None:
            public_eng_info = PublicEngagement(user_id=current_user.id)
        public_eng_info.name = public_eng_form.name.data
        public_eng_info.start_date = public_eng_form.start_date.data
        public_eng_info.end_date = public_eng_form.end_date.data
        public_eng_info.activity_type = public_eng_form.activity_type.data
        public_eng_info.topic = public_eng_form.topic.data
        public_eng_info.target_area = public_eng_form.target_area.data
        public_eng_info.primary_attribution = public_eng_form.primary_attribution.data
        db.session.add(public_eng_info)
        db.session.add(current_user)
        db.session.commit()
        flash("Your changes have been saved")
        return redirect(url_for("edit_profile"))

    return render_template("edit_profile.html", title="Edit Profile", edu_form=edu_form, emp_form=emp_form,
                           prof_form=prof_form, img=svg, dist_form=dist_form, fund_form=fund_form,
                           team_form=team_form, impact_form=impact_form, inov_form=inov_form, public_form=public_form,
                           pres_form=pres_form, ac_form=ac_form, non_ac_form=non_ac_form, conf_form=conf_form,
                           commun_form=commun_form, fund_ratio_form=fund_ratio_form, public_eng_form=public_eng_form)


@app.route("/register", methods=["GET", "POST"])
def register():
    if not current_user.is_admin():
        flash("Admin area only")
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
        user.set_access(form.access.data)
        db.session.add(user)
        db.session.commit()
        msg = Message("Registration", sender = 'group8cs3305@gmail.com', recipients = [user.email])
        msg.body = "Thank you for registering an account with us. Please take the time to update your profile."
        mail.send(msg)
        flash("Succesfully Registered")
        return redirect(url_for("index"))
    return render_template("register.html", title="Register", form=form, img=svg)

@app.route("/account_application", methods=["GET", "POST"])
def account_application():
    if not current_user.access == 3:
        flash("Host Institution area only")
        return redirect(url_for("index"))
    form = RegisterForm()
    if form.validate_on_submit():
        if not form.validate_email(form.email):
            flash("Please enter a valid email")
            return redirect(url_for("register"))
        if not form.validate_username(form.username):
            flash("Username not valid")
            return redirect(url_for("register"))
        user = User(username=form.username.data, email=form.email.data, access=1)
        msg = Message("Account Application", sender = 'group8cs3305@gmail.com', recipients = [user.email])
        msg.body = "Thank you for applying for an account with us. Your application will be processed within 5 working days."
        mail.send(msg)
        flash("Successfully Applied for Account")
        return redirect(url_for("index"))
    return render_template("account_application.html", title="Account Application", form=form, img=svg)


@app.route("/makecall", methods=["GET", "POST"])
@login_required
def makecall():
    if not current_user.is_admin():
        flash("Admin area only")
        return redirect(url_for("index"))
    user = User.query.filter_by(id=current_user.id).first_or_404()
    form = CallsForProposalForm()
    if form.validate_on_submit():
        status = ""
        currentdate = datetime.now()
        startdate = str(form.start_date.data).replace("-", "")
        int(startdate)
        strdate = ""
        strdate += str(currentdate.year)
        strdate += str(currentdate.month)
        strdate += str(currentdate.day)
        if int(form.start_date.data.replace("-", "")) < int(strdate.replace("-", "")):
            status = "Inactive"
        else:
            status = "Active"
        call = Proposal(
            user_id=user.id,
            type_of_call=form.type_of_call.data,
            deadline=form.deadline.data,
            name=form.name.data,
            text_of_call=form.text_of_call.data,
            target_audience=form.target_audience.data,
            eligibility_criteria=form.eligibility_criteria.data,
            reporting_guidelines=form.reporting_guidelines.data,
            start_date=form.start_date.data,
            call_status=status,
            application_status=True
        )

        db.session.add(call)
        db.session.add(user)
        db.session.commit()
        flash("Succesfully published call")
        return redirect(url_for("index"))

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


@app.route('/profile/<user_id>')
@login_required
def profile(user_id):
    user = User.query.filter_by(id=user_id).first_or_404()
    access = user.get_access()
    proposals = Proposal.query.filter_by(user_id=user.id)
    return render_template('profile.html', user=user, img=svg, proposals=proposals, access=access)


@app.route("/workbench")
@login_required
def workbench():
    if not current_user.access == 1:
        flash("Area only for researchers")
        return redirect(url_for("index"))
    education_info = current_user.education_info.all()
    education_length = len(education_info)

    employment_info = current_user.employment.all()
    employment_length = len(employment_info)

    professional_studies = current_user.professional_studies.all()
    professional_studies_length = len(professional_studies)

    distinctions_and_awards = current_user.distinctions_and_awards.all()
    distinctions_and_awards_length = len(distinctions_and_awards)

    funding_diversification = current_user.funding_diversification.all()
    funding_diversification_length = len(funding_diversification)

    team_members = current_user.team_members.all()
    team_members_length = len(team_members)

    impacts = current_user.impacts.all()
    impacts_length = len(impacts)

    innovations = current_user.innovations.all()
    innovation_length = len(innovations)

    publications = current_user.publications.all()
    publications_length = len(publications)

    presentations = current_user.presentations.all()
    presentations_length = len(presentations)

    academic_collabs = current_user.academic_collabs.all()
    academic_collabs_length = len(academic_collabs)

    non_academic_collabs = current_user.non_academic_collabs.all()
    non_academic_collabs_length = len(non_academic_collabs)

    conferences = current_user.conferences.all()
    conferences_length = len(conferences)

    communications = current_user.communications.all()
    communications_length = len(communications)

    funding_ratio = current_user.funding_ratio.all()
    funding_ratio_length = len(funding_ratio)

    public_engagement = current_user.public_engagement.all()
    public_engagement_length = len(public_engagement)

    form = CallsForProposalFilter()
    proposal_info = Proposal.query.filter_by(application_status=True)
    return render_template("workbench.html", proposal_info=proposal_info, user=current_user, img=svg, edu_info=education_info, form=form,
                           edu_len=education_length, emp_info=employment_info, emp_len=employment_length,
                           prof_info=professional_studies, prof_len=professional_studies_length,
                           dist_info=distinctions_and_awards, dist_len=distinctions_and_awards_length,
                           fund_info=funding_diversification, fund_len=funding_diversification_length,
                           team_info=team_members, team_len=team_members_length, imp_info=impacts,
                           imp_len=impacts_length,
                           innov_info=innovations, innov_len=innovation_length, publications_info=publications,
                           publ_len=publications_length, pres_info=presentations,
                           pres_len=presentations_length, ac_info=academic_collabs, acad_len=academic_collabs_length,
                           non_ac_info=non_academic_collabs, non_ac_len=non_academic_collabs_length,
                           conf_info=conferences, confer_len=conferences_length, commun_info=communications,
                           commu_len=communications_length,
                           funding_ratio_info=funding_ratio, funding_rat_len=funding_ratio_length,
                           public_eng_info=public_engagement, public_eng_len=public_engagement_length)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/calls", methods=["GET", "POST"])
def calls():

    form = CallsForProposalFilter()
    proposal_info = Proposal.query.filter_by(application_status=True)

    return render_template("calls.html", title="Calls for Proposals", form=form, proposal_info=proposal_info, img=svg)


@app.route("/admin")
@login_required
def admin():
    if not current_user.is_admin():
        flash("Admin area only")
        return redirect(url_for("index"))
    return render_template("admin.html", title="Admin", img=svg)

@app.route("/reviewer")
@login_required
def reviewer():
    if not current_user.access == 4:
        flash("Reviewer area only")
        return redirect(url_for("index"))
    return render_template("reviewer.html", title="Reviewer", img=svg)

@app.route("/host_institution")
@login_required
def host_institution():
    if not current_user.access == 3:
        flash("Host Institution area only")
        return redirect(url_for("index"))
    return render_template("host_institution.html", title="Host Institution", img=svg)


@app.route("/assign_admin", methods=["GET", "POST"])
@login_required
def assign_admin():
    user = User.query.filter_by(username=current_user.username).first_or_404()

    if not user.is_admin():
        flash("No Permission for this area")
        return redirect(url_for("index"))

    form = UserSearchForm()

    return render_template("assign_admin.html", title="Assign Admin", form=form, img=svg)



@app.route("/proposal_application/<id>", methods=["GET", "POST"])
@login_required
def proposal_application(id):
    form = ApplicationForm()
    if not current_user.access == 1:
        flash("Area only for researchers")
        return redirect(url_for("index"))
    user = User.query.filter_by(username=current_user.username).first_or_404()
    proposal = Proposal.query.filter_by(id=id).first_or_404()
    if request.method == "POST":
        if form.accept.data == False:
            flash("Must accept terms and conditions")
            return redirect(url_for("proposal_application", id=id))
        app_info = Application(user_id=current_user.id)
        app_info.proposal_title = form.proposal_title.data
        app_info.award_duration = form.award_duration.data
        app_info.nrp = form.nrp.data
        app_info.legal_remit = form.legal_remit.data
        app_info.use_of_animals = form.use_of_animals.data
        app_info.use_of_humans = form.use_of_humans.data
        app_info.location = form.location.data
        if form.co_applicants.data:
            app_info.co_applicants = form.co_applicants.data
        app_info.abstract = form.abstract.data
        if "file" not in request.files:
            flash("No file part")
            return redirect(url_for("proposal_application", id=id))
        file = request.files["file"]
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == "":
            flash("No selected file")
            return redirect(url_for("proposal_application", id=id))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        app_info.path_to_file = file.filename
        app_info.proposal_id = proposal.id
        flash("You have successfully applied!")
        db.session.add(app_info)
        db.session.commit()
        return redirect(url_for("workbench"))
    return render_template("application.html", title="Proposal Application", img=svg, proposal=proposal, form = form)


@app.route("/accepted/<id>")
@login_required
def accepted(id):
    if not current_user.access == 2 and not current_user.access == 4:
        flash("Reviewer area only")
        return redirect(url_for("index"))

    application = Application.query.filter_by(id=id).first_or_404()
    winning_applicant = User.query.filter_by(id=application.user_id).first_or_404()
    proposal = Proposal.query.filter_by(id=application.proposal_id).first_or_404()
    proposal.application_status = False
    proposal.user_id = winning_applicant.id

    db.session.add(proposal)
    db.session.commit()

    msg = Message("Application", sender='group8cs3305@gmail.com', recipients=[winning_applicant.email])
    msg.body = "Thank you for applying. Your application has been accepted."
    mail.send(msg)

    flash("Application has been accepted. Notifying applicant.")
    return redirect(url_for("review_applications"))


@app.route("/rejected/<id>")
@login_required
def rejected(id):
    if not current_user.access == 2 and not current_user.access == 4:
        flash("Reviewer area only")
        return redirect(url_for("index"))
    application = Application.query.filter_by(id=id).first_or_404()
    applicant = User.query.filter_by(id=application.user_id).first_or_404()

    msg = Message("Application", sender='group8cs3305@gmail.com', recipients=[applicant.email])
    msg.body = "Thank you for applying. Unfortunately your application has been rejected."
    mail.send(msg)
    db.session.delete(application)
    db.session.commit()

    flash("Application has been rejected. Notifying applicant: %s at email: %s." % (applicant.username, applicant.email))
    return redirect(url_for("admin"))


@app.route("/modify/<id>")
@login_required
def modify(id):
    if not current_user.access == 2 and not current_user.access == 4:
        flash("Reviewer area only")
        return redirect(url_for("index"))
    application = Application.query.filter_by(id=id).first_or_404()
    applicant = User.query.filter_by(id=application.user_id).first_or_404()

    msg = Message("Application", sender='group8cs3305@gmail.com', recipients=[applicant.email])
    msg.body = "Thank you for applying. We are interested in your application but require some modification to it."
    mail.send(msg)

    flash("Application requires modification. Notifying applicant.")
    return redirect(url_for("review_applications"))

@app.route("/view_users")
@login_required
def view_users():
    if not current_user.is_admin():
        flash("Admin area only")
        return redirect(url_for("index"))
    users = User.query.all()

    return render_template("view_users.html", img=svg, title="View Users", users=users)

@app.route("/view_researchers")
@login_required
def view_researchers():
    if not current_user.access == 3:
        flash("Host Institution area only")
        return redirect(url_for("index"))
    education_info = EducationInfo.query.all()
    users = User
    #users = EducationInfo.query.filter_by(institution=institution)
    return render_template("view_researchers.html", svg=svg, title="View Researchers", users=users, education_info=education_info)

@app.route("/review_reports")
@login_required
def review_reports():
    if not current_user.access == 2 and not current_user.access == 4:
        flash("Reviewers area only")
        return redirect(url_for("index"))
    proposals = Proposal.query.filter_by(application_status=False)
    users = User

    return render_template("review_reports.html", proposals=proposals, img=svg, title="Review Reports", users=users)


@app.route("/annual_report_form/<proposal_id>", methods=["GET", "POST"])
@login_required
def annual_report_form(proposal_id):
    if not current_user.access == 1:
        flash("Researchers area only")
        return redirect(url_for("index"))
    form = AnnualReportForm()
    proposal = Proposal.query.filter_by(id=proposal_id).first()

    if form.validate_on_submit():
        annual_report_check = AnnualReport.query.filter_by(proposal_id=proposal_id).first()
        # if there is already a annual report submitted
        if not annual_report_check is None:
            flash("You have already submitted an Annual Report for the Grant: '%s'" % proposal.name)
            return redirect(url_for("profile", user_id=current_user.id))
        annual_report = AnnualReport(proposal_id=proposal_id)
        annual_report.deviations = form.deviations.data
        annual_report.research_highlights = form.research_highlights.data
        annual_report.challenges = form.challenges.data
        annual_report.planned_activities = form.planned_activities.data
        annual_report.employment = form.employment.data
        annual_report.education = form.education.data
        annual_report.professional_studies = form.professional_studies.data
        annual_report.distinction_and_awards = form.distinction_and_awards.data
        annual_report.funding_diversification = form.funding_diversification.data
        annual_report.team_members = form.team_members.data

        db.session.add(annual_report)
        db.session.commit()

        flash("Added your Annual Report! Thank You!")
        return redirect(url_for("index"))


    return render_template("annual_report.html", form=form, proposal_id=proposal_id, img=svg)

@app.route("/review_individual_reports/<id>")
@login_required
def review_individual_reports(id):
    if not current_user.access == 2 and not current_user.access == 4:
        flash("Reviewers area only")
        return redirect(url_for("index"))
    annual_report = AnnualReport.query.filter_by(proposal_id=id).first_or_404()
    return render_template("review_individual_reports.html", img=svg, title="Review Individual Reports",
                           annual_report=annual_report)

@app.route("/review_individual_apps/<id>")
@login_required
def review_individual_apps(id):
    if not current_user.access == 2 and not current_user.access == 4:
        flash("Reviewers area only")
        return redirect(url_for("index"))
    proposal = Proposal.query.filter_by(id=id).first_or_404()
    applications = proposal.applications.all()
    return render_template("review_individual_apps.html", img=svg, title="Review Individual Applications",
                           applications=applications)

@app.route("/review_applications")
@login_required
def review_applications():
    if not current_user.access == 2 and not current_user.access == 4:
        flash("Reviewers area only")
        return redirect(url_for("index"))
    proposals = Proposal.query.filter_by(application_status=True)
    return render_template("review_applications.html", img=svg, title="Proposals",
                           proposals=proposals)


# how to start venv: "source venv/bin/activate"

@app.route("/add_activity/<proposal_id>", methods=["GET", "POST"])
@login_required
def add_activity(proposal_id):
    if not current_user.access == 1:
        flash("Researchers area only")
        return redirect(url_for("index"))
    proposal = Proposal.query.filter_by(id=proposal_id).first_or_404()
    form = ActivityForm()
    if form.validate_on_submit():
        activity = Activity(proposal_id=proposal.id)
        activity.activity_title = form.activity_title.data
        activity.activity_body = form.activity_body.data
        db.session.add(activity)
        db.session.add(proposal)
        db.session.commit()
        flash("Activity Recorded")
        return redirect(url_for("profile", user_id=current_user.id))

    return render_template("add_activity.html", form=form, img=svg)


@app.route("/view_activities/<proposal_id>", methods=["GET", "POST"])
@login_required
def view_activities(proposal_id):
    proposal = Proposal.query.filter_by(id=proposal_id).first_or_404()
    activities = proposal.activities.all()

    return render_template("view_activities.html", activities=activities, img=svg)


@app.route("/education/<username>")
@login_required
def education(username):
    if not current_user.access == 1:
        flash("Researcher area only")
        return redirect(url_for("index"))
    user = User.query.filter_by(username=username).first()
    education_info = user.education_info
    return render_template("education.html", education_info=education_info, img=svg)


@app.route("/employment/<username>")
@login_required
def employment(username):
    if not current_user.access == 1:
        flash("Researcher area only")
        return redirect(url_for("index"))
    user = User.query.filter_by(username=username).first()
    employment = user.employment
    return render_template("employment.html", employment=employment, img=svg)


@app.route("/professional_studies/<username>")
@login_required
def professional_studies(username):
    if not current_user.access == 1:
        flash("Researcher area only")
        return redirect(url_for("index"))
    user = User.query.filter_by(username=username).first()
    professional_studies = user.professional_studies
    return render_template("professional_studies.html", professional_studies=professional_studies, img=svg)


@app.route("/distinctions_and_awards/<username>")
@login_required
def distinctions_and_awards(username):
    if not current_user.access == 1:
        flash("Researcher area only")
        return redirect(url_for("index"))
    user = User.query.filter_by(username=username).first()
    distinctions_and_awards = user.distinctions_and_awards
    return render_template("distinctions_and_awards.html", distinctions_and_awards=distinctions_and_awards, img=svg)


@app.route("/funding_diversification/<username>")
@login_required
def funding_diversification(username):
    if not current_user.access == 1:
        flash("Researcher area only")
        return redirect(url_for("index"))
    user = User.query.filter_by(username=username).first()
    funding_diversification = user.funding_diversification
    return render_template("funding_diversification.html", funding_diversification=funding_diversification, img=svg)


@app.route("/team_members/<username>")
@login_required
def team_members(username):
    if not current_user.access == 1:
        flash("Researcher area only")
        return redirect(url_for("index"))
    user = User.query.filter_by(username=username).first()
    team_members = user.team_members
    return render_template("team_members.html", team_members=team_members, img=svg)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow().strftime("%B %d %Y")
        db.session.commit()
