from flask import Blueprint, request, jsonify  # type: ignore[import]
from app.db import db
from app.utils.security import hash_password, check_password, generate_token

# Create a Blueprint for auth routes
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    # Get JSON data from request body
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    # Validate required fields
    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    # Check if user already exists in DB
    existing_user = db.users.find_one({"email": email})
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    # Hash password before storing (never store plain passwords)
    hashed_password = hash_password(password)

    # Create user document
    user = {
        "email": email,
        "password": hashed_password
    }

    # Insert user into database
    db.users.insert_one(user)

    return jsonify({"message": "User created successfully"}), 201


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