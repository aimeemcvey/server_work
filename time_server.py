# time_server.py
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


@app.route("/time", methods=["GET"])
def current_time():
    dt = datetime.now()
    time = datetime.strftime(dt, "%H:%M:%S")
    return time


@app.route("/date", methods=["GET"])
def current_date():
    dt = datetime.now()
    date = datetime.strftime(dt, "%m-%d-%y")
    return date


@app.route("/age", methods=["POST"])
def calculate_age():
    age_year = request.get_json()
    date = datetime.strftime(datetime.now(), "%m-%d-%y")
    date_split = date.split('-')
    date_ints = []
    for x in date_split:
        date_ints.append(int(x))
    date_ints[2] = date_ints[2] + 2000

    given_year = age_year.get("date")
    year_split = given_year.split('/')
    given_year_ints = []
    for x in year_split:
        given_year_ints.append(int(x))

    current_day = datetime(date_ints[2], date_ints[0], date_ints[1])
    given_day = datetime(given_year_ints[2], given_year_ints[0], given_year_ints[1])
    diff = current_day - given_day
    years = round(diff.days/365)
    return "Difference of {} days or {} years".format(diff.days, years)


@app.route("/until_next_meal/<meal>", methods=["GET"])
def meal_time(meal):
    t = datetime.now()
    if meal == 'breakfast':
        bfast_time = datetime(2020, 3, 24, 9, 0, 0)
        diff = bfast_time - t
    if meal == 'lunch':
        lunch_time = datetime(2020, 3, 24, 13, 0, 0)
        diff = lunch_time - t
    if meal == 'dinner':
        dinner_time = datetime(2020, 3, 24, 18, 30, 0)
        diff = dinner_time - t
    hours = round(diff.seconds/3600)
    return "{} hours until {}".format(hours, meal)


if __name__ == "__main__":
    app.run()
