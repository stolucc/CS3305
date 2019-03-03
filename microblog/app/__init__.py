from flask import Flask, flash, request, redirect, url_for
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mimetypes
from flask_mail_sendgrid import MailSendGrid

#Makes Python treat the directories as cotaining python packages

UPLOAD_FOLDER = "/home/jack/PycharmProjects/CS3305/microblog/app/uploads"
ALLOWED_EXTENSIONS = set(["pdf"])

app = Flask(__name__)
app.config.from_object(Config)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
app.config['MAIL_SENDGRID_API_KEY'] = ''
mail = MailSendGrid(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = "login"

mimetypes.add_type('image/svg+xml', '.svg')

from app import routes, models
