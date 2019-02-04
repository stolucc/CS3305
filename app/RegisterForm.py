from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,Boolean Field, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequire()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirmpass = PasswordField("Confirm_Password", validators=[DataRequired()])
    submit = SubmitField("Register")
    def validate_passwordmatch(self,password,confirmpass):
        pass1 = password.data
        pass2 = confirmpass.data
        if pass1 != pass2:
            raise ValidationError("Please make sure the passwords match")

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Please use a different username")
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address.")
