#!/usr/bin/python3
"""
0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
         "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/data")
def data():
    return jsonify([username for username in users.keys()])


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    try:
        return users[username]
    except KeyError:
        return jsonify({"error": "User not found"})


@app.post("/add_user")
def add_user():
    user = request.get_json()
    try:
        users[user['username']] = user
        return jsonify({"message": "User added", "user": user})
    except KeyError:
        return jsonify({"error": "Username is required"})


if __name__ == "__main__":
    app.run()
