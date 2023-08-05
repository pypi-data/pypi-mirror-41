import json


data = {
    'url': 'https://192.168.254.233/0/up/',
    'id': 'ravi61',
    'password': 'mamta267'
}
with open('details.json', 'w') as file:
    json.dump(data, file, indent=4)
