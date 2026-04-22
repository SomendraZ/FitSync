from flask import Flask  # type: ignore[import]
from flask_cors import CORS  # type: ignore[import]
from app.db import db
from app.routes.auth import auth_bp
from app.routes.user import user_bp
from app.routes.exercise import exercise_bp


def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Enable CORS (allows frontend like React Native to call backend)
    CORS(app)

    # Register auth routes (signup, login, etc.)
    # Example: /auth/signup, /auth/login
    app.register_blueprint(auth_bp, url_prefix="/auth")
    # Register user routes (profile, etc.)
    # Example: /user/profile
    app.register_blueprint(user_bp, url_prefix="/user")
    # Register exercise routes (get exercises, etc.)
    # Example: /exercises?category=push or /exercises?muscle_group=chest
    app.register_blueprint(exercise_bp, url_prefix="/exercises")

    @app.route("/")
    def home():
        # Basic health check route
        return {"message": "FitSync API is running"}

    @app.route("/test-db")
    def test_db():
        # Debug route to verify MongoDB connection
        collections = db.list_collection_names()
        return {"collections": collections}

    return app