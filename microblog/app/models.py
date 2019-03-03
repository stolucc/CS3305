from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Loads posts and users from the database

ACCESS = {
    "guest": 0,
    "researcher": 1,
    "admin": 2,
    "host institution": 3,
    "reviewer": 4
}


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    access = db.Column(db.Integer)
    proposals = db.relationship('Proposal', backref='author', lazy='dynamic')
    education_info = db.relationship("EducationInfo", backref="author", lazy="dynamic")
    employment = db.relationship("Employment", backref="author", lazy="dynamic")
    professional_studies = db.relationship("ProfessionalStudies", backref="author", lazy="dynamic")
    distinctions_and_awards = db.relationship("DistinctionsAndAwards", backref="author", lazy="dynamic")
    funding_diversification = db.relationship("FundingDiversification", backref="author", lazy="dynamic")
    team_members = db.relationship("TeamMembers", backref="author", lazy="dynamic")
    impacts = db.relationship("Impacts", backref="author", lazy="dynamic")
    innovations = db.relationship("Innovation", backref="author", lazy="dynamic")
    publications = db.relationship("Publication", backref="author", lazy="dynamic")
    presentations = db.relationship("Presentation", backref="author", lazy="dynamic")
    academic_collabs = db.relationship("AcademicCollabs", backref="author", lazy="dynamic")
    non_academic_collabs = db.relationship("NonAcademicCollabs", backref="author", lazy="dynamic")
    conferences = db.relationship("Conference", backref="author", lazy="dynamic")
    communications = db.relationship("Communications", backref="author", lazy="dynamic")
    funding_ratio = db.relationship("FundingRatio", backref="author", lazy="dynamic")
    public_engagement = db.relationship("PublicEngagement", backref="author", lazy="dynamic")

    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.String(20), default=datetime.utcnow().strftime("%B %d %Y"))

    def __repr__(self):
        return "<User {}>".format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.access == 2

    def allowed(self, access_level):
        return self.access >= access_level

    def set_access(self, access_string):
        value = ACCESS[access_string]
        self.access = value

    def get_access(self):
        for acc in ACCESS:
            if self.access == ACCESS[acc]:
                return acc


class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applications = db.relationship("Application", backref="author", lazy="dynamic")
    name = db.Column(db.String(140))
    activities = db.relationship("Activity", backref="author", lazy="dynamic")
    annual_report = db.relationship("AnnualReport", backref="author", lazy="dynamic")
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    deadline = db.Column(db.String(20))
    text_of_call = db.Column(db.String(500))
    target_audience = db.Column(db.String(50))
    eligibility_criteria = db.Column(db.String(100))
    # award duration by calculating difference between start date and end date'
    reporting_guidelines = db.Column(db.String(150))
    start_date = db.Column(db.String(20))
    type_of_call = db.Column(db.String(40))
    call_status = db.Column(db.String(20))
    application_status = db.Column(db.Boolean())

    def __repr__(self):
        return "<Proposal {}>".format(self.name)


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey("proposal.id"))
    activity_title = db.Column(db.String(100))
    activity_body = db.Column(db.String(400))


class AnnualReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey("proposal.id"))
    deviations = db.Column(db.String(200))
    research_highlights = db.Column(db.String(400))
    challenges = db.Column(db.String(400))
    planned_activities = db.Column(db.String(500))


class Application(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    proposal_id = db.Column(db.Integer, db.ForeignKey("proposal.id"))
    id = db.Column(db.Integer, primary_key=True)
    path_to_file = db.Column(db.String(30))


class EducationInfo(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(40))
    field_of_study = db.Column(db.String(120))
    institution = db.Column(db.String(120))
    location = db.Column(db.String(120))
    year_of_degree = db.Column(db.String(20))

    def __repr__(self):
        return "Degree: {}".format(self.degree)


class Employment(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(60))
    location = db.Column(db.String(120))
    years = db.Column(db.String(10))


class ProfessionalStudies(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.String(12))
    end_date = db.Column(db.String(12))
    society_name = db.Column(db.String(40))
    member_type = db.Column(db.String(40))
    status = db.Column(db.String(10))


class DistinctionsAndAwards(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(4))
    awarding_body = db.Column(db.String(60))
    award_details = db.Column(db.String(120))
    member_name = db.Column(db.String(40))


class FundingDiversification(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.String(12))
    end_date = db.Column(db.String(12))
    funding_amt = db.Column(db.Integer)
    funding_body = db.Column(db.String(60))
    funding_program = db.Column(db.String(60))


class TeamMembers(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    position_in_team = db.Column(db.String(120))
    other_users = db.Column(db.String(120))
    start_date = db.Column(db.String(12))
    end_date = db.Column(db.String(12))


class Impacts(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    category = db.Column(db.String(40))
    primary_beneficiary = db.Column(db.String(40))
    primary_attribution = db.Column(db.String(40))


class Innovation(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    innovation_type = db.Column(db.String(40))
    title = db.Column(db.String(60))
    primary_attribution = db.Column(db.String(40))


class Publication(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    publication_type = db.Column(db.String(40))
    title = db.Column(db.String(60))
    primary_attribution = db.Column(db.String(40))
    journal_name = db.Column(db.String(50))
    status = db.Column(db.String(20))
    doi = db.Column(db.String(50))


class Presentation(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    event_type = db.Column(db.String(40))
    title = db.Column(db.String(60))
    primary_attribution = db.Column(db.String(40))
    organising_body = db.Column(db.String(40))
    location = db.Column(db.String(30))


class AcademicCollabs(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DATE())
    end_date = db.Column(db.DATE())
    institution = db.Column(db.String(50))
    department = db.Column(db.String(40))
    location = db.Column(db.String(30))
    collaborator = db.Column(db.String(40))
    collaborator_goal = db.Column(db.String(50))
    interaction_freq = db.Column(db.String(20))
    primary_attribution = db.Column(db.String(40))


class NonAcademicCollabs(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DATE())
    end_date = db.Column(db.DATE())
    institution = db.Column(db.String(50))
    department = db.Column(db.String(40))
    location = db.Column(db.String(30))
    collaborator = db.Column(db.String(40))
    collaborator_goal = db.Column(db.String(50))
    interaction_freq = db.Column(db.String(20))
    primary_attribution = db.Column(db.String(40))


class Conference(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DATE())
    end_date = db.Column(db.DATE())
    title = db.Column(db.String(50))
    event_type = db.Column(db.String(40))
    role = db.Column(db.String(40))
    location = db.Column(db.String(30))
    primary_attribution = db.Column(db.String(40))


class Communications(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    number_lectures = db.Column(db.Integer)
    number_visits = db.Column(db.Integer)
    number_media = db.Column(db.Integer)


class FundingRatio(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    annual_spend = db.Column(db.String(50))


class PublicEngagement(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))
    topic = db.Column(db.String(50))
    activity_type = db.Column(db.String(40))
    target_area = db.Column(db.String(20))
    primary_attribution = db.Column(db.String(40))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
