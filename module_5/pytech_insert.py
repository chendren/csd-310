# Chad Hendren
# Bellevue University
# CSD-310 November 21, 2021
# Module 5 pytech_insert.py assignment

import pymongo
from pymongo import MongoClient
from pymongo.collation import CollationAlternate
url = "mongodb+srv://admin:admin@cluster0.fsuv8.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# NOT the elegant way of inserting via lopping, I know :)

student = {"first_name":"Julius","last_name":"Hendren","student_id":"1007"}

student_student_id = db.students.insert_one(student).inserted_id

print("Inserted student record "+(student["first_name"])+" "+(student["last_name"])+" into the students collection with id "+str(student_student_id))

student2 = {"first_name":"Aurelius","last_name":"Hendren","student_id":"1008"}

student_student_id = db.students.insert_one(student2).inserted_id

print("Inserted student record "+(student2["first_name"])+" "+(student2["last_name"])+" into the students collection with id "+str(student_student_id))

student3 = {"first_name":"Julio","last_name":"Hendren","student_id":"1009"}

student_student_id = db.students.insert_one(student3).inserted_id

print("Inserted student record "+(student3["first_name"])+" "+(student3["last_name"])+" into the students collection with id "+str(student_student_id))

