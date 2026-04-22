from flask import Blueprint, jsonify, request
from bson import ObjectId # type: ignore[import]
from datetime import datetime
from app.db import db
from app.utils.decorators import token_required

user_bp = Blueprint("user", __name__)

@user_bp.route("/profile", methods=["GET"])
@token_required
def get_profile(user_id):
    user = db.users.find_one({"_id": ObjectId(user_id)})

    if not user:
        return jsonify({"error": "User not found"}), 404

    # 🔥 Remove sensitive data
    user.pop("password", None)

    # Convert ObjectId to string
    user["_id"] = str(user["_id"])

    return jsonify({
        "success": True,
        "data": user
    }), 200

@user_bp.route("/profile", methods=["PUT"])
@token_required
def update_profile(user_id):
    data = request.get_json()

    update_data = {}

    if "username" in data:
        username = data["username"].strip()
        if len(username) < 3:
            return jsonify({"error": "Username must be at least 3 characters"}), 400
        update_data["username"] = username

    if not update_data:
        return jsonify({"error": "No valid fields to update"}), 400

    update_data["updated_at"] = datetime.utcnow()

    db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    return jsonify({
        "success": True,
        "message": "Profile updated successfully"
    }), 200