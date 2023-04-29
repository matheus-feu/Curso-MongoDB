from pymongo import MongoClient, errors


def connect_mongo():
    try:
        uri = "mongodb://localhost:27017"
        mongo_client = MongoClient(uri)
        mongo_client.admin.command("ping")
        return mongo_client
    except errors.ConnectionFailure as e:
        raise e


client = connect_mongo()