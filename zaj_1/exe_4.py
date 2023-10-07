import requests
import json

station_id = 877
url = f'https://api.gios.gov.pl/pjp-api/rest/station/sensors/{station_id}'
response = requests.get(url)

if response.status_code != 200:
    exit()

stations = json.loads(response.content.decode('utf-8'))

print(stations)
