from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Use environment variables if set (for GitHub Actions), otherwise use default
    db_host = os.getenv('DB_HOST', 'Timpa.local')
    db_user = os.getenv('DB_USER', 'dbadm')
    db_password = os.getenv('DB_PASSWORD', 'P%40ssw0rd')
    db_name = os.getenv('DB_NAME', 'ormdatabase')
    
    app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
