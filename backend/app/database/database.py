from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings

DATABASE_URL = settings.DATABASE_URL
DATABASE_NAME = settings.DATABASE_NAME

client = None
db = None


async def connect_db():
    global client
    global db
    client = AsyncIOMotorClient(DATABASE_URL)
    db = client[DATABASE_NAME]
    create_indexes(db)


async def close_db():
    client.close()


def get_database():
    return db


def create_indexes(db):
    projects = db['projects']
    users = db['users']
    projects.create_index("name", unique=True)
    users.create_index("email", unique=True)
