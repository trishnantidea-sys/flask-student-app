from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"  ## menentukan database yg akan digunakan (kita pake SQL lite) Bisa diganti
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  ## disable fitur yg bikin memory berat

db = SQLAlchemy(app)  ### Menghubungkan SQL alchemy dengan Flask


###### Database Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

### CREATE TABLE -- di run hanya sekali
with app.app_context():
    db.create_all()
#print("DB created")


### Menampilkan Data --- READ DATA
@app.route("/")
def index():
    students = Student.query.all() ### sama aja kaya SELECT * FROM Student
    return render_template("index.html", students=students)


#### Menambahkan Data ---- CREATE DATA
@app.route('/add', methods=['POST'])
def add_students():
    Nama = request.form["name"]
    Usia = request.form["age"]
    new_students = Student(name=Nama, age=Usia)

    # students.append(new_students)
    db.session.add(new_students)  ### INSERT INTO student (name, age) VALUES ("Andi", 20)
    db.session.commit()

    return redirect(url_for("index"))


#### Menghapus Data - Delete Data
@app.route("/delete/<int:id>")
def delete_student(id):
    # global students
    # students = [s for s in students if s['id'] != id]
    student = Student.query.get(id)  #### Menemukan data berdasarkan ID (primary key) ==> SELECT * FROM student WHERE id = ....
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("index"))

#### Mengubah Data --- UPDATE DATA
@app.route("/edit/<int:id>")
def edit_student(id):
    # student = ""

    # for s in students:
    #     if s['id'] == id:
    #         student = s
    #         break

    student = Student.query.get(id)
    return render_template("edit.html", student=student)


@app.route("/update/<int:id>", methods=["POST"])
def update_student(id):
    # for s in students:
    #     if s['id'] == id:
    #         s['name'] = request.form['Nama']
    #         s['age'] = request.form['Usia']

    student = Student.query.get(id)
    student.name = request.form["Nama"]
    student.age = request.form["Usia"]

    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5050)