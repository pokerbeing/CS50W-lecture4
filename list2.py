import os

from flask import Flask, render_template, request
from models import *
from sqlalchemy import or_, and_

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():

    passenger = Passenger(name="Larry", flight_id=1)
    db.session.add(passenger)
    db.session.commit()
    
    
    
    # Equivalent to the SQL SELECT * command
    flights = Flight.query.filter_by(origin="Paris").all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")


    print("\nAscending destinations")
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

    print("\n in")
    flights = Flight.query.filter(Flight.origin.in_(["Tokyo", "Paris"])).all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    print("\n compound boolean expression and_")
    flights = Flight.query.filter(and_(Flight.origin == "Paris",
             Flight.duration > 500)).all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    print("\n compound boolean expression or_")
    flights = Flight.query.filter(or_(Flight.origin == "Paris",
             Flight.duration > 500)).all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    print("\n compound boolean expression or_")
    flights = Flight.query.filter(or_(Flight.origin == "Paris",
             Flight.duration > 500)).all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

    print("\n JOIN")
    query = (db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all())
    for each in query:
        print(f"{flight.origin} {flight.destination} {passenger.name}")

if __name__ == "__main__":
    with app.app_context():
        main()
