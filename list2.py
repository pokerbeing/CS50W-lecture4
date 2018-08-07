import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    # Equivalent to the SQL SELECT * command
    flights = Flight.query.order_by(Flight.origin).all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    print("\nDescending destinations")
    flights = Flight.query.order_by(Flight.destination.desc()).all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")        

    print("\nExclude paris")
    flights = Flight.query.filter(Flight.origin!='Paris').all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")        

    print("\nLike %n%")
    flights = Flight.query.filter(Flight.origin.like("%n%")).all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")


    
if __name__ == "__main__":
    with app.app_context():
        main()
