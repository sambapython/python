import requests
from pprint import pprint # pprint helps in better illustration of json structure
resp = requests.get('http://host:port/users')
pprint(resp.json())

resp = requests.post("http://host:port/users", json={key:value})
pprint(resp.json())
