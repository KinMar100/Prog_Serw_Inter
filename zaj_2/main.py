import requests
import json

url = 'https://api.gios.gov.pl/pjp-api/rest/station/findAll'
response = requests.get(url)

print(response.content)