# name_server.py

import requests

r = requests.get("https://api.github.com/repos/aimeemcvey/BME547Class/branches")
answer = r.json()
print(answer)
for branch in answer:
    print("Name of branch is {}".format(branch["name"]))

request_json = {"one": "Spain", "two": "Canada"}
s = requests.post("http://vcm-7631.vm.duke.edu:5000/compare", json=request_json)
if r.status_code == 200:
    print(s.json())
else:
    print("Error with status code of {}" .format(r.status_code))
