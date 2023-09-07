from flask_login import UserMixin
from __init__ import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    role = db.Column(db.String(1000))
    age = db.Column(db.Integer)
    address = db.Column(db.String(1000))
    registration = db.Column(db.String(1000))
    gender = db.Column(db.String(1000))
    profile_picture = db.Column(db.String(1000))
    about_me = db.Column(db.String(1000))
    phone = db.Column(db.String(100))
    major = db.Column(db.String(100))
    register_date = db.Column(db.Date)
    year = db.Column(db.Integer)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    student_id = db.Column(db.Integer)
    month_paid = db.Column(db.Date)
    payment_date = db.Column(db.Date)
    amount = db.Column(db.Float)
    status = db.Column(db.String(1000))
    type = db.Column(db.String(1000))

class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    grade = db.Column(db.Float)
    subject = db.Column(db.String(1000))
    grade_date = db.Column(db.Date)

class Major(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    major_name = db.Column(db.String(100))
    duration = db.Column(db.Float)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg_from = db.Column(db.Integer)
    msg_to = db.Column(db.Integer)
    content = db.Column(db.String(1000))
    date_sent = db.Column(db.Date)

class Absence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer)
    date_absence = db.Column(db.DateTime)
    justified = db.Column(db.String(10))
    details = db.Column(db.String(1000))

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    id_prof = db.Column(db.Integer)
