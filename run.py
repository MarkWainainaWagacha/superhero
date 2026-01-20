from server.app import app
#from server.seed import seed_database  # Optional, only if you want to seed

if __name__ == "__main__":
    # Seed database only once (optional)
    # seed_database()

    # Start Flask server
    app.run(debug=True, port=5555)
