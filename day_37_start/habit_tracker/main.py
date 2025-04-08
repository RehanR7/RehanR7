import requests
from datetime import datetime

TOKEN = "K09acz(uMtGph("
USERNAME = "drexistance"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_params = {
    "name": "Coding Time Records",
    "unit": "Minutes",
    "type": "int",
    "color": "shibafu",
    "timezone": "Asia/Karachi",
    "startOnMonday": True
}

# response = requests.put(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# date = datetime(2025, 2, 24)
# pixel_endpoint =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# pixel_params = {
#     "date": date.strftime(format="%Y%m%d"),
#     "quantity": "4"
# }

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20250224"
update_pixel_params = {
    "quantity": "240"
}
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20250224"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)

date = datetime.now()
quantity = input("How long did you work today: ")
pixel_creation_endpoint =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params = {
    "date": date.strftime(format="%Y%m%d"),
    "quantity": quantity
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
print(response.text)