#! /usr/bin/env python3
import pymongo
import time

DATABASE_NAME = "inti"
COLLECTION_NAME = "test_gps"

client = pymongo.MongoClient("mongodb+srv://inti-drifter:inti2023@cluster0.vktbm.gcp.mongodb.net/drifter")

database = client[DATABASE_NAME]

collection =database[COLLECTION_NAME]



def list_data():
    pass


def find_data(**filters):
    

    try:
        clist = collection.find(filters)

        for data in clist:
            print(data)
       
    except ValueError as exc:
      pass

def insert_data(data):
    try:
        
        collection.insert_one(data)
       
    except ValueError as exc:
        if exc.timeout:
            print(f"block timed out: {exc!r}")
        else:
            print(f"failed with non-timeout error: {exc!r}")
    