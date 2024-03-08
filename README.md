## 重要提醒

- 本项目纯为爱发电，也从未公布过任何收款方式，单纯因为对守望先锋的热爱。如果你是购买到了与本产品类似的软件，或者花钱享受到了本产品的服务，大概率你被骗了，建议联系商家退款。
- 最后，如果你真的想卖本项目赚钱，请点 [这里了解]([https://www.python.org/downloads/](https://www.baidu.com/s?wd=%E5%AD%A4%E5%84%BF%E6%80%8E%E4%B9%88%E5%8A%9E%E6%88%B7%E5%8F%A3%E6%9C%AC)

# bnt-auth

bnt-auth is a collection of python scripts to help bypass Battle.net's 2 factor authentication system

## Perquisites / Installation

- Install [python](https://www.python.org/downloads/)

```python
git clone https://github.com/dayumsista/bnt-auth.git
```
```
cd bnt-auth
```

## Usage (Windows)


1. Retrieve SSO Token:
Go to [https://account.battle.net/login/en/?ref=localhost](https://account.battle.net/login/en/?ref=localhost). After logging in, ignore the 404 Error, but copy the token following ST= from the URL.
Example: EU-84902f44j57m687039586j7egdfa0a54-1165739690

2. Get Bearer Token:
Replace <SSO_TOKEN> with the token you got from web and execute the following untitled1.py to obtain the Bearer Token:
{"access_token":"XXX","token_type":"bearer","expires_in":0,"scope":"auth.authenticator","sub":"XXX"}

3. Get Serial & Restore Codes:
Use the Bearer Token(access_token) to fetch the Serial and Restore Codes of an existing authenticator:
untitled2 goes to bind a known serial and restoreCode to an account, while untitled3 is to add a brand new
Responce should be
{"serial":"XXX","restoreCode":"XXX","deviceSecret":"XXX","timeMs":0,"requireHealup":false}

4. Winauth
Download Winauth at [https://winauth.github.io/winauth/download.html](https://winauth.github.io/winauth/download.html)
Add - Battle.Net - Import Authenticator - Private Key
Private Key is deviceSecret, just put it in

### Usage example
[Watch on streamable](https://streamable.com/ncodz4)
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Credits
- [BillyCurtis](https://github.com/BillyCurtis) for coming up with this [idea](https://github.com/jleclanche/python-bna/issues/38#issuecomment-1902482544) 

## License

[MIT](https://choosealicense.com/licenses/mit/)
