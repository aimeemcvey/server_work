# time_server.py
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


@app.route("/time", methods=["GET"])
def current_time():
    time = datetime.now()
    time = datetime.strftime(time, "%H:%M:%S")
    print(time)
    return time

# @app.route("/date", methods=["GET"])
# def current_date():
#
#
# @app.route("/age", methods=["POST"])
# def calculate_age():
#     info_dictionary = {
#         "author": "Aimee McVey",
#         "version": 20,
#         "date": "March 27, 2020"
#     }
#     return jsonify(info_dictionary)
#
#
# @app.route("/until_next_meal/<meal>", methods=["GET"])
# def meal_time():


if __name__ == "__main__":
    app.run()
