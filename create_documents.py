from datetime import datetime

from drivers.mongo_client import client

# Criar o banco de dados e a coleção
person = client.person
person_collection = person.person_collection


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
            "created_at": datetime.utcnow()

        }
        docs.append(doc)
        # person_collection.insert_one(doc)

    person_collection.insert_many(docs)


create_documents()
