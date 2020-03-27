# health_db_server.py
from flask import Flask, jsonify, request

db = []

app = Flask(__name__)


def add_patient_to_db(name, id, age):
    new_patient = {"name": name, "id": id, "age": age}
    db.append(new_patient)
    return True


def init_database():
    add_patient_to_db("Ann Ables", 101, 35)
    add_patient_to_db("Bob Boyles", 102, 40)


if __name__ == "__main__":
    init_database()
    app.run()
