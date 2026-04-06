from app import create_app

# Create Flask app instance
app = create_app()

if __name__ == "__main__":
    # Run server in debug mode (auto reload + better error logs)
    app.run(debug=True, use_reloader=False)