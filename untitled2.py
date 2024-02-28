import requests
import json

url = 'https://authenticator-rest-api.bnet-identity.blizzard.net/v1/authenticator/device'

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer KRAxR4kEyAyfT8gS3D8hQQ9rrIcQPtGnI3'
}

data = {
  "restoreCode": "JGR9YKW8A7", 
  "serial": "KR230629386322"  
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.text)
