# client.py
import requests

name_to_send = "Sue"
# r = requests.get("http://127.0.0.1:5000/info")
r = requests.post("http://127.0.0.1:5000/send_name", json=name_to_send)
print(r.status_code)
print(r.text)

name_to_send = "Johnny"
r = requests.post("http://127.0.0.1:5000/send_name", json=name_to_send)
print(r.status_code)
print(r.text)

r = requests.get("http://127.0.0.1:5000/get_names")
answer = r.json()
print(answer)

r = requests.get("http://127.0.0.1:5000/say_hello/Dave")
print(r.text)
