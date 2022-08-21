from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

from config import Configuration



# Create flask application
api = Flask(__name__)

# Load application configuration
api.config.from_object(Configuration)

db = SQLAlchemy(api)

# Enable db/application migration
migrate = Migrate(api, db, render_as_batch=True)


from core import views

