from functools import wraps
from flask import request, jsonify # type: ignore[import]
import jwt # type: ignore[import]
from app.config import Config


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Step 1: Get token from headers
        auth_header = request.headers.get("Authorization")

        if auth_header:
            try:
                # Format: Bearer <token>
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({"error": "Invalid token format"}), 401

        # Step 2: Check if token exists
        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            # Step 3: Decode token
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])

            # Extract user_id
            user_id = data["user_id"]

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401

        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        # Step 4: Pass user_id to route
        return f(user_id, *args, **kwargs)

    return decorated