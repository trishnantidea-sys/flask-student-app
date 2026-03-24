from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  ## disable fitur yg bikin memory berat

db = SQLAlchemy(app) ### menghubungkan SQL alchemy dengan Flask


##### Database model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
Class ini merepresentasikan Tabel dalam Database
SQL alchemny otomatis akan mengubah Code tersebut menjadi

CREATE TABLE Student (
    id INTEGER Primary Key,
    name TEXT,
    age INTEGER
)
ORM ==>
student = Student(name="Andi", age = 20)

db.session.add(student)
db.session.commit()

SQL Alchemy akan otomatis mengubah code menjadi 
INSERT INTO studet (nama, age) VALUES ("Andi",20)