import os
from dotenv import load_dotenv  # type: ignore[import]

# Load environment variables from .env file
load_dotenv()


class Config:
    # MongoDB connection string
    MONGO_URI = os.getenv("MONGO_URI")

    # Secret key for JWT encoding/decoding
    SECRET_KEY = os.getenv("SECRET_KEY")