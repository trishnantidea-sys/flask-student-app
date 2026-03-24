# Flask ==> micro web framework untuk python yang digunakan untuk membuat aplikasi web dengan cepat dan mudah.
# Browser ==> HTTP Request ==> Flask (Web Server) ==> Python Function ==> HTTP Response ==> Browser
# Flask ==> Menghubungkan Web Request dengan Python Function

# # Install Flask
# pip install flask

# SQL Alchemy : Kita bisa gunakan Raw SQL ==> SELECT ....., INSERT ....., UPDATE dst....
# ORM ==> Object Relational Mapper ==> Pake Object dari Python nanti sama alchemy akan diubah menjadi query SQL
# Maintainability ==> Lebih mudah di maintain, Lebih clean, karena meskipun menggunakan SQL, tidak ada RAW Query SQL di dalam code nya

# ##### Install Package
# Flask Alchemy
# pip install flask_sqlalchemy

student = {
    "name": "Andi",
    "age": 20
}

print(student['name'])  #### Mewakili 1 student ==> setara dengan 1 baris data

students = [
    {"name": "Andi", "age": 20},
    {"name": "Budi", "age": 18}
]  ### setara dengan Tabel

### Masalah jika kita ingin MENGHARUSKAN setiap student HARUS punya NAME dan AGE

# student = {"name":"Andi"} ## tetap works, tapi tidak sesuai dengan ketentuan kita

# student = {"age":20}
# student = {"age": 20}
# name :
# age : NULL

# ## Tidak ada Struktur yg Fixed dari python

# Class ==> menentukan struktur dari suatu object (student)

class Student: ## Class
    def __init__(self, name, age):
        self.name = name  ## Atribut Name
        self.age = age    ## Atribut Age


# class Student ==> menentukan-mendefine Blueprint
# Setiap Object (Student) HARUS mengikuti Blueprint/Aturan ini
# __init__ ==> constructor ==> akan di run ketika object dibuat

# self.name; self.age ==> Atribut di dalam Object (Student)

# Setiap student HARUS memiliki atribut ini


s1 = Student("Andi", 20) ## Object Student 1
s2 = Student("Budi", 18) ## Object Student 2

print(s1.name)
print(s2.age)


### Dengan Class, setiap student object Harus mengikuti Struktur yg sudah ditentukan


Python ---------> Database
Class ----------> Table
Object ---------> Row - Baris
Atribut --------> Column - Kolom


class Students: ======> Database Table Students
Student("Andi", 20) ====> Baris ==> Andi | 20

## tidak ada struktur yang fixed dari python

Class ==> menentukan struktur dari suatu object (student)

db.session ===> SQL alchemy session ==> session memory

student = Student(name="Andi", age=20)

db.session.add(student)

Student Object ---> SQL Alchemy Session (data masih tersimpan di memori session) belum tersimpan di dalam Database
db.session.commit() ==> SQL Alchemy mengirimkan Update perubahan ke dalam Database

Student Object ---> SQL Alchemy Session ---> SQL Database (SQLite)

Bisa untuk multiple operation
Contoh :
student1 = Student(name="Andi",age=20)
student2 = Student(name="Budi",age=18)

db.session.add(student1)
db.session.add(student2)

db.session.commit()  ### Commit sama kaya di MYSQL dipake untuk operasi yg mengubah database ==> CREATE, UPDATE, DELETE

Create Object --> db.session.add() --> SESSION (temporary memory) --> db.session.commit() --> DATABASE

gunicorn ==> Production web server
app.run(debug=True) ==> Development server (Ga kepake pas deployment)

web: gunicorn app:app

web ==> Seb service
gunicorn ==> production server
app:app ==> pake file flask_app

Yang artinya ==> Perintah untuk Running Flask app yang ada di dalam app.py

Python local ==> push/upload ==> Github ==> Server

kalo sudah di masukkan ke gituhub tinggal :
git add .
git commit -m