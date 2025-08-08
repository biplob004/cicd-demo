from flask import Flask, jsonify
import logging
import os

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.route("/")
def hello_world():
    logger.info("Hello world endpoint accessed")
    return "Hello, World! This is a Flask demo application for CI/CD testing."


@app.route("/health")
def health_check():
    logger.info("Health check endpoint accessed")
    return jsonify({"status": "healthy", "message": "Flask app is running successfully"})


@app.route("/info")
def app_info():
    return jsonify(
        {"app_name": "Flask CI/CD Demo", "version": "1.0.1", "environment": os.environ.get("FLASK_ENV", "development")}
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
