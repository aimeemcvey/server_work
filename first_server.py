# first_server.py

from flask import Flask, jsonify, request

app = Flask(__name__)
name_database = []


@app.route("/", methods=["GET"])
def server_on():
    return "Server On"


@app.route("/info", methods=["GET"])
def info():
    info_dictionary = {
        "author": "Aimee McVey",
        "version": 20,
        "date": "March 27, 2020"
    }
    return jsonify(info_dictionary)


@app.route("/send_name", methods=["POST"])
def add_name_to_database():
    name_to_add = request.get_json()
    name_database.append(name_to_add)
    return "Name '{}' added".format(name_to_add)


@app.route("/number", methods=["GET"])
def return_number():
    return jsonify(5)


@app.route("/get_names", methods=["GET"])
def get_names():
    return jsonify(name_database)


@app.route("/say_hello/<person_name>", methods=["GET"])
def say_hello(person_name):
    answer = "Hello, {}".format(person_name)
    return answer


@app.route("/get_info/server_name", methods=["GET"])
def return_server_info():
    return "The server info is this."


@app.route("/get_info/author", methods=["GET"])
def return_author():
    return "The author is me."


@app.route("/math/addition/<num1>..<num2>", methods=["GET"])
def addition(num1, num2):
    answer = int(num1) + int(num2)
    return jsonify(answer)


if __name__ == "__main__":
    app.run()
