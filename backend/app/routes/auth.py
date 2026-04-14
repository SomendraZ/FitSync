from flask import Blueprint, request, jsonify  # type: ignore[import]
from pymongo.errors import DuplicateKeyError # type: ignore[import]

from app.db import db
from app.utils.security import hash_password, check_password, generate_token
from app.utils.decorators import token_required
from app.models.user_model import create_user_document

# Create a Blueprint for auth routes
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    # Get JSON data from request body
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    username = data.get("username")

    # Validation
    if not email or "@" not in email:
        return jsonify({"error": "Valid email required"}), 400

    if not password or len(password) < 6:
        return jsonify({"error": "Password must be at least 6 characters"}), 400

    if not username or len(username) < 3:
        return jsonify({"error": "Username must be at least 3 characters"}), 400


    # Normalize
    email = email.lower().strip()
    username = username.strip()

    hashed_password = hash_password(password)

    # Create user document
    user = create_user_document(email, hashed_password, username)


    # Insert user into database
    try:
        db.users.insert_one(user)
    except DuplicateKeyError:
        return jsonify({"error": "User already exists"}), 400

    return jsonify({
        "message": "User created successfully",
        "username": username
    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    # Get JSON data from request body
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    # Find user by email
    user = db.users.find_one({"email": email})

    # Check if user exists
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    # Verify password with hashed password
    if not check_password(password, user["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate authentication token (JWT)
    token = generate_token(user["_id"])

    return jsonify({
        "message": "Login successful",
        "token": token
    }), 200

@auth_bp.route("/profile", methods=["GET"])
@token_required
def profile(user_id):
    return jsonify({
        "message": "Access granted",
        "user_id": user_id
    })