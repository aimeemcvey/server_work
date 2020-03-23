import requests
import json
from datetime import datetime

age_dict = {
    "date": "10/10/1999",
    "units": "years"
}
with open('age.json', 'w') as outfile:
    json.dump(age_dict, outfile)

with open('age.json') as json_file:
    age_year = json.load(json_file)
date = datetime.strftime(datetime.now(), "%m-%d-%y")
date_split = date.split('-')
date_ints = []
for x in date_split:
    date_ints.append(int(x))
date_ints[2] = date_ints[2] + 2000
print(date_ints)

given_year = age_year.get("date")
year_split = given_year.split('/')
given_year_ints = []
for x in year_split:
    given_year_ints.append(int(x))
print(given_year_ints)

current_day = datetime(date_ints[2], date_ints[0], date_ints[1])
given_day = datetime(given_year_ints[2], given_year_ints[0], given_year_ints[1])
diff = current_day-given_day
print("Difference of {} days".format(diff.days))