from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# Loads posts and users from the database

ACCESS = {
    "guest" : 0,
    "user" : 1,
    "admin" : 2
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
    innovations = db.relationship("Innovation",backref="author", lazy="dynamic")
    publications = db.relationship("Publication", backref="author", lazy="dynamic")
    presentations = db.relationship("Presentation", backref="author", lazy="dynamic")
    academiccollabs = db.relationship("AcademicCollabs", backref="author", lazy="dynamic")
    nonacademiccollabs = db.relationship("NonAcademicCollabs", backref="author",lazy="dynamic")
    conferences = db.relationship("Conference", backref="author", lazy="dynamic")
    communications = db.relationship("Communications",backref="author",lazy="dynamic")
    funding_ratio = db.relationship("FundingRatio", backref="author",lazy="dynamic")
    public_engagement = db.relationship("PublicEngagement", backref="author",lazy="dynamic")

    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())

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


class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    deadline = db.Column(db.DATE)
    text_of_call = db.Column(db.String(500))
    target_audience = db.Column(db.String(50))
    eligibility_criteria = db.Column(db.String(100))
    # award duration by calculating difference between start date and end date'
    reporting_guidelines = db.Column(db.String(150))
    start_date = db.Column(db.DATE)

    def __repr__(self):
        return "<Proposal {}>".format(self.name)


class Application(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(15))


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
    impact_title = db.Column(db.String(60))
    impact_category = db.Column(db.String(40))
    primary_beneficiary = db.Column(db.String(40))
    primary_attribution = db.Column(db.String(40))


class Innovation(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    type = db.Column(db.String(40))
    title = db.Column(db.String(60))
    primary_attribution = db.Column(db.String(40))


class Publication(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    type = db.Column(db.String(40))
    title = db.Column(db.String(60))
    primary_attribution = db.Column(db.String(40))
    journal_conf_name = db.Column(db.String(50))
    status = db.Column(db.String(20))
    doi = db.Column(db.String(50))


class Presentation(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    type = db.Column(db.String(40))
    title = db.Column(db.String(60))
    primary_attribution = db.Column(db.String(40))
    organising_body = db.Column(db.String(40))
    location = db.Column(db.String(30))


class AcademicCollabs(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DATE())
    end_date = db.Column(db.DATE())
    name = db.Column(db.String(50))
    department = db.Column(db.String(40))
    location = db.Column(db.String(30))
    collaborator = db.Column(db.String(40))
    goal = db.Column(db.String(50))
    interaction_freq = db.Column(db.String(20))
    primary_attribution = db.Column(db.String(40))


class NonAcademicCollabs(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DATE())
    end_date = db.Column(db.DATE())
    name = db.Column(db.String(50))
    department = db.Column(db.String(40))
    location = db.Column(db.String(30))
    collaborator = db.Column(db.String(40))
    goal = db.Column(db.String(50))
    interaction_freq = db.Column(db.String(20))
    primary_attribution = db.Column(db.String(40))


class Conference(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DATE())
    end_date = db.Column(db.DATE())
    title = db.Column(db.String(50))
    type = db.Column(db.String(40))
    role = db.Column(db.String(40))
    location = db.Column(db.String(30))
    primary_attribution = db.Column(db.String(40))


class Communications(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    num_of_lecs_demos = db.Column(db.Integer)
    num_of_visits = db.Column(db.Integer)
    num_of_interactions = db.Column(db.Integer)


class FundingRatio(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    percentage = db.Column(db.Integer)


class PublicEngagement(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DATE())
    end_date = db.Column(db.DATE())
    topic = db.Column(db.String(50))
    type = db.Column(db.String(40))
    target_area = db.Column(db.String(20))
    primary_attribution = db.Column(db.String(40))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
