import json

x = """{
    "data": "Jennifer Smith",
    "Contact Number": 7867567898,
    "meta": "jen123@gmail.com",
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    }"""

# parse x:
y = json.loads(x)
print(y)

send_dict: dict = y['data']
meta_dict: dict = send_dict['meta']

