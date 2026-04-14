from pymongo import MongoClient  # type: ignore[import]
from app.config import Config

# Create MongoDB client using connection string
client = MongoClient(Config.MONGO_URI)

# Get default database from URI
db = client.get_database()

# Ensure unique email indexes
db.users.create_index("email", unique=True)