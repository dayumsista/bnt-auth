import requests

url = 'https://oauth.battle.net/oauth/sso'


headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
}

data = {
    'client_id': 'baedda12fe054e4abdfc3ad7bdea970a',
    'grant_type': 'client_sso',
    'scope': 'auth.authenticator',
    'token': 'KR-cfa233bc317d09d8bce6f690bf1fe4ef-1164730913' 
} 
#Key https://account.battle.net/login/en/?ref=localhost

response = requests.post(url, headers=headers, data=data)

print(response.text)
