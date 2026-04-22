from flask import Blueprint, request, jsonify
from app.db import db

exercise_bp = Blueprint("exercise", __name__)


# 🔹 GET all exercises (with optional filters)
@exercise_bp.route("", methods=["GET"])
def get_exercises():
    category = request.args.get("category")
    muscle_group = request.args.get("muscle_group")

    query = {}

    if category:
        query["category"] = category.lower()

    if muscle_group:
        query["muscle_group"] = muscle_group.lower()

    exercises = list(db.exercises.find(query))

    # Convert ObjectId to string
    for ex in exercises:
        ex["_id"] = str(ex["_id"])

    return jsonify({
        "success": True,
        "count": len(exercises),
        "data": exercises
    }), 200