import bcrypt  # type: ignore[import]
import jwt  # type: ignore[import]
from datetime import datetime, timedelta
from app.config import Config


# Hash plain password before storing in DB
def hash_password(password):
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")  # convert bytes → string

# Compare entered password with stored hashed password
def check_password(password, hashed):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed.encode("utf-8")  # convert string → bytes
    )


# Generate JWT token for authenticated user
def generate_token(user_id):
    payload = {
        "user_id": str(user_id),  # Store user ID in token
        "exp": datetime.utcnow() + timedelta(days=1)  # Token expires in 1 day
    }

    # Encode payload using secret key
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")
    return token