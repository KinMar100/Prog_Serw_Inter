import requests
import json

sensor_id = 5766
url = f'https://api.gios.gov.pl/pjp-api/rest/data/getData/{sensor_id}'
response = requests.get(url)

if response.status_code != 200:
    assert False

data = json.loads(response.content.decode('utf-8'))
value = data['values'][0]

print(data)

print(f'Czas: {value["date"]}, wartość odczytu: {value["value"]}')
