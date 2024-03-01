import requests
import time
url = 'https://oauth.battle.net/oauth/sso'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
}
token = input("Please enter your token: ")
data = {
    'client_id': 'baedda12fe054e4abdfc3ad7bdea970a',
    'grant_type': 'client_sso',
    'scope': 'auth.authenticator',
    'token': token  
}
response = requests.post(url, headers=headers, data=data)
response_json = response.json()
if 'error' in response_json and response_json['error'] == 'invalid_token':
    print("Invalid SSO token!")
    exit()
access_token = response_json.get('access_token')
if not access_token:
    print("Access token not found in the response.")
    exit()
url = "https://authenticator-rest-api.bnet-identity.blizzard.net/v1/authenticator"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {access_token}"  
}
response = requests.post(url, headers=headers)
auth_response_json = response.json()
serial = auth_response_json.get('serial')
restoreCode = auth_response_json.get('restoreCode')
deviceSecret = auth_response_json.get('deviceSecret')
print(serial)
print(restoreCode)
print(deviceSecret)

import sys
import os

data_list = [
    serial,
    restoreCode,
    deviceSecret
]

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(application_path, "bntAuth.txt")

file_exists_and_not_empty = os.path.isfile(file_path) and os.path.getsize(file_path) > 0

with open(file_path, "a") as f:
    if file_exists_and_not_empty:
        f.write("\n")
    for item in data_list:
        f.write(item + "\n")

time.sleep(2)
print("Data saved.")

time.sleep(2)
input("Press Enter to exit...")
#https://account.battle.net/login/en/?ref=localhost
