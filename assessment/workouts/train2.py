import json

x = """{
    "data": "Jennifer Smith",
    "Contact Number": 7867567898,
    "meta": ["mail_id", "jen123@gmail.com", "mobile_number"],
    "Hobbies":["Reading", "Sketching", "Horse Riding"]
    }"""

# parse x:
y = json.loads(x)
# print(type(y))
#
send_dict: dict = y['Hobbies']
print("send_dict_type :", type(send_dict))
print(send_dict)

meta_dict: dict = y['meta']
print("meta_dict_type :", type(y))
print(meta_dict)
