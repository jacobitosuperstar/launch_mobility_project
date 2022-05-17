import requests
import json
import time

url_register = "http://localhost:8000/register/"
url_update = "http://localhost:8000/updater/"
url_delete = "http://localhost:8000/deleter/"
url_user_zone_updater = "http://localhost:5000/"
url_user_locations = "http://localhost:3000/"
url_distance_calculations = "http://localhost:3000/distance/"

# # user creation
# data_register = {
#     "first_name": "jacobo",
#     "middle_name": "mateo",
#     "last_name": "bedoya",
#     "email": "mateo@mateo.com",
#     "zip_code": "95014",
#     "password": "prueba",
#     "confirm_password": "prueba",
# }
# data_register = json.dumps(data_register)
# x = requests.post(url_register, json=data_register)
# x = x.json()
# print("** Checking User Registration **")
# print(x)
# time.sleep(5)
#
# # checking the creation from the other app
# y = requests.get(url_user_zone_updater)
# y = y.json()
# print("** Checking User Creation from the other app **")
# print(y)
# time.sleep(5)
#
# # checking locations
# z = requests.get(url_user_locations)
# z = z.json()
# print("** Checking User Locations on creation from the other app **")
# print(z)
# time.sleep(5)
#
# # updating the user
# data_update = {
#     "user_id": x.get("user").get("id"),
#     "email": "jacobo@jacobo.com",
#     "zip_code": "96898",
# }
# data_update = json.dumps(data_update)
# x = requests.post(url_update, json=data_update)
# x = x.json()
# print("** Checking User Update **")
# print(x)
# time.sleep(5)
#
# # checking the creation from the other app
# y = requests.get(url_user_zone_updater)
# # y = json.loads(y.text)
# y = y.json()
# print("** Checking User Update from the other app **")
# print(y)
# time.sleep(5)
#
# # checking locations
# z = requests.get(url_user_locations)
# z = z.json()
# print("** Checking User Locations on update from the other app **")
# print(z)
# time.sleep(5)
#
# # user deletion
# data_deletion = {
#     # "user_id": x.get("user").get("id")
#     "user_id": 4
# }
# data_deletion = json.dumps(data_deletion)
# x = requests.post(url_delete, json=data_deletion)
# print("** Checking User Deletion **")
# print(x.json())
# time.sleep(5)
#
# # checking the creation from the other app
# y = requests.get(url_user_zone_updater)
# # y = json.loads(y.text)
# y = y.json()
# print("** Checking User Deletion from the other app **")
# print(y)
# time.sleep(5)
#
# # checking locations
# z = requests.get(url_user_locations)
# z = z.json()
# print("** Checking User Locations on update from the other app **")
# print(z)
# time.sleep(5)

# measuring distance
data = {
    "zip_code_1": "96898",
    "zip_code_2": "95014",
}
data_update = json.dumps(data)
z = requests.post(url_distance_calculations, json=data_update)
z = z.json()
print("** Checking User Update **")
print(z)
time.sleep(5)
