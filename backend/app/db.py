from pymongo import MongoClient  # type: ignore[import]
from app.config import Config

# Create MongoDB client using connection string
client = MongoClient(Config.MONGO_URI)

# Get default database from URI
db = client.get_database()

# Create indexes for faster queries
db.users.create_index("email", unique=True)
db.exercises.create_index("category")
db.exercises.create_index("muscle_group")