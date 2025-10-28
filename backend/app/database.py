# # backend/app/database.py
# import os
# from motor.motor_asyncio import AsyncIOMotorClient
# from dotenv import load_dotenv
# from typing import Any

# load_dotenv()

# MONGO_URI = os.getenv("MONGO_URI")
# MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "daily_progress")

# _client: AsyncIOMotorClient | None = None
# db = None  # type: ignore

# async def init_db():
#     """Initialize global client and db. Call on app startup."""
#     global _client, db
#     if _client is None:
#         if not MONGO_URI:
#             raise RuntimeError("MONGO_URI not set in environment (.env or Render env vars)")
#         _client = AsyncIOMotorClient(MONGO_URI)
#         db = _client[MONGO_DB_NAME]

# def get_collection(name: str) -> Any:
#     if db is None:
#         raise RuntimeError("Database not initialized. Call init_db() first.")
#     return db[name]






# # backend/app/database.py
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from typing import Any

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "daily_progress")

_client: AsyncIOMotorClient | None = None
db = None  # type: ignore

async def init_db():
    """Initialize global client and db. Call on app startup."""
    global _client, db
    if _client is None:
        if not MONGO_URI:
            raise RuntimeError("MONGO_URI not set in environment (.env or Render env vars)")
        _client = AsyncIOMotorClient(MONGO_URI)
        db = _client[MONGO_DB_NAME]

def get_collection(name: str) -> Any:
    if db is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    return db[name]



# # app/database.py
# import motor.motor_asyncio
# from dotenv import load_dotenv
# import os

# load_dotenv()

# MONGO_URI = os.getenv("MONGO_URI")
# DB_NAME = os.getenv("MONGO_DB_NAME")

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
# db = client[DB_NAME]


# # app/database.py
# import motor.motor_asyncio
# from dotenv import load_dotenv
# import os, asyncio

# load_dotenv()

# MONGO_URI = os.getenv("MONGO_URI")
# DB_NAME = os.getenv("MONGO_DB_NAME")

# client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
# db = client[DB_NAME]

# async def test_connection():
#     try:
#         await db.command("ping")
#         print(f"✅ Connected to MongoDB database: {DB_NAME}")
#     except Exception as e:
#         print("❌ Connection failed:", e)

# if __name__ == "__main__":
#     asyncio.run(test_connection())
