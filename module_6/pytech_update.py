# Chad Hendren
# Bellevue University
# CSD-310 November 21, 2021
# Module 5 pytech_update.py assignment

import json
import pymongo
from pymongo import MongoClient
from pymongo.collation import CollationAlternate
url = "mongodb+srv://admin:admin@cluster0.fsuv8.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech.students


myquery = ({ "student_id": "1007" })
myupdate = ({ "$set": {"student_id": "1010"}})
db.update_one(myquery, myupdate)

doc = db.find_one({"student_id": "1010"})
stud_id = str(doc["student_id"])
print("Student ID:  "+(stud_id))
print("First Name:  "+doc["first_name"])
print("Last Name:  "+doc["last_name"]+'\n')
