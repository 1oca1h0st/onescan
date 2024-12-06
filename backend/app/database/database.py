from motor.motor_asyncio import AsyncIOMotorClient

DATABASE_URL = "mongodb://127.0.0.1:27017"
DATABASE_NAME = "fastapi_db"

client = None
db = None

async def connect_db():
    global client
    global db
    client = AsyncIOMotorClient(DATABASE_URL)
    db = client[DATABASE_NAME]

async def close_db():
    client.close()

def get_database():
    return db
