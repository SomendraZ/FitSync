from flask import Flask  # type: ignore[import]
from flask_cors import CORS  # type: ignore[import]
from app.db import db
from app.routes.auth import auth_bp


def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Enable CORS (allows frontend like React Native to call backend)
    CORS(app)

    # Register auth routes (signup, login, etc.)
    # All routes inside auth_bp will be prefixed with /auth
    # Example: /auth/signup, /auth/login
    app.register_blueprint(auth_bp, url_prefix="/auth")

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