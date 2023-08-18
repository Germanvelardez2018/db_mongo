#! /usr/bin/env python3
import pymongo

DATABASE_NAME = "inti"
COLLECTION_NAME = "test_gps"

client = pymongo.MongoClient("mongodb+srv://inti-drifter:inti2023@cluster0.vktbm.gcp.mongodb.net/drifter")

database = client[DATABASE_NAME]

collection =database[COLLECTION_NAME]



