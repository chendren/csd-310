# Chad Hendren
# Bellevue University
# CSD-310 November 21, 2021
# Module 5 mongodb_test.py assignment

import pymongo
from pymongo import MongoClient
url = "mongodb+srv://admin:<password>@cluster0.fsuv8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names)
