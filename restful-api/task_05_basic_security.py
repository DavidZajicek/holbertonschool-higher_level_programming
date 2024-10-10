#!/usr/bin/python3
"""
0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
basic_auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "holberton-study"
jwt = JWTManager(app)

users = {}


@basic_auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username).get("password"), password):
        return username


@basic_auth.get_user_roles
def get_user_roles(user):
    return user.get_roles()


@app.get('/basic-protected')
@basic_auth.login_required
def basic_protected():
    return "Hello, {}!".format(basic_auth.current_user())


@app.route('/login', methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username in users and check_password_hash(users.get(username).get("password"), password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return jsonify({"message": "Bad username or password"}), 401


@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200


@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admin_only():
    if users[get_jwt_identity()]["role"] != "admin":
        return "Admins only", 403
    return "Admin Access: Granted", 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/")
def hello_world():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify([username for username in users])


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    try:
        return users[username]
    except KeyError:
        return jsonify({"error": "User not found"}), 404


@app.post("/add_user")
def add_user():
    user = request.get_json()
    try:
        user['password'] = generate_password_hash(user['password'])
        users[user['username']] = user
        return jsonify({"message": "User added", "user": user}), 201
    except KeyError:
        return jsonify({"error": "Username is required"}), 400


if __name__ == "__main__":
    app.run()
