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
mycol = db["students"]

docs = db.mycol.find({})
print(docs)

myquery = { "student_id": "1007" }

doc = mycol.find(myquery)
print("Student ID: "+(doc["student_id"])
print("First Name: "+(doc["first_name"])
print("Last Name: "+(doc["last_name"])