# name_server.py

import requests

student = {"name": "Aimee McVey", "net_id": "ajm111", "e-mail": "aimee.mcvey@duke.edu"}
# s = requests.post("http://vcm-7631.vm.duke.edu:5001/student", json=student)
# if s.status_code == 200:
#     print(s.json())
# else:
#     print("Error with status code of {}" .format(s.status_code))

r = requests.get("http://vcm-7631.vm.duke.edu:5001/list")
student_list = r.json()
print(student_list)

numbers = {"a": 6, "b": 2}
n = requests.post("http://vcm-7631.vm.duke.edu:5001/sum", json=numbers)
if n.status_code == 200:
    print("The sum is {}." .format(n.json()))
else:
    print("Error with status code of {}" .format(n.status_code))

