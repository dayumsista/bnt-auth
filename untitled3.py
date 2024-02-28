import requests

bearer_token = "KRW13BlHa86zMjY41WgoqcXT6VMYh5JYNa" #bearer_token

url = "https://authenticator-rest-api.bnet-identity.blizzard.net/v1/authenticator"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

response = requests.post(url, headers=headers)

print(response.text)