import asyncio

from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

"""
pip install motor

Use Motor para aplicativos Python assíncronos.
Motor é o driver assíncrono do MongoDB para Python. Ele fornece suporte para asyncio,
tornando possível escrever aplicativos assíncronos para o MongoDB.
"""


async def connect_to_mongo():
    uri = "mongodb://localhost:27017"

    client = AsyncIOMotorClient(uri, server_api=ServerApi(version="1"))

    try:
        await client.admin.command("ping")
        print("Connected to MongoDB")
    except Exception as e:
        print(e)


asyncio.run(connect_to_mongo())
