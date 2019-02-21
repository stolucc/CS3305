from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mimetypes
from flask_mail import Mail

#Makes Python treat the directories as cotaining python packages

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = "login"

mimetypes.add_type('image/svg+xml', '.svg')

from app import routes, models
