# Takes object definition from models.py and creates the corresponding SQL tables

import os

from flask import Flask, render_template, request

# Import table configuration from models.py
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db defined as SQLAlchemy database in models.py
db.init_app(app)

def main():
    # Command to create SQL tables
    db.create_all()

if __name__ == "__main__":
    # For command line vs. web originated commands
    with app.app_context():
        main()
