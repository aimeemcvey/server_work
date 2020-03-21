# blood_match.py
import requests

p = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/ajm111")
patient_list = p.json()

b_donor = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(patient_list["Donor"]))
b_recipient = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/{}".format(patient_list["Recipient"]))
print(b_donor.text)
print(b_recipient.text)

if b_donor.text == "O-" or b_donor.text == "O+":
    compatible = "Yes"
if b_donor.text == "A-" or b_donor.text == "A+":
    if b_recipient.text == "A-" or b_recipient.text == "A+" or b_recipient.text == "AB+" or b_recipient.text == "AB-":
        compatible = "Yes"
    else:
        compatible = "No"
if b_donor.text == "B-" or b_donor.text == "B+":
    if b_recipient.text == "B-" or b_recipient.text == "B+" or b_recipient.text == "AB+" or b_recipient.text == "AB-":
        compatible = "Yes"
    else:
        compatible = "No"
if b_donor.text == "AB-" or b_donor.text == "AB+":
    if b_recipient.text == "AB+" or b_recipient.text == "AB-":
        compatible = "Yes"
    else:
        compatible = "No"

print(compatible)

match = {"Name": "ajm111", "Match": compatible}
m = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=match)
if m.status_code == 200:
    print("You are {}." .format(m.text))
else:
    print("Error with status code of {}" .format(m.status_code))

