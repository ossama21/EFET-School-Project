from flask import Blueprint, render_template, flash, g, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import create_app
from models import User, Payment, Grade, Major, Message, Absence, Subject
import sqlite3
from __init__ import db


def connect_db():
    sql = sqlite3.connect('./instance/db.sqlite')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    #Check if DB is there
    if not hasattr(g, 'sqlite3'):
        g.sqlite3_db = connect_db()
    return g.sqlite3_db

def get_all_payments(student_id):
    db = get_db()
    #create table payment(id integer primary key autoincrement, student_id integer, month_paid date, payment_date date, amount float, status text)
    cursor = db.execute(f"select p.id, p.student_id, p.month_paid, p.payment_date, p.amount, p.status, p.type, u.name from payment p INNER JOIN user u ON p.student_id=u.id where p.student_id = {student_id}")
    results = cursor.fetchall()
    return results

def get_student_infos(student_id):
    user = User.query.filter_by(id=student_id).first()
    return user

def get_all_users():
    users = User.query.all()
    return users

def get_all_students():
    users = User.query.filter_by(role='student')
    return users

def get_all_grades(student_id):
    # this function retrieves student's grades from table Grade
    grades = Grade.query.filter_by(student_id=student_id)
    return grades

def get_all_majors():
    db = get_db()
    cursor = db.execute(f"SELECT major.id, major.major_name AS major_name, duration, COUNT(user.id) AS number_students FROM major LEFT JOIN user ON major.major_name = user.major GROUP BY major.major_name ORDER BY number_students desc;")
    majors = cursor.fetchall()
    return majors

def get_user_messages(student_id):
    db = get_db()
    cursor = db.execute(f"SELECT m.id AS mid, m.content AS content, u1.name AS msg_from, u2.name AS msg_to, m.date_sent AS date_sent FROM message m JOIN user u1 ON m.msg_from = u1.id JOIN user u2 ON m.msg_to = u2.id where u1.id = {student_id} or u2.id = {student_id};")
    messages = cursor.fetchall()
    return messages

def get_student_absence(student_id):
    absence = Absence.query.filter_by(student_id=student_id)
    return absence

def get_grades_mean(student_id):
    db = get_db()
    cursor = db.execute(f"select sum(grade)/count(*) AS mean, subject from grade where student_id = {student_id} group by subject;")
    grades_mean = cursor.fetchall()
    return grades_mean

def get_all_subjects():
    db = get_db()
    cursor = db.execute(f"select subject.id as id, subject.name as name, user.name as teacher_name from subject join user on subject.id_prof = user.id;")
    subjects = cursor.fetchall()
    return subjects

def get_all_teachers():
    teacher = User.query.filter_by(role='teacher')
    return teacher

def get_all_absence():
    db = get_db()
    cursor = db.execute(f"select a.id as id, a.student_id as student_id, a.date_absence as date_absence, a.justified as justified, a.details as details, u.name as student_name from absence a join user u on u.id = a.student_id;")
    all_absence = cursor.fetchall()
    return all_absence

def get_one_payment(payment_id):
    payment = Payment.query.filter_by(id=payment_id).first()
    return payment
