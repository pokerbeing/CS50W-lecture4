
# Translation of import.py which uses ORM to perform import
# instead of straight SQL commands

import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    # Loop over every record in CSV reader
    for origin, destination, duration in reader:
        # Note that syntax eliminates the need to placeholders
        flight = Flight(origin=origin, destination=destination, duration=duration)
        # Adds the instantiated object flight to the db 
        db.session.add(flight)
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
