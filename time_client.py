# time_client.py
import requests
import json

age_dict = {
    "date": "10/10/1999",
    "units": "years"
}

json_to_send = age_dict
r = requests.post("http://127.0.0.1:5000/age", json=json_to_send)
print(r.status_code)
print(r.text)
