#! /usr/bin/env python3
import pymongo

DATABASE_NAME = "inti"
COLLECTION_NAME = "test_gps"
URL = "mongodb+srv://inti-drifter:inti2023@cluster0.vktbm.gcp.mongodb.net/drifter"





_client = None
_database = None


class DatabaseManager:
    def __init__(self, config = {}):
        self.database_name = config.get("database", DATABASE_NAME)
        self.url = config.get("url", URL)
        self.client = pymongo.MongoClient(self.url)
        self.database = self.client[self.database_name]
        

    def insert_data(self, collection, **data):
        try:
            return self.database[collection].insert_one(data)
        except Exception as e:
            print(f"Error inserting data: {str(e)}")
            return None

    def find_data(self, collection, **filters):
        try:
            return self.database[collection].find(filters)
        except Exception as e:
            print(f"Error finding data: {str(e)}")
            return None

    def list_collection(self, name_collection):
        collection = self.database[name_collection] 
        clist = collection.find({})
        for data in clist:
            print(data)



# Uso:
if __name__ == "__main__":
    config = {"database": "mydatabase", "url": URL}
    db_manager = DatabaseManager(config)

    data_to_insert = {"name": "John", "age": 30}
    db_manager.insert_data("mycollection", data_to_insert)

    search_filters = {"age": {"$gt": 25}}
    result = db_manager.find_data("mycollection", search_filters)

    for document in result:
        print(document)

    db_manager.client.close()
