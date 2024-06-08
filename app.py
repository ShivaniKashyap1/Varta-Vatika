from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Sample data for users
users = [
    {"id": 1, "email": "chysubhash1234@gmail.com", "password": "Subhash"},
    {"id": 2, "email": "user2@example.com", "password": "password2"},
]

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    # Find the user by email
    user = next((u for u in users if u["email"] == email), None)

    # If the user is found, check the password
    if user:
        if check_password_hash(user["password"], password):
            return jsonify({"message": "Logged in successfully", "user": user})
        else:
            return jsonify({"message": "Invalid password"}), 401
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)