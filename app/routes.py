from flask import Flask, jsonify, request
from app.calculator import add, subtract, multiply, divide

app = Flask(__name__)


@app.route("/")
def home():
    return "Python Calculator Microservice Running"


@app.route("/add")
def add_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    result = add(a, b)

    return jsonify({
        "operation": "addition",
        "result": result
    })


@app.route("/subtract")
def subtract_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    result = subtract(a, b)

    return jsonify({
        "operation": "subtraction",
        "result": result
    })


@app.route("/multiply")
def multiply_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    result = multiply(a, b)

    return jsonify({
        "operation": "multiplication",
        "result": result
    })


@app.route("/divide")
def divide_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    result = divide(a, b)

    return jsonify({
        "operation": "division",
        "result": result
    })