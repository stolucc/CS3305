from datetime import date

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, Length
import re
from app.models import User


# Create the fields for every form, with validation methods for the register form.
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class EditProfileForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    about_me = TextAreaField("About me", validators=[Length(min=0, max=140)])
    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    access = SelectField('Access Type',
                         choices=[('researcher', 'Researcher'),
                                  ('admin', 'Admin'),
                                  ('host institution', 'Host Intitution'),
                                  ('reviewer', 'Reviewer')])
    password = PasswordField("Password", validators=[DataRequired()])
    confirmpass = PasswordField("Confirm_Password", validators=[DataRequired()])
    submit = SubmitField("Register")

    def validate_password(self, password):
        password = str(password)
        if re.findall("[A-Z]", password) and re.findall("[a-z]", password) and re.findall("0-9", password) and len(
                password) > 8:
            return True
        return False

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


class ApplicationForm(FlaskForm):
    proposal_title = StringField("Proposal Title", validators=[DataRequired()])
    award_duration = StringField("Duration of Award", validators=[DataRequired()])
    nrp = SelectField("National Research Priority (NRP) Area", choices=[('Priority Area A', 'Priority Area A - Future Networks & Communications'),
                                                                        ("Priority Area B", "Priority Area B - Data Analytics, Management, Security & Privacy"),
                                                                        ("Priority Area C", "Priority Area C - Digital Platforms, Content & Applications"),
                                                                        ("Priority Area D", "Priority Area D - Connected Health and Independent Living"),
                                                                        ("Priority Area E", "Priority Area E - Medical Devices"),
                                                                        ("Priority Area F", "Priority Area F - Diagnostics"),
                                                                        ("Priority Area G", "Priority Area G - Therapeutics: Synthesis, Formulation, Processing and Drug Delivery"),
                                                                        ("Priority Area H", "Priority Area H - Food for Health"),
                                                                        ("Priority Area I", "Priority Area I - Sustainable Food Production and Processing"),
                                                                        ("Priority Area J", "Priority Area J - Marine Renewable Energy"),
                                                                        ("Priority Area K", "Priority Area K - Smart Grids & Smart Cities"),
                                                                        ("Priority Area L", "Priority Area L - Manufacturing Competitiveness"),
                                                                        ("Priority Area M", "Priority Area M - Processing Technologies and Novel Materials"),
                                                                        ("Priority Area N", "Priority Area N - Innovation in Servics and Business Processes"),
                                                                        ("Software", "Software"),
                                                                        ("Other", "Other")
                                            ])
    legal_remit = StringField("Please describe how your proposal is aligned with SFI's legal remit (max 250 words)",
                              validators = [DataRequired()])
    use_of_animals = BooleanField("This application involves the use of animals", validators=[DataRequired()])
    use_of_humans = BooleanField("This applications involves the use of human participants, human biological material, or identifiable data",
                                 validators=[DataRequired()])
    location = StringField("Location at time of submission", validators=[DataRequired()])
    co_applicants = StringField("Co-applicants", [DataRequired()])
    abstract = StringField("Lay abstract", validators=[DataRequired()])
    accept = BooleanField("I accept these terms", validators=[DataRequired()])
    submit = SubmitField("Apply")


class EducationForm(FlaskForm):
    degree = StringField("Degree", validators=[DataRequired()])
    field_of_study = StringField("Field of Study", validators=[DataRequired()])
    institution = StringField("Institution", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    year_awarded = StringField("Year of Degree Awarded", validators=[DataRequired()])
    submit = SubmitField("Save Education Info")


class ActivityForm(FlaskForm):
    activity_title = StringField("Activity Title", validators=[DataRequired()])
    activity_body = StringField("Activity Body", validators=[DataRequired()])
    submit = SubmitField("Save your activities")


class AnnualReportForm(FlaskForm):
    deviations = StringField("Deviations from original Research Plan", validators=[DataRequired()])
    research_highlights = StringField("3 most important research highlights", validators=[DataRequired()])
    challenges = StringField("Challenges you encountered", validators=[DataRequired()])
    planned_activities = StringField("Planned activities for the coming year", validators=[DataRequired()])
    education = BooleanField("Education")
    employment = BooleanField("Employment")
    professional_studies = BooleanField("Professional Studies")
    distinction_and_awards = BooleanField("Distinction and Awards")
    funding_diversification = BooleanField("Funding Diversification")
    team_members = BooleanField("Team Members")
    submit = SubmitField("Save Annual Report")


class EmploymentForm(FlaskForm):
    institution = StringField("Institution/Company", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    years = StringField("Years", validators=[DataRequired()])
    submit = SubmitField("Save Employment Info")


class ProfessionalStudiesForm(FlaskForm):
    start_date = StringField("Start Date", validators=[DataRequired()])
    end_date = StringField("End Date", validators=[DataRequired()])
    society = StringField("Name of Society", validators=[DataRequired()])
    membership = StringField("Type of Membership", validators=[DataRequired()])
    status = StringField("Status (e.g active)", validators=[DataRequired()])
    submit = SubmitField("Save Professional Studies Info")


class DistinctionsAndAwardsForm(FlaskForm):
    year = StringField("Year", validators=[DataRequired()])
    awarding_body = StringField("Awarding Body", validators=[DataRequired()])
    award_details = StringField("Details of Award", validators=[DataRequired()])
    member_name = StringField("Team Member Name", validators=[DataRequired()])
    submit = SubmitField("Save Distinctions And Awards Info")


class FundingDiversificationForm(FlaskForm):
    start_date = StringField("Start Date", validators=[DataRequired()])
    end_date = StringField("End Date", validators=[DataRequired()])
    funding_amount = StringField("Amount of Funding", validators=[DataRequired()])
    funding_body = StringField("Funding Body", validators=[DataRequired()])
    funding_program = StringField("Funding Programme", validators=[DataRequired()])
    submit = SubmitField("Save Funding Info")


class TeamMembersForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    position_in_team = StringField("Position within the Team", validators=[DataRequired()])
    start_date = StringField("Start Date with Team", validators=[DataRequired()])
    departure_date = StringField("Departure Date", validators=[DataRequired()])
    other_users = StringField("Other Users on Team", validators=[DataRequired()])
    submit = SubmitField("Save Team Members Info")


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
                                choices=[('open', 'Open'),
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


class CallsForProposalForm(FlaskForm):
    type_of_call = SelectField('Call Type',
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
    deadline = StringField("Deadline", validators=[DataRequired()])
    name = StringField("Call Name", validators=[DataRequired()])
    text_of_call = StringField("Text of call", validators=[DataRequired()])
    target_audience = StringField("Target Audience", validators=[DataRequired()])
    eligibility_criteria = StringField("Eligibility Criteria", validators=[DataRequired()])
    # duration of award can be acquired through calculating difference between deadline and current date
    reporting_guidelines = StringField("Reporting Guidelines", validators=[DataRequired()])
    start_date = StringField("Start Date", validators=[DataRequired()])
    submit = SubmitField("Submit Proposal")


class UserSearchForm(FlaskForm):
    search = StringField("Search for users")
    submit = SubmitField("Search")
