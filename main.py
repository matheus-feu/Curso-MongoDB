import datetime

from pymongo import MongoClient

connect_string = "mongodb://localhost:27017"

client = MongoClient(connect_string)

# Verify that the database exists
dbs = client.list_database_names()
print(dbs)

# Create a new database
db = client["Alura_Series"]
collections = db.list_collection_names()
print(collections)


# Insert a test document
def insert_test_document():
    collection = db["filmes"]
    test_documet = {
        "titulo": "Star Wars",
        "ano": 1977,
        "diretor": "George Lucas"
    }
    insert_id = collection.insert_one(test_documet).inserted_id
    print(insert_id)


# Create a new database
production = client.production

# Create a new collection
person_collection = production.person_collection


def create_documents():
    first_names = ["John", "Jane", "Joe", "Jack", "Jill"]
    last_names = ["Doe", "Doe", "Doe", "Doe", "Doe"]
    ages = [25, 26, 27, 28, 29]
    telephone_numbers = ["555-555-5555", "555-555-5556", "555-555-5557", "555-555-5558", "555-555-5559"]

    docs = []

    for first_names, last_names, ages, telephone_numbers in zip(first_names, last_names, ages, telephone_numbers):
        doc = {
            "first_name": first_names,
            "last_name": last_names,
            "age": ages,
            "telephone": telephone_numbers,
            "created_at": datetime.datetime.utcnow()

        }
        docs.append(doc)
        # person_collection.insert_one(doc)

    person_collection.insert_many(docs)


create_documents()


