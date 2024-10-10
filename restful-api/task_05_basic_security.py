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

users = {
    "user1": {"username": "user1", "password":  generate_password_hash("user1"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("admin1"), "role": "admin"}
}


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


# @app.route('/admin-only', methods=["GET"])
# @jwt_required
# def admin_only():
#     return "Admin Access: Granted", 200


if __name__ == "__main__":
    app.run()
