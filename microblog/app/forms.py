from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email

from app.models import User

#Create the fields for every form, with validation methods for the register form.

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirmpass = PasswordField("Confirm_Password", validators=[DataRequired()])
    submit = SubmitField("Register")


    def validate_passwordmatch(self, password, confirmpass):
        pass1 = password.data
        pass2 = confirmpass.data
        if pass1 != pass2:
            return False
        return True


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            return False
        return True

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            return False
        return True


class EducationForm(FlaskForm):
    degree = StringField("Degree", validators=[DataRequired()])
    field_of_study = PasswordField("Field of Study", validators=[DataRequired()])
    institution = StringField("Institution", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    year_awarded = StringField("Year of Degree Awarded", validators=[DataRequired()])
    submit = SubmitField("Save")


class Employment(FlaskForm):
    institution = StringField("Institution/Company", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    years = StringField("Years", validators=[DataRequired()])
    submit = SubmitField("Save")


class ProfessionalSocietiesForm(FlaskForm):
    start_date = StringField("Start Date", validators=[DataRequired()])
    end_date = StringField("End Date", validators=[DataRequired()])
    society = StringField("Name of Society", validators=[DataRequired()])
    membership = StringField("Type of Membership", validators=[DataRequired()])
    status = StringField("Status (e.g active)", validators=[DataRequired()])
    submit = SubmitField("Save")


class DistinctionsAwardsForm(FlaskForm):
    year = StringField("Year", validators=[DataRequired()])
    awarding_body = StringField("Awarding Body", validators=[DataRequired()])
    award_details = StringField("Details of Award", validators=[DataRequired()])
    member_name = StringField("Team Member Name", validators=[DataRequired()])
    submit = SubmitField("Save")


class FundingForm(FlaskForm):
    start_date = StringField("Start Date", validators=[DataRequired()])
    end_date = StringField("End Date", validators=[DataRequired()])
    funding_amount = StringField("Amount of Funding", validators=[DataRequired()])
    funding_body = StringField("Funding Body", validators=[DataRequired()])
    fudning_programme = StringField("Funding Programme", validators=[DataRequired()])
    status = StringField("Status (e.g Active)", validators=[DataRequired()])
    primary_attribution = StringField("Primary Attribution", validators=[DataRequired()])
    submit = SubmitField("Save")


class TeamMembersForm(FlaskForm):
    start_date = StringField("Start Date with Team", validators=[DataRequired()])
    departure_date = StringField("Departure Date", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    position_in_team = StringField("Position within the Team", validators=[DataRequired()])
    primary_attribution = StringField("Primary Attribution", validators=[DataRequired()])
    submit = SubmitField("Save")


class ImpactsForm(FlaskForm):
    title = StringField("Impact Title", validators=[DataRequired()])
    category = StringField("Impact Category", validators=[DataRequired()])
    primary_beneficiary = StringField("Primary Beneficiary", validators=[DataRequired()])
    primary_attribution = StringField("Primary Attribution", validators=[DataRequired()])
    submit = SubmitField("Save")


class InovationForm(FlaskForm):
    year = StringField("Year", validators=[DataRequired()])
    innovation_type = StringField("Type", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    primary_attribution = StringField("Primary Attribution", validators=[DataRequired()])
    submit = SubmitField("Save")


class PublicationsForm(FlaskForm):
    year = StringField("Publication Year", validators=[DataRequired()])
    publication_type = SelectField('Publication Type',
                                   choices=[('original', 'Refereed Original Article'),
                                            ('review', 'Refereed Review Article'),
                                            ('conference', 'Refereed Conference Paper'), ('book', 'Book'),
                                            ('report', 'Technical Report')])
    title = StringField("Title", validators=[DataRequired()])
    journal_name = StringField("Journal/Conference Name", validators=[DataRequired()])
    status = SelectField('Publication Status',
                         choices=[('active', 'Active'), ('expired', 'Expired')])
    doi = StringField("DOI", validators=[DataRequired()])
    primary_attribution = StringField("Primary Attribution", validators=[DataRequired()])
    submit = SubmitField("Save")


class PresentationsForm(FlaskForm):
    year = StringField("Year", validators=[DataRequired()])
    title = StringField("Title of Presentation", validators=[DataRequired()])
    event_type = SelectField('Event Type',
                             choices=[('conference', 'Conference'), ('seminar', 'Invited Seminar'),
                                      ('keynote', 'Keynote')])
    organising_body = StringField("Organising Body", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    primary_attribution = StringField("Primary Attribution", validators=[DataRequired()])
    submit = SubmitField("Save")


class AcademicColabForm(FlaskForm):
    start_date = StringField("Start Date", validators=[DataRequired()])
    end_date = StringField("End Date", validators=[DataRequired()])
    institution = StringField("Name of Institution", validators=[DataRequired()])
    department = StringField("Department within Institution", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    collaborator = StringField("Name of Collaborations", validators=[DataRequired()])
    collaborator_goal = SelectField('Primary Goal of Collaborator',
                                    choices=[('access', 'Access to Software/Data/Material/Equipment'),
                                             ('training', 'Training and Career Development'),
                                             ('publication', 'Joint Publication'), ('startup', 'Startup Development'),
                                             ('license', 'License Development'),
                                             ('building_networks', 'Building Networks/Relationships')])
    interaction_freq = StringField("Frequency of Interactions", validators=[DataRequired()])
    primary_attribution = StringField("Primary Attribution", validators=[DataRequired()])
    submit = SubmitField("Save")


class NonAcademicColabForm(FlaskForm):
    start_date = StringField("Start Date", validators=[DataRequired()])
    end_date = StringField("End Date", validators=[DataRequired()])
    institution = StringField("Name of Institution", validators=[DataRequired()])
    department = StringField("Department within Institution", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    collaborator = StringField("Name of Collaborations", validators=[DataRequired()])
    collaborator_goal = SelectField('Primary Goal of Collaborator',
                                    choices=[('access', 'Access to Software/Data/Material/Equipment'),
                                             ('training', 'Training and Career Development'),
                                             ('publication', 'Joint Publication'), ('startup', 'Startup Development'),
                                             ('license', 'License Development'),
                                             ('building_networks', 'Building Networks/Relationships')])
    interaction_freq = StringField("Frequency of Interactions", validators=[DataRequired()])
    primary_attribution = StringField("Primary Attribution", validators=[DataRequired()])
    submit = SubmitField("Save")


class ConferencesForm(FlaskForm):
    start_date = StringField("Start Date", validators=[DataRequired()])
    end_date = StringField("End Date", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    event_type = SelectField('Event Type',
                             choices=[('conference', 'Conference'), ('workshop', 'Workshop'), ('seminar', 'Seminar')])
    role = StringField("Role", validators=[DataRequired()])
    location = StringField("Location of Event", validators=[DataRequired()])
    primary_attribution = StringField("Primary Attribution", validators=[DataRequired()])
    submit = SubmitField("Save")


class CommunicationsForm(FlaskForm):
    year = StringField("Year", validators=[DataRequired()])
    number_lectures = StringField("Number of Public Lectures/Demonstrations", validators=[DataRequired()])
    number_visits = StringField("Number of Visits", validators=[DataRequired()])
    number_media = StringField("Number of Media Interactions", validators=[DataRequired()])
    submit = SubmitField("Save")


class FundingRatioForm(FlaskForm):
    year = StringField("Year", validators=[DataRequired()])
    annual_spend = SelectField('Annual Spend',
                               choices=[('twenty', '0-20'), ('forty', '21-40'), ('sixty', '41-61'), ('eighty', '61-81'),
                                        ('hundred', '81-100')])
    submit = SubmitField("Save")


class PublicEngagementForm(FlaskForm):
    name = StringField("Name of Project", validators=[DataRequired()])
    start_date = StringField("Start Date", validators=[DataRequired()])
    end_date = StringField("End Date", validators=[DataRequired()])
    activity_type = SelectField('Activity Type',
                                choices=[('public_event', 'Public Event'), ('in_class', 'In-Class Activities'),
                                         ('experience_programme', 'Career Experience Programme'), ('other', 'Other')])
    topic = SelectField('Project Topic',
                        choices=[('science', 'Science'), ('math', 'Math'), ('engineering', 'Engineering'),
                                 ('technology', 'Technology'), ('space_related', 'Space Related'), ('other', 'Other')])
    target_area = SelectField('Target Geographical Area',
                              choices=[('local', 'Local (specify County)'), ('national', 'National'),
                                       ('international', 'International')])
    primary_attribution = StringField("Primary Attribution", validators=[DataRequired()])
    submit = SubmitField("Save")


class CallsForProposalFilter(FlaskForm):
    deadline_type = SelectField('Deadline',
                                choices=[('deadline', 'Deadline'), ('open', 'Open'),
                                         ('closed', 'Closed'), ('other', 'Other')])
    call_type = SelectField('Call Type',
                            choices=[('funding', 'Funding Oppurtunities'), ('conference', 'Conference/Workshop'),
                                     ('early', 'Early/Mid Career Investigator Led'),
                                     ('education', 'Education and Public management'),
                                     ('entrepreneur', 'Entrepreneurship'),
                                     ('established', 'Established Investigator Led'),
                                     ('european', 'European Oppurtunities'), ('industry', 'Industry Facing'),
                                     ('infrastructure', 'Infrastructure'), ('policy', 'Policy'),
                                     ('recruitment', 'Recruitment Only'),
                                     ('partnerships', 'SFI Partnerships'), ('centres', 'SFI Research Centres'),
                                     ('other', 'Other')])
    submit = SubmitField("Filter")


class ApplicationForm(FlaskForm):
    fname = StringField("Funding Name", validators=[DataRequired()])
    proposal = StringField("Title of Proposal", validators=[DataRequired()])
    lead_name = StringField("Full Name of Lead Investigators", validators=[DataRequired()])
    co_name = StringField("Full Name of Co-Investigator(s)", validators=[DataRequired()])
    research = StringField("Research Body", validators=[DataRequired()])
    co_commit = StringField("Percentage Co-Investigator Commitment", validators=[DataRequired()])
    lead_commit = StringField("Percentage Lead Investigator Commitment", validators=[DataRequired()])
    budget = StringField("Total Requested SFI Budget", validators=[DataRequired()])
    start_date = StringField("Requested Starting Date", validators=[DataRequired()])
    duration = StringField("Proposed Duration", validators=[DataRequired()])
    submit = SubmitField("Apply")
