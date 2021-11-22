# Chad Hendren
# Bellevue University
# CSD-310 November 21, 2021
# Module 5 pytech_delete.py assignment

import pymongo
from pymongo import MongoClient
from pymongo.collation import CollationAlternate
url = "mongodb+srv://admin:admin@cluster0.fsuv8.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech.students

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
doc = db.find_one({"student_id": "1007"})
stud_id = str(doc["student_id"])
print("Student ID:  "+(stud_id))
print("First Name:  "+doc["first_name"])
print("Last Name:  "+doc["last_name"]+'\n')

docs = db.find({})
for document in docs:
    stud_id = str(docs["student_id"])
    print("Student ID:  "+(stud_id))
    print("First Name:  "+docs["first_name"])
    print("Last Name:  "+docs["last_name"]+'\n')