import requests
import json
import time
token = input("Please enter your token: ")
restoreCode = input("Please enter your restoreCode: ")
serial = input("Please enter your serial: ")
url = 'https://oauth.battle.net/oauth/sso'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
}

data = {
    'client_id': 'baedda12fe054e4abdfc3ad7bdea970a',
    'grant_type': 'client_sso',
    'scope': 'auth.authenticator',
    'token': token  
}

response = requests.post(url, headers=headers, data=data)
print(response)
time.sleep(1)
if response.status_code == 200:
    try:
        response_json = response.json()

        access_token = response_json.get('access_token', 'No access_token found')

        print(access_token)

    except json.JSONDecodeError:
        print("Failed to parse response as JSON")
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")


url = 'https://authenticator-rest-api.bnet-identity.blizzard.net/v1/authenticator/device'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}'
}

data = {
  "restoreCode": restoreCode, 
  "serial": serial  
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text)