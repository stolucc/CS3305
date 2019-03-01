from flask import Flask, flash, request, redirect, url_for
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mimetypes
from flask_mail import Mail

#Makes Python treat the directories as cotaining python packages

UPLOAD_FOLDER = "/home/jack/PycharmProjects/CS3305/microblog/app/uploads"
ALLOWED_EXTENSIONS = set(["pdf"])

app = Flask(__name__)
app.config.from_object(Config)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
db = SQLAlchemy(app)


app.config['MAIL_SERVER'] = 'smtpgmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'group8cs3305@gmail.com'
app.config['MAIL_PASSWORD'] = 'Cat1234567'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
migrate = Migrate(app, db, mail)
login = LoginManager(app)
login.login_view = "login"

mimetypes.add_type('image/svg+xml', '.svg')

from app import routes, models
