import requests

url = 'http://wmii.uwm.edu.pl/'
response = requests.get(url)

print(response)
print("________")
print(response.status_code)
print("________")
print(response.headers)
print("________")
print(response.content)
print("________")
print(response.content.decode('utf-8'))
print("________")
