import requests


r = requests.get('https://api.randomuser.me', params={'results':5})

data = r.json()
for i in data['info']:
    print(i)
