from pymongo import MongoClient
from decouple import config

def get_database():

    MONGODB_URL = config("MONGODB_URL")
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(MONGODB_URL)
 
    # Create the database for our example (we will use the same database throughout the tutorial
    return client['TCC']