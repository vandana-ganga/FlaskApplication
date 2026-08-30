from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

credentials = {}


# --------------------------------------------------------------------------
# Version 1 endpoints
# --------------------------------------------------------------------------

@app.route("/", methods=["GET"])
def home():
    """Serve the welcome page. GET only - any other method returns 405."""
    return render_template("index.html")


@app.route("/health", methods=["GET"])
def health():
    """Serve the health check page. GET only - any other method returns 405."""
    return render_template("health.html")


@app.route("/add", methods=["POST"])
def add_credential():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Request body must be a JSON object sent with "
                     "Content-Type: application/json"
        }), 400

    missing = [field for field in ("username", "password") if not data.get(field)]
    if missing:
        return jsonify({
            "error": "Missing or empty required field(s): " + ", ".join(missing)
        }), 400

    username = data["username"]
    password = data["password"]

    if not isinstance(username, str) or not isinstance(password, str):
        return jsonify({"error": "username and password must be strings"}), 400

    already_stored = username in credentials
    credentials[username] = password

    if already_stored:
        return jsonify({
            "message": f"Password for '{username}' was updated",
            "username": username,
        }), 200

    return jsonify({
        "message": f"User '{username}' added successfully",
        "username": username,
    }), 201


@app.route("/get/<username>", methods=["GET"])
def get_credential(username):
    if username not in credentials:
        return jsonify({"error": f"Username '{username}' not found"}), 404

    return jsonify({
        "username": username,
        "password": credentials[username],
    }), 200


@app.errorhandler(404)
def handle_not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(405)
def handle_method_not_allowed(error):
    return jsonify({
        "error": "Method not allowed. Check whether this endpoint expects "
                 "GET or POST."
    }), 405


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
