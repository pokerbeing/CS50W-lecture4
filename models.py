
# Maps object-oriented Python programming to a SQL database

from flask_sqlalchemy import SQLAlchemy   # Uses Flask library

db = SQLAlchemy()

class Flight(db.Model):     # Class inherits from db.Model SQLAlchemy class
    __tablename__ = "flights"  # Refers to SQL table name
    id = db.Column(db.Integer, primary_key=True)  
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
