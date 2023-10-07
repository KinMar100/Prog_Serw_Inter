import requests
import json

url = 'https://api.gios.gov.pl/pjp-api/rest/station/findAll'
response = requests.get(url)

# print(response.content)

print(response.content.decode('utf-8'))

content = response.content.decode('utf-8')
parsed_content = json.loads(content)

print(type(response.content), type(content), type(parsed_content))

print(parsed_content)

for station in parsed_content:
    print(f'ID: {station["id"]}, nazwa: {station["stationName"]}, miasto: {station["city"]["name"]}, lokalizacja:'
          f' {station["addressStreet"]}')
